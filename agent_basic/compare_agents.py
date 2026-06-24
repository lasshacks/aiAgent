"""직접 구현 Agent와 LangChain Agent를 같은 조건에서 비교합니다."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def run_case(name: str, script: str, prompt: str, base_url: str, timeout: int) -> dict:
    """Agent CLI 하나를 별도 프로세스로 실행하고 결과를 측정합니다."""
    command = [
        sys.executable,
        str(ROOT / script),
        prompt,
        "--base-url",
        base_url,
    ]
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        elapsed = time.perf_counter() - started
        return {
            "name": name,
            "elapsed": elapsed,
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }
    except subprocess.TimeoutExpired as error:
        return {
            "name": name,
            "elapsed": time.perf_counter() - started,
            "returncode": None,
            "stdout": (error.stdout or "").strip(),
            "stderr": f"{timeout}초 timeout",
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="?", default="12와 30을 더해줘")
    parser.add_argument(
        "--base-url",
        default=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    )
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()

    cases = [
        ("Direct", "basic_agent.py"),
        ("LangChain", "langchain_agent.py"),
    ]
    results = [
        run_case(name, script, args.prompt, args.base_url, args.timeout)
        for name, script in cases
    ]

    for result in results:
        status = "TIMEOUT" if result["returncode"] is None else result["returncode"]
        print(f"\n=== {result['name']} ===")
        print(f"elapsed={result['elapsed']:.2f}s, exit={status}")
        if result["stdout"]:
            print(result["stdout"])
        if result["stderr"]:
            print(f"[stderr] {result['stderr']}")

    succeeded = all(result["returncode"] == 0 for result in results)
    raise SystemExit(0 if succeeded else 1)


if __name__ == "__main__":
    main()
