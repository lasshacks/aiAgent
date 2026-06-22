"""로컬 Ollama 모델의 코드 생성 및 도구 호출 능력을 비교합니다."""

import argparse
import json
import time
import urllib.error
import urllib.request
from typing import Any


CODE_PROMPT = """Return only valid Python code, without Markdown fences.
Implement parse_and_add(a, b). It must accept int, float, and numeric strings,
reject booleans and invalid values with ValueError, return the sum, and include
at least five assert-based tests."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate_sum",
            "description": "Add two numbers",
            "parameters": {
                "type": "object",
                "required": ["a", "b"],
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
            },
        },
    }
]


def post_json(base_url: str, path: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Ollama API에 JSON 요청을 보내고 JSON 응답을 반환합니다."""
    request = urllib.request.Request(
        f"{base_url}{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return json.loads(response.read())


def clean_code(text: str) -> str:
    """모델이 붙인 Markdown 코드 펜스를 제거합니다."""
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        return "\n".join(lines)
    return text


def benchmark_generation(base_url: str, model: str) -> dict[str, Any]:
    """동일한 Python 코드 생성 요청의 속도와 기본 품질을 측정합니다."""
    started = time.perf_counter()
    result = post_json(
        base_url,
        "/api/chat",
        {
            "model": model,
            "messages": [{"role": "user", "content": CODE_PROMPT}],
            "stream": False,
            "think": False,
            "options": {"temperature": 0.2, "num_predict": 128},
        },
    )
    elapsed = time.perf_counter() - started
    content = result.get("message", {}).get("content", "")
    code = clean_code(content)
    try:
        compile(code, f"<{model}>", "exec")
        syntax_valid = True
    except SyntaxError:
        syntax_valid = False

    eval_count = result.get("eval_count", 0)
    eval_duration = result.get("eval_duration", 0)
    tokens_per_second = (
        eval_count / (eval_duration / 1_000_000_000) if eval_duration else 0
    )
    return {
        "wall_seconds": round(elapsed, 2),
        "load_seconds": round(result.get("load_duration", 0) / 1_000_000_000, 2),
        "output_tokens": eval_count,
        "tokens_per_second": round(tokens_per_second, 2),
        "syntax_valid": syntax_valid,
        "has_function": "def parse_and_add" in code,
        "has_five_asserts": code.count("assert ") >= 5,
        "response": content,
    }


def benchmark_tool_call(base_url: str, model: str) -> dict[str, Any]:
    """Agent 작업의 전제인 구조화된 도구 호출 지원 여부를 측정합니다."""
    started = time.perf_counter()
    try:
        result = post_json(
            base_url,
            "/api/chat",
            {
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": "Use calculate_sum to add 12 and 30. Do not calculate it yourself.",
                    }
                ],
                "tools": TOOLS,
                "stream": False,
                "think": False,
                "options": {"temperature": 0, "num_predict": 64},
            },
        )
    except urllib.error.HTTPError as error:
        return {
            "wall_seconds": round(time.perf_counter() - started, 2),
            "supported": False,
            "error": error.read().decode("utf-8", errors="replace"),
        }

    tool_calls = result.get("message", {}).get("tool_calls", [])
    return {
        "wall_seconds": round(time.perf_counter() - started, 2),
        "supported": bool(tool_calls),
        "tool_calls": tool_calls,
        "fallback_content": result.get("message", {}).get("content", ""),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:11434")
    parser.add_argument("models", nargs="*", default=["qwen3:4b", "gemma3:4b"])
    args = parser.parse_args()

    report: dict[str, Any] = {}
    for model in args.models:
        try:
            generation = benchmark_generation(args.base_url, model)
        except (TimeoutError, urllib.error.URLError) as error:
            generation = {"completed": False, "error": str(error)}
        try:
            tool_call = benchmark_tool_call(args.base_url, model)
        except (TimeoutError, urllib.error.URLError) as error:
            tool_call = {"completed": False, "error": str(error)}
        report[model] = {
            "generation": generation,
            "tool_call": tool_call,
        }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
