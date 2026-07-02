"""Run the MCP server over stdio and call one tool directly.

This file is a direct MCP client test. It does not use an LLM.
Use it to verify:

1. server process startup
2. MCP initialize handshake
3. tool discovery
4. tool execution
5. structured result return
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_PATH = Path(__file__).with_name("server.py").resolve()


async def call_mcp_tool(tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Start the local MCP server and call one tool."""
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
                raise ValueError(f"등록되지 않은 MCP Tool입니다: {tool_name}")

            result = await session.call_tool(tool_name, arguments)
            if result.isError:
                raise RuntimeError(f"MCP Tool 실행 실패: {result.content}")

            if result.structuredContent is not None:
                return dict(result.structuredContent)

            return {
                "content": [
                    content.model_dump(mode="json", by_alias=True)
                    for content in result.content
                ]
            }


def call_mcp_tool_sync(tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Synchronous wrapper for scripts that do not manage an event loop."""
    return asyncio.run(call_mcp_tool(tool_name, arguments))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", choices=("hello", "add_numbers"), default="add_numbers")
    parser.add_argument("--a", type=float, default=12)
    parser.add_argument("--b", type=float, default=30)
    parser.add_argument("--name", default="MCP")
    args = parser.parse_args()

    if args.tool == "hello":
        arguments: dict[str, Any] = {"name": args.name}
    else:
        arguments = {"a": args.a, "b": args.b}

    try:
        payload = call_mcp_tool_sync(args.tool, arguments)
        print(f"[Tool] {args.tool} -> {json.dumps(payload, ensure_ascii=False)}")
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise SystemExit(f"MCP Client 실행 실패: {error}") from error


if __name__ == "__main__":
    main()
