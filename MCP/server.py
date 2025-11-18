"""MCP server exposing TutorCruncher SDK functionality."""
from __future__ import annotations

import asyncio
import inspect
import os
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    JSONRPCMessage,
    Resource,
)
import mcp.types as types

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tc_api_sdk import (  # noqa: E402
    TutorCruncherClient,
    models,
    spec,
)
from tc_api_sdk.resources import RESOURCE_CLASSES  # noqa: E402

# Initialize the server
server = Server("TutorCruncher SDK Server")

# Context variable to store API key from request
from contextvars import ContextVar
api_key_var: ContextVar[Optional[str]] = ContextVar("api_key", default=None)

def _require_api_key() -> str:
    # First check context var (from request header)
    api_key = api_key_var.get()
    if api_key:
        return api_key
    
    # Fallback to environment variable
    api_key = os.environ.get('TC_API_KEY')
    if not api_key:
        raise RuntimeError('TC_API_KEY not found in request headers or environment variables.')
    return api_key


@contextmanager
def _open_client() -> TutorCruncherClient:
    client = TutorCruncherClient(api_key=_require_api_key())
    try:
        yield client
    finally:
        client.close()


def _serialize_result(result: Any) -> Any:
    """Serialize SDK results to JSON-compatible types."""
    if hasattr(result, 'to_dict'):
        return result.to_dict(exclude_none=False)
    if isinstance(result, list):
        return [_serialize_result(item) for item in result]
    return result


# Registry for dynamic tools
# Map tool_name -> (resource_name, method_name, method_doc)
TOOL_REGISTRY: Dict[str, Dict[str, Any]] = {}

def _register_tools():
    """Populate the TOOL_REGISTRY with SDK methods."""
    for resource_name, resource_cls in RESOURCE_CLASSES.items():
        for method_name, method in inspect.getmembers(resource_cls):
            if method_name.startswith('_') or method_name == 'metadata':
                continue

            tool_name = f'{resource_name}_{method_name}'
            
            # Inspect signature to build schema (simplified for now)
            # We'll just document it in the description as the SDK is dynamic
            sig = inspect.signature(method)
            doc = inspect.getdoc(method) or f"Call {resource_name}.{method_name}"
            
            TOOL_REGISTRY[tool_name] = {
                'resource': resource_name,
                'method': method_name,
                'doc': doc,
                'signature': sig
            }

_register_tools()


@server.list_tools()
async def handle_list_tools() -> List[Tool]:
    """List available tools."""
    tools = []
    for name, info in TOOL_REGISTRY.items():
        # Construct a simple JSON schema for arguments
        # For now, we'll make it generic since SDK methods are flexible
        # Ideally we would reflect the actual signature
        tools.append(
            Tool(
                name=name,
                description=info['doc'][:100], # Truncate for brevity
                inputSchema={
                    "type": "object",
                    "properties": {
                        "id": {"type": ["string", "integer", "null"]},
                        "params": {"type": "object"},
                        "payload": {"type": "object"},
                        "model": {"type": "string", "description": "Model class name"},
                        "raw": {"type": "boolean"}
                    },
                    "additionalProperties": True
                }
            )
        )
    return tools


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Handle tool execution."""
    if name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: {name}")

    info = TOOL_REGISTRY[name]
    args = arguments or {}
    
    # Extract known args
    id_arg = args.get('id')
    params = args.get('params')
    payload = args.get('payload')
    model_name = args.get('model')
    raw = args.get('raw', False)
    
    # Resolve model
    model_cls = None
    if model_name:
        model_cls = getattr(models, model_name, None)
        if model_cls is None:
            return [TextContent(type="text", text=f"Error: Model '{model_name}' not found")]

    # Prepare kwargs for other arguments
    kwargs = {k: v for k, v in args.items() if k not in ['id', 'params', 'payload', 'model', 'raw']}

    try:
        with _open_client() as client:
            resource = getattr(client, info['resource'])
            method = getattr(resource, info['method'])
            
            result = method(
                id=id_arg,
                params=params,
                payload=payload,
                model=model_cls,
                raw=raw,
                **kwargs
            )
            
            serialized = _serialize_result(result)
            return [TextContent(type="text", text=str(serialized))]
            
    except Exception as e:
        return [TextContent(type="text", text=f"Error executing {name}: {str(e)}")]


@server.list_resources()
async def handle_list_resources() -> List[Resource]:
    return [
        Resource(
            uri=types.AnyUrl("tutorcruncher://schema"),
            name="SDK Schema",
            description="TutorCruncher SDK Schema",
            mimeType="application/json"
        )
    ]


@server.read_resource()
async def handle_read_resource(uri: types.AnyUrl) -> str | bytes:
    if str(uri) == "tutorcruncher://schema":
        return str(spec.get_schema())
    raise ValueError(f"Unknown resource: {uri}")


async def main():
    # Run the server using stdin/stdout
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            types.InitializationOptions(
                server_name="TutorCruncher SDK Server",
                server_version="0.1.0",
                capabilities=types.ServerCapabilities(
                    tools=types.ToolsCapability(listChanged=False),
                    resources=types.ResourcesCapability(subscribe=False, listChanged=False),
                ),
            ),
        )

if __name__ == '__main__':
    asyncio.run(main())
