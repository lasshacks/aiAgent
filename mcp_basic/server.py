"""Basic MCP server for AI Platform Engineering Lab.

This server exposes deterministic tools over stdio transport.
It is intentionally small so that the MCP handshake, tool discovery,
and tool call flow can be tested before connecting real infra tools.
"""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "ai-platform-study",
    instructions="Basic MCP tool server for AI Platform Engineering Lab.",
)


@mcp.tool()
def hello(name: str = "MCP") -> dict[str, str]:
    """Return a Korean greeting message."""
    return {"result": f"안녕하세요, {name}!"}


@mcp.tool()
def add_numbers(a: float, b: float) -> dict[str, float]:
    """Add two numbers and return the result."""
    return {"result": a + b}


if __name__ == "__main__":
    mcp.run(transport="stdio")
