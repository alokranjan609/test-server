from fastmcp import FastMCP
import random

mcp = FastMCP("Remote MCP Server")

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return result"""
    return a + b

@mcp.tool()
def random_number() -> int:
    """Generate a random integer between 1 and 10"""
    return random.randint(1, 10)


if __name__ == "__main__":
    # Run as network server
    mcp.run(transport="http", host="0.0.0.0", port=8000)