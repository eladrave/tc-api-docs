from __future__ import annotations

from dataclasses import asdict, dataclass, field, fields, is_dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Iterable, List, Optional, Type, TypeVar, Union, get_args, get_origin

T = TypeVar('T', bound='APIModel')


def _strip_optional(annotation: Any) -> Any:
    origin = get_origin(annotation)
    if origin is Union:
        args = [arg for arg in get_args(annotation) if arg is not type(None)]
        if len(args) == 1:
            return args[0]
    return annotation


def _parse_datetime(value: Any) -> datetime:
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        text = value
    else:
        text = str(value)
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    return datetime.fromisoformat(text)


def _deserialize_value(value: Any, annotation: Any) -> Any:
    if value is None:
        return None
    annotation = _strip_optional(annotation)
    origin = get_origin(annotation)
    if origin in (list, List):
        (item_type,) = get_args(annotation) or (Any,)
        if value is None:
            return []
        return [_deserialize_value(item, item_type) for item in value]
    if origin in (dict, Dict):
        key_type, item_type = get_args(annotation) or (Any, Any)
        return {
            _deserialize_value(key, key_type): _deserialize_value(item, item_type)
            for key, item in (value or {}).items()
        }
    if origin is Union:
        for arg in get_args(annotation):
            if arg is type(None):
                continue
            try:
                return _deserialize_value(value, arg)
            except Exception:
                continue
        return value
    if isinstance(annotation, type) and issubclass(annotation, APIModel):
        if value is None:
            return None
        return annotation.from_dict(value)
    if annotation is Decimal:
        return Decimal(str(value))
    if annotation is datetime:
        return _parse_datetime(value)
    if annotation in (int, float, bool, str):
        return annotation(value)
    return value


def _serialize_value(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, APIModel):
        return value.to_dict()
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, datetime):
        iso = value.isoformat()
        return iso[:-6] + 'Z' if iso.endswith('+00:00') else iso
    if isinstance(value, list):
        return [_serialize_value(item) for item in value]
    if isinstance(value, dict):
        return {key: _serialize_value(item) for key, item in value.items()}
    return value


@dataclass
class APIModel:
    """Base class that powers (de-)serialisation for every data model."""

    def to_dict(self, *, exclude_none: bool = True) -> Dict[str, Any]:
        payload: Dict[str, Any] = {}
        for field_info in fields(self):
            value = getattr(self, field_info.name)
            if exclude_none and value is None:
                continue
            serialized = _serialize_value(value)
            payload[field_info.name] = serialized
        return payload

    @classmethod
    def from_dict(cls: Type[T], data: Optional[Dict[str, Any]]) -> T:
        if not isinstance(data, dict):
            return cls()  # type: ignore[arg-type]
        kwargs = {}
        for field_info in fields(cls):
            kwargs[field_info.name] = _deserialize_value(data.get(field_info.name), field_info.type)
        return cls(**kwargs)


@dataclass
class PaginatedResponse(APIModel):
    """Represents a paginated TutorCruncher response."""

    count: int = 0
    next: Optional[str] = None
    previous: Optional[str] = None
    results: List[Any] = field(default_factory=list)
    extra: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_payload(cls, payload: Dict[str, Any], model: Optional[Type[APIModel]] = None) -> 'PaginatedResponse':
        raw_results = payload.get('results') or []
        if model and issubclass(model, APIModel):
            results = [model.from_dict(item) for item in raw_results]
        else:
            results = raw_results
        extra = {key: value for key, value in payload.items() if key not in {'count', 'next', 'previous', 'results'}}
        return cls(
            count=payload.get('count', len(results)),
            next=payload.get('next'),
            previous=payload.get('previous'),
            results=results,
            extra=extra,
        )


def parse_response(payload: Any, model: Optional[Type[APIModel]]) -> Any:
    if model is None or not isinstance(model, type) or not issubclass(model, APIModel):
        return payload
    if isinstance(payload, dict) and 'results' in payload and isinstance(payload['results'], list):
        return PaginatedResponse.from_payload(payload, model)
    if isinstance(payload, list):
        return [model.from_dict(item) for item in payload]
    if isinstance(payload, dict):
        return model.from_dict(payload)
    return payload


def prepare_payload(data: Any) -> Any:
    if data is None:
        return None
    if isinstance(data, APIModel):
        return data.to_dict()
    if isinstance(data, list):
        return [prepare_payload(item) for item in data]
    if isinstance(data, dict):
        return {key: prepare_payload(value) for key, value in data.items()}
    return data
