# TutorCruncher MCP Server

This folder contains a Python [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server that exposes TutorCruncher API capabilities via the SDK. Any MCP-compatible agent (VS Code, Claude Desktop/Code, Cursor, etc.) can connect to it and use the provided tools/resources.

## Prerequisites

1. Python 3.10+
2. The `mcp` package (server runtime + CLI inspector)
3. A TutorCruncher API token with read permissions (set in `TC_API_KEY`)

## Setup

```bash
cd MCP
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # installs the MCP runtime
pip install -e ..                # exposes the local tc_api_sdk package
export TC_API_KEY="token <API KEY>"
```

## Running the server

Two options:

```bash
# Run through the MCP CLI inspector (recommended while testing)
mcp dev server.py

# Or run directly:
python server.py
```

Both commands launch a stdin/stdout MCP server named _TutorCruncher SDK Server_. The `dev` command also opens the MCP Inspector web UI so you can invoke tools and inspect resources without configuring an IDE.

## Tools exposed

| Tool | Description |
| --- | --- |
| `list_clients(status=None, limit=10)` | Retrieves a page of clients, optionally filtered by status (e.g. `prospect`) |
| `get_client_details(client_id)` | Fetches a single client's full record |
| `list_appointments(status='planned', limit=5)` | Fetches upcoming appointments |
| `paginate_prospect_clients(limit=25, pages=2)` | Demonstrates multi-page traversal for prospect clients |

All tools return plain JSON-compatible dictionaries, making them easy to consume within agent workflows.

## Resources

`tutorcruncher://schema` exposes the raw `tc_api_sdk` schema so agents can inspect metadata (resource names, endpoints, etc.) from MCP.

## Connecting from IDEs

Once the server runs locally, configure your MCP-enabled IDE/client with:

- Transport: `stdio` (usually automatic for local adapters)
- Command: `python /path/to/server.py` (ensure `TC_API_KEY` is in the environment)

Each client has its own connector settings; consult the client's MCP documentation for connection details.
