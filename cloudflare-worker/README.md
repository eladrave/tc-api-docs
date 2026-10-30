# TutorCruncher MCP on Cloudflare Workers

This is a native JavaScript Cloudflare Worker port of the Python MCP in `../MCP/`.
The tool allowlist is generated from `../tc_api_sdk/generated/api_schema.json`: **97 operations** across 29 resources.
It talks directly to the TutorCruncher HTTPS API and does not depend on the previous Cloud Run service.

## Endpoints

- `https://tcmcp.shellyrave.com/mcp`: stateless MCP Streamable HTTP, JSON-RPC over POST
- `https://tcmcp.shellyrave.com/health`: unauthenticated service health (does not check TutorCruncher credentials)
- `/sse`: POST alias for migration; deprecated GET/SSE transport is not implemented

## Authentication

**Per-client API credentials (default):** pass the TutorCruncher API key in
`Authorization: Bearer <TUTORCRUNCHER_API_KEY>`, or in
`X-TutorCruncher-API-Key`. The key is forwarded only to
`https://secure.tutorcruncher.com` as the TutorCruncher `token` auth scheme.
For backwards compatibility, `?TC_API_KEY=...` is also supported, but **avoid it**:
URL query strings may be stored in logs, histories, and analytics.

**Managed server credentials (optional):** set BOTH Worker secrets `TC_API_KEY`
and `MCP_ACCESS_TOKEN`. Callers must provide `Authorization: Bearer <MCP_ACCESS_TOKEN>`
or `X-MCP-Token`; the Worker forwards only the server-side `TC_API_KEY` upstream.
The Worker deliberately refuses to use a shared `TC_API_KEY` without an access token.

Never commit credentials or log request headers/body.

## Deploy

```bash
cd cloudflare-worker
npx wrangler deploy
# Optional managed mode, set both secrets:
npx wrangler secret put TC_API_KEY
npx wrangler secret put MCP_ACCESS_TOKEN
```

The Cloudflare zone must belong to the same account as the Worker. The custom domain
is configured as a Worker origin, not as a manually-created A or CNAME record.

## Verify

```bash
curl -fsS https://tcmcp.shellyrave.com/health
curl -fsS https://tcmcp.shellyrave.com/mcp \
  -H "Authorization: Bearer $TUTORCRUNCHER_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

To test live TutorCruncher access, call `clients_list_all_clients` with `params: {"limit": 1}`.

## Protocol and differences from Python implementation

This port implements stateless Streamable HTTP using JSON responses, not legacy
persistent SSE transport. Supported MCP methods include `initialize`,
`ping`, `tools/list`, `tools/call`, `resources/list`, and `resources/read`.
The schema resource exposes the compact operation catalog, rather than the Python
SDK's full model definitions. The legacy Python `model` and `raw` tool arguments
are accepted for compatibility but responses remain raw JSON/text. All 97 API
operations retain their original names, HTTP methods and paths.

Caution: the catalog includes mutations such as invoice payments and deletes.
Restrict who has valid credentials and use client-side approval for write tools.
