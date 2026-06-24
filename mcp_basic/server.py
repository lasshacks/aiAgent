"""첫 번째 MCP Server: hello와 add_numbers Tool을 stdio로 제공합니다."""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP(
    "ai-platform-study",
    instructions="AI Platform Engineering Lab의 기본 MCP Tool 서버입니다.",
)


@mcp.tool()
def hello(name: str = "MCP") -> str:
    """입력한 이름을 포함한 인사말을 반환합니다."""
    return f"안녕하세요, {name}!"


@mcp.tool()
def add_numbers(a: float, b: float) -> dict[str, float]:
    """두 숫자를 더하고 계산 결과를 반환합니다."""
    return {"result": a + b}


if __name__ == "__main__":
    mcp.run(transport="stdio")
