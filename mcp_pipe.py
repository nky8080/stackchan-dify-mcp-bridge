"""
mcp_pipe.py

Generic MCP pipe: launches the MCP server script passed as a command-line
argument and bridges StackChan's requests to it.

Usage:
    python mcp_pipe.py <your_mcp_server_script>.py

This file is intentionally generic — it does not know about any specific
Dify agent or knowledge base. Server-specific logic (e.g. Kanazawa tourism)
lives in scripts under examples/.

Based on: mcp_pipe.py from 78/mcp-calculator
          (https://github.com/78/mcp-calculator).
          The source repository's README states the project is under the
          MIT License, though no separate LICENSE file is present in that
          repository at the time of writing. Attribution given to GitHub
          user "78" (repository owner) accordingly.
Modifications: adapted for use as a generic StackChan-to-Dify MCP bridge.
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mcp_pipe.py <mcp_server_script.py>")
        sys.exit(1)

    target_script = sys.argv[1]
    # TODO: actual pipe/launch logic — start target_script as the MCP server
    # and relay StackChan's requests/responses between it and the device.
    print(f"Would launch MCP server: {target_script}")
