"""외부 패키지 없이 Ollama Chat API를 호출하는 작은 클라이언트입니다."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any


DEFAULT_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


class OllamaError(RuntimeError):
    """Ollama API 호출이 실패했을 때 발생합니다."""


def post_json(
    path: str,
    payload: dict[str, Any],
    *,
    base_url: str = DEFAULT_BASE_URL,
    timeout: int = 180,
) -> dict[str, Any]:
    """Ollama API에 JSON을 전송하고 응답을 사전으로 반환합니다."""
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}{path}",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise OllamaError(f"Ollama HTTP {error.code}: {detail}") from error
    except (urllib.error.URLError, TimeoutError) as error:
        raise OllamaError(f"Ollama 연결 실패: {error}") from error


def chat(
    messages: list[dict[str, Any]],
    *,
    model: str = "qwen3:4b",
    tools: list[dict[str, Any]] | None = None,
    response_format: str | dict[str, Any] | None = None,
    base_url: str = DEFAULT_BASE_URL,
    num_ctx: int = 8192,
    num_predict: int = 256,
) -> dict[str, Any]:
    """Ollama 모델에 대화와 선택적 도구 목록을 전달합니다."""
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": False,
        "options": {
            "temperature": 0,
            "num_ctx": num_ctx,
            "num_predict": num_predict,
        },
    }
    if tools:
        payload["tools"] = tools
    if response_format is not None:
        payload["format"] = response_format

    return post_json("/api/chat", payload, base_url=base_url)
