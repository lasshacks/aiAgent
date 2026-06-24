"""Ollama의 일반 Chat 호출을 확인하는 1단계 실습입니다."""

from __future__ import annotations

import argparse
import time

from ollama_client import OllamaError, chat


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="안녕하세요. 한 문장으로 답해주세요.")
    parser.add_argument("--model", default="gemma3:4b")
    parser.add_argument("--base-url", default=None)
    args = parser.parse_args()

    options = {"model": args.model}
    if args.base_url:
        options["base_url"] = args.base_url

    started = time.perf_counter()
    try:
        response = chat([{"role": "user", "content": args.prompt}], **options)
    except OllamaError as error:
        raise SystemExit(str(error)) from error

    elapsed = time.perf_counter() - started
    message = response.get("message", {})
    print(message.get("content", ""))
    print(f"\nmodel={args.model} elapsed={elapsed:.2f}s tokens={response.get('eval_count', 0)}")


if __name__ == "__main__":
    main()

