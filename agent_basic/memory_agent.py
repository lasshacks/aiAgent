"""대화 이력을 JSON 파일에 저장하는 Tool Calling Agent 실습입니다."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from agent_core import agent_answer
from ollama_client import OllamaError


DEFAULT_MEMORY_PATH = Path(__file__).with_name("memory.json")
MAX_MESSAGES = 10


def load_memory(path: Path) -> list[dict[str, Any]]:
    """저장된 대화 이력을 불러옵니다."""
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Memory 파일은 JSON 배열이어야 합니다.")
    return [item for item in data if isinstance(item, dict)][-MAX_MESSAGES:]


def save_memory(path: Path, messages: list[dict[str, Any]]) -> None:
    """최근 대화만 임시 파일을 거쳐 안전하게 저장합니다."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(messages[-MAX_MESSAGES:], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="12와 30을 더해줘.")
    parser.add_argument("--model", default="qwen3:4b")
    parser.add_argument("--base-url", default=None)
    parser.add_argument("--memory", type=Path, default=DEFAULT_MEMORY_PATH)
    parser.add_argument("--clear", action="store_true")
    parser.add_argument("--show", action="store_true")
    args = parser.parse_args()

    if args.clear:
        args.memory.unlink(missing_ok=True)
        print("Memory를 초기화했습니다.")
        return

    history = load_memory(args.memory)
    if args.show:
        print(json.dumps(history, ensure_ascii=False, indent=2))
        return

    try:
        answer, name, result, used_fallback = agent_answer(
            args.prompt,
            model=args.model,
            base_url=args.base_url,
            history=history,
        )
    except (OllamaError, ValueError, TypeError, json.JSONDecodeError) as error:
        raise SystemExit(f"Memory Agent 실행 실패: {error}") from error

    history.extend(
        [
            {"role": "user", "content": args.prompt},
            {"role": "assistant", "content": answer},
        ]
    )
    save_memory(args.memory, history)
    print(f"[Tool] {name} -> {json.dumps(result, ensure_ascii=False)}")
    print(f"[Agent] {answer}")
    print(f"[Memory] {args.memory} 저장, fallback={used_fallback}")


if __name__ == "__main__":
    main()
