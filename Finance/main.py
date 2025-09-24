"""
FastMCP quickstart for Finance.

cd to the `Finance` directory and run:
    uv init .
    uv add "mcp[cli]"
    uv add "requests"
    uv run mcp install main
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Finance Demo", dependencies=["requests"])

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."

# Add a tool to fetch market news
@mcp.tool()
def get_market_news() -> str:
    """Fetch the latest market news from Seeking Alpha API"""
    from seekingAlpha import fetch_market_news
    return fetch_market_news()

# Add a tool to get stock quotes
@mcp.tool()
def get_stock_quote(symbol: str) -> str:
    """Fetch the global stock quote for a given symbol from Alpha Vantage API"""
    from seekingAlpha import get_global_quote
    return get_global_quote(symbol)
