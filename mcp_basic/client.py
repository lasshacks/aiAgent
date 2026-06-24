"""stdio로 MCP Server를 실행하고 Tool 목록과 호출 결과를 확인합니다."""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_PATH = Path(__file__).with_name("server.py").resolve()


async def run_client(tool_name: str, arguments: dict[str, object]) -> None:
    """MCP handshake 후 Tool을 검색하고 하나를 호출합니다."""
    server = StdioServerParameters(
        command=sys.executable,
        args=[str(SERVER_PATH)],
        cwd=SERVER_PATH.parent,
        encoding="utf-8",
    )

    async with stdio_client(server) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            initialize_result = await session.initialize()
            print(f"[MCP] server={initialize_result.serverInfo.name}")

            listed = await session.list_tools()
            tool_names = [tool.name for tool in listed.tools]
            print(f"[MCP] tools={tool_names}")
            if tool_name not in tool_names:
                raise ValueError(f"등록되지 않은 Tool입니다: {tool_name}")

            result = await session.call_tool(tool_name, arguments)
            if result.isError:
                raise RuntimeError(f"MCP Tool 실행 실패: {result.content}")

            payload = result.structuredContent
            if payload is None:
                payload = [
                    content.model_dump(mode="json", by_alias=True)
                    for content in result.content
                ]
            print(f"[Tool] {tool_name} -> {json.dumps(payload, ensure_ascii=False)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", choices=("hello", "add_numbers"), default="add_numbers")
    parser.add_argument("--a", type=float, default=12)
    parser.add_argument("--b", type=float, default=30)
    parser.add_argument("--name", default="MCP")
    args = parser.parse_args()

    arguments: dict[str, object]
    if args.tool == "hello":
        arguments = {"name": args.name}
    else:
        arguments = {"a": args.a, "b": args.b}

    try:
        asyncio.run(run_client(args.tool, arguments))
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise SystemExit(f"MCP Client 실행 실패: {error}") from error


if __name__ == "__main__":
    main()
