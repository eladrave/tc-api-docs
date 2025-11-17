from __future__ import annotations

from types import MappingProxyType
from typing import Any, Callable, Dict, Optional

from . import spec


def _slug_to_pascal(value: str) -> str:
    parts = [segment for segment in ''.join(ch if ch.isalnum() else ' ' for ch in value).split(' ') if segment]
    return ''.join(part.capitalize() for part in parts) or 'Resource'


class BaseResource:
    """Shared functionality for every resource wrapper."""

    _resource_spec: Dict[str, Any]

    def __init__(self, client: 'TutorCruncherClient') -> None:
        self._client = client

    @property
    def metadata(self) -> Dict[str, Any]:
        return self._resource_spec


def _build_docstring(resource_spec: Dict[str, Any], op: Dict[str, Any]) -> str:
    doc_lines = [op.get('title') or op.get('id') or 'Endpoint']
    doc_lines.append(f"{op.get('method', 'GET').upper()} {op.get('path')}")
    if resource_spec.get('primary_model'):
        doc_lines.append(f"Suggested model: {resource_spec['primary_model']}")
    if op.get('query_filter_class'):
        doc_lines.append(f"Query parameters dataclass: {op['query_filter_class']}")
    if op.get('description_file'):
        doc_lines.append(f"Docs: {op['description_file']}")
    doc_lines.append('Args: id (path parameter), params (dict), payload (dict/dataclass), model, raw.')
    return '\n'.join(doc_lines)


def _build_operation_method(op: Dict[str, Any], resource_spec: Dict[str, Any]) -> Callable[..., Any]:
    formatted_path = (op.get('path') or '').replace('<id>', '{id}')
    requires_id = '<id>' in (op.get('path') or '')
    method = op.get('method', 'GET').upper()
    doc = _build_docstring(resource_spec, op)

    def operation(
        self,
        *,
        id: Any = None,
        params: Optional[Dict[str, Any]] = None,
        payload: Any = None,
        model: Any = None,
        raw: bool = False,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **request_kwargs: Any,
    ) -> Any:
        path = formatted_path
        if requires_id:
            if id is None:
                raise ValueError('`id` is required for this endpoint.')
            path = formatted_path.format(id=id)
        url_params = params or request_kwargs.pop('query', None)
        body = payload if payload is not None else request_kwargs.pop('json', None)
        data = request_kwargs.pop('data', None)
        return self._client._request(
            method=method,
            path=path,
            params=url_params,
            payload=body,
            data=data,
            model=model,
            raw=raw,
            headers=headers,
            timeout=timeout,
            **request_kwargs,
        )

    operation.__name__ = op.get('operation_id') or 'call'
    operation.__doc__ = doc
    return operation


def build_resource_classes() -> Dict[str, type]:
    classes: Dict[str, type] = {}
    for resource in spec.iter_resources():
        attrs: Dict[str, Any] = {'_resource_spec': resource}
        for op in resource.get('operations', []):
            attrs[op.get('operation_id')] = _build_operation_method(op, resource)
        class_name = f"{_slug_to_pascal(resource['id'])}Resource"
        classes[resource['attribute_name']] = type(class_name, (BaseResource,), attrs)
    return classes


RESOURCE_CLASSES = MappingProxyType(build_resource_classes())
