from __future__ import annotations

import json
from importlib import resources
from typing import Any, Dict, Iterator, List

SCHEMA_RESOURCE = 'tc_api_sdk.generated.api_schema.json'


def _load_schema() -> Dict[str, Any]:
    with resources.files('tc_api_sdk.generated').joinpath('api_schema.json').open('r') as fp:
        return json.load(fp)


SCHEMA = _load_schema()
RESOURCES: List[Dict[str, Any]] = SCHEMA.get('resources', [])
RESOURCE_BY_ATTR = {entry['attribute_name']: entry for entry in RESOURCES}


def iter_resources() -> Iterator[Dict[str, Any]]:
    return iter(RESOURCES)


def get_resource(attr_name: str) -> Dict[str, Any]:
    return RESOURCE_BY_ATTR[attr_name]


def get_schema() -> Dict[str, Any]:
    """Return a copy of the loaded schema."""
    return json.loads(json.dumps(SCHEMA))
