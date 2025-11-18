# TutorCruncher MCP Server

A production-grade, streamable HTTP MCP server that exposes the TutorCruncher SDK to agentic AI workflows.

## 1. Configuration Snippet

To register this tool with your MCP agent runtime, use the following configuration:

```json
"mcp_tools": [
  {
    "server_label": "tutorcruncher",
    "url": "https://<your-mcp-server-host>/sse",
    "type": "http",
    "headers": {
      "Authorization": "Bearer YOUR_TC_API_KEY"
    }
  }
]
```

## 2. Example Agent Usage

**Prompt:**
> Please use the "clients_list_all_clients" tool from server "tutorcruncher" with parameters { "limit": 5, "status": "prospect" } and await the result.

**JSON-RPC Request (Internal):**
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "clients_list_all_clients",
    "arguments": {
      "limit": 5,
      "status": "prospect"
    }
  },
  "id": 1
}
```

**Response:**
The server returns a JSON result containing the list of clients. If the SDK method supports streaming, the response will be delivered via SSE chunks.

## 3. Setup & Deployment

### Prerequisites
- Python 3.11+
- Docker (optional but recommended)
- A TutorCruncher API Key

### Local Setup
```bash
cd MCP
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e ..
export TC_API_KEY="token <YOUR_KEY>" # Optional if passed via headers
python sse_server.py
```
Server listens on `http://0.0.0.0:8000`.

### Docker Deployment
```bash
# Build
docker build -f MCP/Dockerfile -t tc-mcp-server .

# Run (Option A: Server-side Auth)
docker run -p 8000:8000 -e TC_API_KEY="token <YOUR_KEY>" tc-mcp-server

# Run (Option B: Client-side Auth)
# No env var needed; client must send Authorization header
docker run -p 8000:8000 tc-mcp-server
```

## 4. Authentication

The server supports two authentication methods:

1.  **Header-Based (Recommended):**
    Pass `Authorization: Bearer <API_KEY>` or `Authorization: token <API_KEY>` in the HTTP headers. This allows multi-tenant usage where the agent provides the key.

2.  **Environment Variable:**
    Set `TC_API_KEY` in the server environment. This key is used as a fallback if no header is provided.

## 5. Tool List

The server dynamically exposes **all** available resources and methods from the `tc_api_sdk` (approx. 90+ tools).

Common tools include:
- `clients_list_all_clients`
- `clients_get_a_client`
- `agents_list_all_agents`
- `appointments_list_all_appointments`

## 6. Streaming Semantics

The server uses **Server-Sent Events (SSE)** for transport.
- **Transport Streaming:** All communication happens over a persistent HTTP connection (`/sse`), allowing the server to push JSON-RPC responses asynchronously.
- **Data Streaming:** If an SDK method returns a generator or stream, the server will push partial results as they become available (implementation dependent on SDK capabilities).

## 7. Security Checklist

- [x] **Authentication:** Validates `Authorization` header or falls back to server-side key.
- [x] **Authorization:** API key is injected into the SDK client context for every request.
- [x] **Logging:** Structured logging captures request method, path, status, and duration.
- [x] **Safe Argument Handling:** Tool arguments are passed as kwargs to the typed SDK methods.
- [x] **HTTPS:** Recommended to run behind a reverse proxy (Nginx, AWS ALB) terminating TLS.
