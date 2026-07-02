"""Minimal Agent -> MCP integration test.

Flow:

User prompt
  -> local LLM chooses a tool
  -> this script calls the MCP server
  -> MCP server executes the deterministic tool
  -> this script renders the final answer

This is the final step of the 04_MCP basic practice.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from client import call_mcp_tool_sync


ROOT_DIR = Path(__file__).resolve().parents[1]
AGENT_BASIC_DIR = ROOT_DIR / "agent_basic"
sys.path.insert(0, str(AGENT_BASIC_DIR))

from ollama_client import OllamaError, chat  # noqa: E402


MCP_TOOLS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "hello",
            "description": "Return a Korean greeting message for a given name.",
            "parameters": {
                "type": "object",
                "required": ["name"],
                "additionalProperties": False,
                "properties": {
                    "name": {"type": "string", "description": "Name to greet"},
                },
            },
        },
    },
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
]


def select_tool_schema(prompt: str) -> dict[str, Any]:
    """Keep routing narrow so small local models do not wander."""
    lowered = prompt.lower()
    numbers = re.findall(r"-?\d+(?:\.\d+)?", prompt)
    if len(numbers) >= 2 or any(word in lowered for word in ("더해", "합", "add", "sum", "plus")):
        return MCP_TOOLS[1]
    return MCP_TOOLS[0]


def action_schema(tool: dict[str, Any]) -> dict[str, Any]:
    function = tool["function"]
    return {
        "type": "object",
        "required": ["tool", "arguments"],
        "additionalProperties": False,
        "properties": {
            "tool": {"type": "string", "enum": [function["name"]]},
            "arguments": function["parameters"],
        },
    }


def extract_action_with_fallback(
    prompt: str,
    *,
    model: str,
    base_url: str | None,
    selected_tool: dict[str, Any],
) -> tuple[dict[str, Any], bool]:
    """Ask the model for a native tool call, then fall back to JSON schema."""
    function = selected_tool["function"]
    messages = [
        {
            "role": "system",
            "content": (
                "/no_think\n"
                "You are a tool router. Call the provided tool immediately. "
                "Do not answer with normal text."
            ),
        },
        {"role": "user", "content": f"/no_think\n{prompt}"},
    ]

    options: dict[str, Any] = {
        "model": model,
        "tools": [selected_tool],
        "num_predict": 256,
    }
    if base_url:
        options["base_url"] = base_url

    response = chat(messages, **options)
    tool_calls = response.get("message", {}).get("tool_calls", [])
    if tool_calls:
        call = tool_calls[0]
        native_function = call.get("function", {})
        arguments = native_function.get("arguments", {})
        if isinstance(arguments, str):
            arguments = json.loads(arguments)
        return {
            "tool": native_function.get("name"),
            "arguments": arguments,
        }, False

    print("[Agent] Native tool call 실패. JSON Action fallback을 사용합니다.")
    fallback_messages = [
        {
            "role": "system",
            "content": (
                "Return one JSON object only. "
                "Select the supplied function and extract its arguments. "
                "Do not explain."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Function name: {function['name']}\n"
                f"Function description: {function['description']}\n"
                f"User request: {prompt}"
            ),
        },
    ]
    fallback_options: dict[str, Any] = {
        "model": model,
        "response_format": action_schema(selected_tool),
        "num_predict": 128,
    }
    if base_url:
        fallback_options["base_url"] = base_url

    fallback_response = chat(fallback_messages, **fallback_options)
    action = json.loads(fallback_response.get("message", {}).get("content", "{}"))
    return action, True


def render_answer(tool_name: str, payload: dict[str, Any]) -> str:
    if tool_name == "hello":
        return str(payload.get("result"))
    if tool_name == "add_numbers":
        return f"계산 결과는 {payload.get('result')}입니다."
    return json.dumps(payload, ensure_ascii=False)


def run_agent(prompt: str, *, model: str, base_url: str | None) -> int:
    selected_tool = select_tool_schema(prompt)
    action, used_fallback = extract_action_with_fallback(
        prompt,
        model=model,
        base_url=base_url,
        selected_tool=selected_tool,
    )

    tool_name = str(action["tool"])
    arguments = action["arguments"]
    if not isinstance(arguments, dict):
        raise ValueError("Tool arguments must be a JSON object.")

    payload = call_mcp_tool_sync(tool_name, arguments)
    print(f"[MCP Tool] {tool_name} -> {json.dumps(payload, ensure_ascii=False)}")
    print(f"[Agent] {render_answer(tool_name, payload)}")
    print(f"[Fallback] {used_fallback}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="12와 30을 더해줘")
    parser.add_argument("--model", default="qwen3:4b")
    parser.add_argument("--base-url", default=None)
    args = parser.parse_args()

    try:
        raise SystemExit(run_agent(args.prompt, model=args.model, base_url=args.base_url))
    except (OllamaError, OSError, RuntimeError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(f"MCP Agent 실행 실패: {error}") from error


if __name__ == "__main__":
    main()
