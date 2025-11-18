"""MCP server exposing TutorCruncher SDK functionality."""
from __future__ import annotations

import os
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import parse_qsl, urlparse

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tc_api_sdk import (  # noqa: E402
    AppointmentsAppointmentObject,
    ClientsClientObjectVersion2,
    TutorCruncherClient,
    spec,
)

mcp = FastMCP('TutorCruncher SDK Server')


def _require_api_key() -> str:
    api_key = os.environ.get('TC_API_KEY')
    if not api_key:
        raise RuntimeError('Set the TC_API_KEY environment variable before starting the MCP server.')
    return api_key


@contextmanager
def _open_client() -> TutorCruncherClient:
    client = TutorCruncherClient(api_key=_require_api_key())
    try:
        yield client
    finally:
        client.close()


def _serialize_models(items) -> List[Dict]:
    return [item.to_dict(exclude_none=False) if hasattr(item, 'to_dict') else item for item in items]


@mcp.tool()
def list_clients(status: Optional[str] = None, limit: int = 10) -> Dict:
    """Return a single page of clients optionally filtered by status (prospect/live/dormant)."""
    params: Dict[str, str | int] = {'limit': limit}
    if status:
        params['status'] = status
    with _open_client() as client:
        response = client.clients.list_all_clients(
            params=params,
            model=ClientsClientObjectVersion2,
        )
    return {
        'count': response.count,
        'next': response.next,
        'results': _serialize_models(response.results),
    }


@mcp.tool()
def get_client_details(client_id: int) -> Dict:
    """Fetch a single client by ID."""
    with _open_client() as client:
        result = client.clients.get_a_client(
            id=client_id,
            model=ClientsClientObjectVersion2,
        )
    if result is None:
        return {'error': f'Client {client_id} not found'}
    return result.to_dict(exclude_none=False)


@mcp.tool()
def list_appointments(status: str = 'planned', limit: int = 5) -> Dict:
    """Return recent appointments filtered by status (planned/complete/etc)."""
    params: Dict[str, str | int] = {'limit': limit}
    if status:
        params['status'] = status
    with _open_client() as client:
        response = client.appointments.list_all_appointments(
            params=params,
            model=AppointmentsAppointmentObject,
        )
    return {
        'count': response.count,
        'next': response.next,
        'results': _serialize_models(response.results),
    }


@mcp.tool()
def paginate_prospect_clients(limit: int = 25, pages: int = 2) -> Dict:
    """Collect multiple pages of prospect clients to demonstrate pagination."""
    params: Dict[str, str | int] = {'limit': limit, 'status': 'prospect'}
    collected: List[Dict] = []
    page_count = 0
    with _open_client() as client:
        while page_count < pages:
            response = client.clients.list_all_clients(
                params=params,
                model=ClientsClientObjectVersion2,
            )
            collected.extend(_serialize_models(response.results))
            page_count += 1
            if not response.next:
                break
            next_query = dict(parse_qsl(urlparse(response.next).query))
            params = {
                'limit': int(next_query.get('limit', limit)),
                'offset': int(next_query.get('offset', params.get('offset', 0))),
                'status': next_query.get('status', 'prospect'),
            }
    return {'pages_collected': page_count, 'results': collected}


@mcp.resource('tutorcruncher://schema')
def get_schema() -> Dict:
    """Expose the TutorCruncher SDK schema description."""
    return spec.get_schema()


if __name__ == '__main__':
    mcp.run(transport='stdio')
