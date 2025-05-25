from mcp.server.fastmcp import FastMCP
import time
import signal
import sys

# Handle Ctrl+C
def signal_handler(sig, frame):
    print("Shutting down server gracefully..")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Create the MCP server
mcp = FastMCP(
    name="count-r",
    host="127.0.0.1",
    port=5000,
    timeout=30
)

# Define your tool
@mcp.tool()
def count_r(word: str) -> int:
    """Count the number of 'r' letters in a given word."""
    try:
        if not isinstance(word, str):
            return 0
        return word.lower().count("r")
    except Exception:
        return 0

if __name__ == "__main__":
    try:
        print("Starting MCP Server 'count-r' on 127.0.0.1:5000")
        mcp.run()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
