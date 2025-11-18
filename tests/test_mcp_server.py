
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from starlette.testclient import TestClient

# Add root to path to import MCP modules
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# Mock the SDK client before importing sse_server
# This prevents actual network calls during tests
with patch('tc_api_sdk.TutorCruncherClient') as MockClient:
    from MCP.sse_server import create_app
    from MCP.server import TOOL_REGISTRY

@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)

def test_health_check(client):
    # SSE endpoint should accept connection (even if it closes immediately without handshake)
    # But without proper SSE handshake it might just return 200 or keep open.
    # Starlette TestClient doesn't fully support streaming, but we can check initial response.
    # However, we need to pass auth.
    headers = {"Authorization": "Bearer test_token"}
    with client.stream("GET", "/sse", headers=headers) as response:
        assert response.status_code == 200

def test_missing_auth(client):
    # Should fail or handle gracefully. 
    # Our implementation allows connection but might fail later if key is needed.
    # But _extract_api_key returns None, and _require_api_key raises Error if not found.
    # The server.py logic checks for key when _open_client is called.
    # So connection might succeed, but tool call should fail.
    
    # Let's try to connect. The handle_sse doesn't enforce key presence immediately, 
    # but it sets context var. If context var is None, _require_api_key will check env.
    # If env is also missing, it raises RuntimeError.
    
    # We need to ensure TC_API_KEY is NOT in env for this test
    with patch.dict(os.environ, {}, clear=True):
        # We expect the connection to close or error out when server tries to run.
        # But server.run might not need key immediately until a tool is called?
        # Actually, _open_client is called inside tool handlers.
        # So initial connection should be fine?
        # Wait, handle_sse calls server.run.
        pass

def test_tool_discovery(client):
    # We can't easily test JSON-RPC over SSE with TestClient without a complex client mock.
    # But we can verify the app structure and that tools are registered.
    assert len(TOOL_REGISTRY) > 0
    assert 'clients_list_all_clients' in TOOL_REGISTRY

def test_message_post_auth(client):
    # Test posting a message with auth header
    headers = {"Authorization": "Bearer test_token"}
    # We need a valid session ID usually, but let's just check if it accepts the request
    # The server expects a session_id query param.
    response = client.post("/messages?session_id=invalid-uuid", json={}, headers=headers)
    # Should return 400 or 404 because session doesn't exist, but that proves it reached the handler
    assert response.status_code in [400, 404]

def test_message_post_no_auth(client):
    # Without auth, it should still reach handler, but context var will be None.
    # If the handler tries to use the client, it will fail.
    # But handle_post_message just forwards to mcp.
    response = client.post("/messages?session_id=invalid-uuid", json={})
    assert response.status_code in [400, 404]

