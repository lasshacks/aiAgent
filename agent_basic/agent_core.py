"""LLM의 tool call을 로컬 Python 함수 실행으로 연결하는 최소 Agent입니다."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from typing import Any, Callable

from ollama_client import OllamaError, chat


def add_numbers(a: float, b: float) -> dict[str, float]:
    """두 숫자를 더합니다."""
    return {"result": a + b}


def get_current_time() -> dict[str, str]:
    """현재 로컬 시각을 ISO 8601 문자열로 반환합니다."""
    return {"current_time": datetime.now().astimezone().isoformat(timespec="seconds")}


TOOL_FUNCTIONS: dict[str, Callable[..., dict[str, Any]]] = {
    "add_numbers": add_numbers,
    "get_current_time": get_current_time,
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Add two numbers and return the numeric result.",
            "parameters": {
                "type": "object",
                "required": ["a", "b"],
                "additionalProperties": False,
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Return the current local date and time.",
            "parameters": {
                "type": "object",
                "additionalProperties": False,
                "properties": {},
            },
        },
    },
]


RESULT_PATTERN = re.compile(r"계산 결과는\s*(-?\d+(?:\.\d+)?)입니다")
RESULT_REFERENCES = ("그 결과", "이 결과", "previous result", "that result")


def resolve_result_reference(
    prompt: str,
    history: list[dict[str, Any]] | None,
) -> tuple[str, str | None]:
    """후속 질문의 결과 참조를 가장 최근 계산값으로 확정합니다."""
    if not any(reference in prompt.lower() for reference in RESULT_REFERENCES):
        return prompt, None

    for message in reversed(history or []):
        if message.get("role") != "assistant":
            continue
        match = RESULT_PATTERN.search(str(message.get("content", "")))
        if match:
            value = match.group(1)
            resolved = prompt
            for reference in RESULT_REFERENCES:
                resolved = re.sub(re.escape(reference), value, resolved, flags=re.IGNORECASE)
            return resolved, value

    return prompt, None


def select_tool(prompt: str) -> dict[str, Any]:
    """질문의 키워드에 따라 모델에 노출할 도구를 하나로 제한합니다."""
    lowered = prompt.lower()
    if any(keyword in lowered for keyword in ("시간", "시각", "날짜", "time", "date")):
        return TOOLS[1]
    return TOOLS[0]


def action_schema(tool: dict[str, Any]) -> dict[str, Any]:
    """선택된 도구만 허용하는 JSON Action 스키마를 생성합니다."""
    function = tool["function"]
    return {
        "type": "object",
        "required": ["tool", "arguments"],
        "properties": {
            "tool": {"type": "string", "enum": [function["name"]]},
            "arguments": function["parameters"],
        },
    }


def execute_tool_call(tool_call: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    """검증된 도구 이름과 인자로 로컬 함수를 실행합니다."""
    function = tool_call.get("function", {})
    name = function.get("name", "")
    arguments = function.get("arguments", {})
    if isinstance(arguments, str):
        arguments = json.loads(arguments)

    if name not in TOOL_FUNCTIONS:
        raise ValueError(f"허용되지 않은 도구입니다: {name}")
    if not isinstance(arguments, dict):
        raise ValueError("도구 인자는 JSON 객체여야 합니다.")

    return name, TOOL_FUNCTIONS[name](**arguments)


def deduplicate_tool_calls(tool_calls: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """동일한 도구와 인자의 중복 호출을 하나로 축약합니다."""
    unique: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for tool_call in tool_calls:
        function = tool_call.get("function", {})
        name = function.get("name", "")
        arguments = function.get("arguments", {})
        if isinstance(arguments, str):
            arguments = json.loads(arguments)
        key = (name, json.dumps(arguments, ensure_ascii=False, sort_keys=True))
        if key not in seen:
            seen.add(key)
            unique.append(tool_call)
    return unique


def request_json_action(
    prompt: str,
    *,
    model: str,
    tool: dict[str, Any],
    base_url: str | None,
    history: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Native tool call 실패 시 JSON Schema로 도구 선택 결과를 요청합니다."""
    function = tool["function"]
    history_text = "\n".join(
        f"{item.get('role', 'unknown')}: {item.get('content', '')}"
        for item in (history or [])[-6:]
    )
    messages = [
        {
            "role": "system",
            "content": (
                "Return one JSON object only. Select the supplied function and extract its "
                "arguments from the user request. Do not explain or calculate the result."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Function name: {function['name']}\n"
                f"Function description: {function['description']}\n"
                f"Conversation history:\n{history_text or '(empty)'}\n"
                f"User request: {prompt}"
            ),
        },
    ]
    options: dict[str, Any] = {
        "model": model,
        "response_format": action_schema(tool),
        "num_predict": 96,
    }
    if base_url:
        options["base_url"] = base_url

    response = chat(messages, **options)
    content = response.get("message", {}).get("content", "")
    try:
        action = json.loads(content)
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON Action 파싱 실패: {content}") from error

    expected_name = function["name"]
    if action.get("tool") != expected_name:
        raise ValueError(f"허용되지 않은 JSON Action입니다: {action}")
    if not isinstance(action.get("arguments"), dict):
        raise ValueError("JSON Action의 arguments는 객체여야 합니다.")
    return action


def render_final_answer(prompt: str, name: str, result: dict[str, Any]) -> str:
    """도구별 결과를 사용자가 읽을 수 있는 최소 답변으로 변환합니다."""
    del prompt
    if name == "add_numbers":
        return f"계산 결과는 {result['result']}입니다."
    if name == "get_current_time":
        return f"현재 시각은 {result['current_time']}입니다."
    return json.dumps(result, ensure_ascii=False)


def agent_answer(
    prompt: str,
    *,
    model: str,
    base_url: str | None = None,
    history: list[dict[str, Any]] | None = None,
) -> tuple[str, str, dict[str, Any], bool]:
    """Agent 한 사이클을 수행하고 답변·도구·결과·fallback 여부를 반환합니다."""
    resolved_prompt, referenced_result = resolve_result_reference(prompt, history)
    if referenced_result is not None:
        print(f"[Memory] 최신 계산 결과 {referenced_result}(으)로 참조를 해석했습니다.")

    selected_tool = select_tool(resolved_prompt)
    selected_name = selected_tool["function"]["name"]
    messages: list[dict[str, Any]] = [
        {
            "role": "system",
            "content": (
                "/no_think\n"
                "You are a function-calling router. "
                f"Call {selected_name} immediately. "
                "Do not explain, reason, calculate, or answer with text. "
                "Your only valid response is one native tool call."
            ),
        },
    ]
    messages.extend((history or [])[-6:])
    messages.append({"role": "user", "content": f"/no_think\n{resolved_prompt}"})
    options: dict[str, Any] = {
        "model": model,
        "tools": [selected_tool],
        "num_predict": 512,
    }
    if base_url:
        options["base_url"] = base_url

    first = chat(messages, **options)
    assistant_message = first.get("message", {})
    tool_calls = assistant_message.get("tool_calls", [])
    used_fallback = False

    if not tool_calls:
        print("[Agent] Native tool call 실패. JSON Action fallback을 사용합니다.")
        used_fallback = True
        action = request_json_action(
            resolved_prompt,
            model=model,
            tool=selected_tool,
            base_url=base_url,
            history=history,
        )
        tool_calls = [
            {
                "function": {
                    "name": action["tool"],
                    "arguments": action["arguments"],
                }
            }
        ]

    original_call_count = len(tool_calls)
    tool_calls = deduplicate_tool_calls(tool_calls)
    if original_call_count > len(tool_calls):
        print(f"[Agent] 동일한 tool call {original_call_count}개를 1개로 정규화했습니다.")
    if len(tool_calls) != 1:
        raise ValueError(f"한 번에 하나의 도구 호출만 허용합니다: {tool_calls}")

    name, result = execute_tool_call(tool_calls[0])
    answer = render_final_answer(resolved_prompt, name, result)
    return answer, name, result, used_fallback


def run_agent(
    prompt: str,
    *,
    model: str,
    base_url: str | None = None,
    history: list[dict[str, Any]] | None = None,
) -> int:
    """Agent 한 사이클을 실행하고 사람이 읽을 수 있는 로그를 출력합니다."""
    answer, name, result, _ = agent_answer(
        prompt,
        model=model,
        base_url=base_url,
        history=history,
    )
    print(f"[Tool] {name} -> {json.dumps(result, ensure_ascii=False)}")
    print(f"[Agent] {answer}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="12와 30을 더한 결과를 알려줘.")
    parser.add_argument("--model", default="qwen3:4b")
    parser.add_argument("--base-url", default=None)
    args = parser.parse_args()

    try:
        raise SystemExit(run_agent(args.prompt, model=args.model, base_url=args.base_url))
    except (OllamaError, ValueError, TypeError, json.JSONDecodeError) as error:
        raise SystemExit(f"Agent 실행 실패: {error}") from error
