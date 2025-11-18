
import logging
import time
import uvicorn
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

try:
    from .server import server, api_key_var
except ImportError:
    from server import server, api_key_var

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("mcp_server")


def create_app():
    sse = SseServerTransport("/messages")

    def _extract_api_key(request: Request) -> str | None:
        # 1. Try Query Parameter
        query_key = request.query_params.get("TC_API_KEY")
        if query_key:
            return query_key

        # 2. Try Authorization Header
        auth_header = request.headers.get("Authorization")
        if auth_header:
            # Support "Bearer <token>" or "token <token>" or just "<token>"
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() in ("bearer", "token"):
                return parts[1]
            return auth_header
            
        return None

    async def handle_sse(scope, receive, send):
        request = Request(scope, receive)
        api_key = _extract_api_key(request)
        token = None
        if api_key:
            token = api_key_var.set(api_key)
        
        try:
            logger.info("New SSE connection initiated")
            async with sse.connect_sse(scope, receive, send) as streams:
                await server.run(
                    streams[0],
                    streams[1],
                    server.create_initialization_options()
                )
        except Exception as e:
            logger.error(f"SSE connection error: {e}")
            raise
        finally:
            if token:
                api_key_var.reset(token)
            logger.info("SSE connection closed")

    async def handle_messages(scope, receive, send):
        request = Request(scope, receive)
        api_key = _extract_api_key(request)
        token = None
        if api_key:
            token = api_key_var.set(api_key)
            
        try:
            await sse.handle_post_message(scope, receive, send)
        except Exception as e:
            logger.error(f"Message handling error: {e}")
            raise
        finally:
            if token:
                api_key_var.reset(token)

    async def app(scope, receive, send):
        path = scope.get("path")
        method = scope.get("method")
        
        if path == "/sse" or path == "/":
            if method != "GET":
                logger.warning(f"Invalid method {method} for {path}")
                response = Response("Method Not Allowed", status_code=405)
                await response(scope, receive, send)
                return
            await handle_sse(scope, receive, send)
        elif path == "/messages":
            if method != "POST":
                logger.warning(f"Invalid method {method} for /messages")
                response = Response("Method Not Allowed", status_code=405)
                await response(scope, receive, send)
                return
            await handle_messages(scope, receive, send)
        else:
            response = Response("Not Found", status_code=404)
            await response(scope, receive, send)

    # Apply CORS Middleware manually
    app = CORSMiddleware(
        app,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )

    return app

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(create_app(), host="0.0.0.0", port=port)
