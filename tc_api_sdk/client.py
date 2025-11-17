from __future__ import annotations

from typing import Any, Dict, Optional

import requests

from ._version import __version__
from .base import APIModel, parse_response, prepare_payload
from .exceptions import raise_for_status
from .resources import RESOURCE_CLASSES

DEFAULT_BASE_URL = 'https://secure.tutorcruncher.com'


class TutorCruncherClient:
    """High level HTTP client that exposes every TutorCruncher resource."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        session: Optional[requests.Session] = None,
        user_agent: Optional[str] = None,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = session or requests.Session()
        self._default_headers = {
            'Authorization': f'token {api_key}',
            'Accept': 'application/json',
            'User-Agent': user_agent or f'tc-api-sdk/{__version__}',
        }
        self.session.headers.update(self._default_headers)
        self.resources: Dict[str, Any] = {}
        for attr, resource_cls in RESOURCE_CLASSES.items():
            resource = resource_cls(self)
            setattr(self, attr, resource)
            self.resources[attr] = resource

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> 'TutorCruncherClient':
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # noqa: D401
        self.close()

    def _request(
        self,
        *,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        payload: Any = None,
        data: Any = None,
        model: Optional[type[APIModel]] = None,
        raw: bool = False,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **request_kwargs: Any,
    ) -> Any:
        url = f'{self.base_url}{path}'
        request_headers = dict(self.session.headers)
        if headers:
            request_headers.update(headers)
        json_payload = prepare_payload(payload)
        request_data = dict(request_kwargs)
        if json_payload is not None:
            request_data['json'] = json_payload
        if data is not None:
            request_data['data'] = data
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            timeout=timeout or self.timeout,
            headers=request_headers,
            **request_data,
        )
        if raw:
            raise_for_status(response)
            return response
        if not 200 <= response.status_code < 300:
            raise_for_status(response)
        if response.status_code == 204 or not response.content:
            return None
        try:
            payload = response.json()
        except ValueError:
            payload = response.text
        return parse_response(payload, model)
