# StackChan-Dify MCP Bridge

A lightweight MCP (Model Context Protocol) bridge that connects an M5Stack **StackChan** to a **Dify** agent, letting StackChan answer voice questions using any knowledge base you configure in Dify.

`mcp_pipe.py` is generic: point it at any MCP server script implementing your own tool/knowledge logic, and it handles piping StackChan's requests to that server.

> **Used in:** [Samurai StackChan: Tourism Guide for Kanazawa](#) — a Hackster.io entry for the M5Stack Global Innovation Contest 2026, using this bridge with a Kanazawa-tourism knowledge base. See [`examples/kanazawa_tourism`](./examples/kanazawa_tourism) for that implementation.
> (Replace the `#` above with the actual Hackster project URL once published.)

## What This Is

- `mcp_pipe.py` — generic MCP client/pipe that launches and communicates with an MCP server script
- `examples/` — example MCP server implementations built on top of this bridge, each targeting a specific Dify agent/knowledge base

This repo focuses on the **software bridge only**. Hardware build details (StackChan assembly, custom helmet, etc.) for the Kanazawa tourism guide are documented on its Hackster.io project page, not here.

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- A running Dify instance, exposed as (or wrapped to behave as) an MCP-compatible endpoint
- An M5Stack StackChan (or compatible M5Stack device) running firmware that can talk to this pipe

## Setup

```bash
uv venv
# Windows
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

uv pip sync requirements.txt
uv pip install fastmcp
```

## Usage

```bash
python mcp_pipe.py <your_mcp_server_script>.py
```

For example, to run the Kanazawa tourism example:

```bash
python mcp_pipe.py examples/kanazawa_tourism/kanazawa_tourism.py
```

## Writing Your Own MCP Server Script

Any script following the same interface as [`examples/kanazawa_tourism/kanazawa_tourism.py`](./examples/kanazawa_tourism/kanazawa_tourism.py) can be plugged into `mcp_pipe.py`. At minimum, it should:

1. Expose an MCP-compatible tool/endpoint that accepts a user query
2. Forward that query to your Dify agent
3. Return the agent's response text back through the pipe to StackChan

See the example folder for a working reference implementation, including how its Dify knowledge base was configured.

## Environment Variables

Copy `.env.example` to `.env` and fill in your own Dify endpoint/key. **Never commit real API keys.**

## Acknowledgments

`mcp_pipe.py` is based on the `mcp_pipe.py` from [78/mcp-calculator](https://github.com/78/mcp-calculator) by GitHub user "78", adapted here as a generic StackChan-to-Dify MCP bridge. That repository's README states it is under the MIT License; no separate LICENSE file was present there at the time of writing.

## License

See [`LICENSE`](./LICENSE).
