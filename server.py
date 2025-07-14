# server.py
# import sqlite3
# from starlette.routing import Mount
# from starlette.applications import Starlette
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")
# mcp_echo = FastMCP("Echo")

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

@mcp.resource("file://documents/{name}")
def read_document(name: str) -> str:
    """Read a document by name."""
    # This would normally read from disk
    return f"Content of {name}"

@mcp.resource("config://settings")
def get_settings() -> str:
    """Get application settings."""
    return """{
    "theme": "dark",
    "language": "en",
    "debug": false
    }"""

@mcp.resource("usage://guide")
def get_usage() -> str:
    with open("docs/usage.txt") as f:
        return f.read()

# @mcp_echo.resource("echo://{message}")
# def echo_resource(message: str) -> str:
#     """Echo a message as a resource"""
#     return f"Resource echo: {message}"

# @mcp_echo.tool()
# def echo_tool(message: str) -> str:
#     """Echo a message as a tool"""
#     return f"Tool echo: {message}"

# @mcp_echo.prompt()
# def echo_prompt(message: str) -> str:
#     """Create an echo prompt"""
#     return f"Please process this message: {message}"


# uv run mcp dev server.py

if __name__ == "__main__":
    mcp.run(transport="sse")
    # uv run server.py