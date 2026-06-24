"""LangChain으로 구현한 단발성 Ollama Tool Calling Agent 비교 예제."""

from __future__ import annotations

import argparse
import json
import os
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from agent_core import (
    action_schema,
    deduplicate_tool_calls,
    execute_tool_call,
    render_final_answer,
    select_tool,
)


@tool
def add_numbers(a: float, b: float) -> dict[str, float]:
    """Add two numbers and return the numeric result."""
    return {"result": a + b}


@tool
def get_current_time() -> dict[str, str]:
    """Return the current local date and time."""
    # 실제 실행은 agent_core의 동일한 allowlist 함수가 담당한다.
    return {}


LANGCHAIN_TOOLS = {
    "add_numbers": add_numbers,
    "get_current_time": get_current_time,
}


def normalize_tool_calls(tool_calls: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """LangChain tool call 형식을 기존 실행기의 형식으로 변환한다."""
    return [
        {
            "function": {
                "name": call.get("name", ""),
                "arguments": call.get("args", {}),
            }
        }
        for call in tool_calls
    ]


def request_structured_action(
    llm: ChatOllama,
    prompt: str,
    selected_tool: dict[str, Any],
) -> dict[str, Any]:
    """bind_tools 실패 시 LangChain structured output으로 Action을 강제한다."""
    function = selected_tool["function"]
    structured_llm = llm.with_structured_output(
        action_schema(selected_tool),
        method="json_schema",
    )
    action = structured_llm.invoke(
        [
            SystemMessage(
                content=(
                    "/no_think\nReturn one JSON object only. "
                    f"Use tool {function['name']} and extract its arguments. "
                    "Do not explain or calculate the result."
                )
            ),
            HumanMessage(content=f"/no_think\n{prompt}"),
        ]
    )
    if not isinstance(action, dict):
        raise ValueError(f"Structured Action이 객체가 아닙니다: {action}")
    if action.get("tool") != function["name"]:
        raise ValueError(f"허용되지 않은 Structured Action입니다: {action}")
    if not isinstance(action.get("arguments"), dict):
        raise ValueError(f"Structured Action arguments가 객체가 아닙니다: {action}")
    return action


def run_langchain_agent(prompt: str, *, model: str, base_url: str) -> int:
    """LangChain의 bind_tools로 도구 호출을 받아 공통 실행기로 처리한다."""
    selected_tool = select_tool(prompt)
    selected_name = selected_tool["function"]["name"]
    llm = ChatOllama(
        model=model,
        base_url=base_url,
        reasoning=False,
        temperature=0,
        num_ctx=8192,
        num_predict=256,
        client_kwargs={"timeout": 120.0},
    )
    model_with_tools = llm.bind_tools(
        [LANGCHAIN_TOOLS[selected_name]],
        tool_choice=selected_name,
    )
    response = model_with_tools.invoke(
        [
            SystemMessage(
                content=(
                    "/no_think\nYou are a function-calling router. "
                    f"Call {selected_name} immediately. Do not explain or answer with text."
                )
            ),
            HumanMessage(content=f"/no_think\n{prompt}"),
        ]
    )

    tool_calls = deduplicate_tool_calls(normalize_tool_calls(response.tool_calls))
    used_fallback = False
    if not tool_calls:
        used_fallback = True
        content_preview = str(response.content).replace("\n", " ")[:300]
        print("[Agent] LangChain bind_tools 호출 실패. structured output fallback을 사용합니다.")
        print(f"[Debug] model content: {content_preview or '(empty)'}")
        action = request_structured_action(llm, prompt, selected_tool)
        tool_calls = [
            {
                "function": {
                    "name": action["tool"],
                    "arguments": action["arguments"],
                }
            }
        ]

    tool_calls = deduplicate_tool_calls(tool_calls)
    if len(tool_calls) != 1:
        raise ValueError(f"도구 호출 하나가 필요하지만 {len(tool_calls)}개를 받았습니다: {tool_calls}")

    name, result = execute_tool_call(tool_calls[0])
    answer = render_final_answer(prompt, name, result)
    print(f"[Tool] {name} -> {json.dumps(result, ensure_ascii=False)}")
    print(f"[Agent] {answer}")
    route = "structured_output_fallback" if used_fallback else "bind_tools"
    print(f"[Framework] LangChain {route}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="12와 30을 더해줘")
    parser.add_argument("--model", default="qwen3:4b")
    parser.add_argument(
        "--base-url",
        default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    )
    args = parser.parse_args()

    try:
        raise SystemExit(
            run_langchain_agent(args.prompt, model=args.model, base_url=args.base_url)
        )
    except (ValueError, TypeError, OSError, TimeoutError) as error:
        raise SystemExit(f"LangChain Agent 실행 실패: {error}") from error


if __name__ == "__main__":
    main()
