#!/usr/bin/env python3
"""Parse the TutorCruncher API docs and emit structured schema + dataclasses.

The generated artefacts live inside `tc_api_sdk/`:
* `generated/api_schema.json` - serialisable description of resources/endpoints.
* `models.py` - strongly typed dataclasses for every documented object and filter.
"""
from __future__ import annotations

import argparse
import json
import keyword
import re
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

import yaml

ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / 'pages'
OUTPUT_DIR = ROOT / 'tc_api_sdk' / 'generated'
SCHEMA_PATH = OUTPUT_DIR / 'api_schema.json'
MODELS_PATH = ROOT / 'tc_api_sdk' / 'models.py'


TYPE_MAPPING = {
    'string': 'str',
    'integer': 'int',
    'decimal': 'Decimal',
    'float': 'float',
    'boolean': 'bool',
    'bool': 'bool',
    'datetime': 'datetime',
}


@dataclass
class FieldDefinition:
    name: str
    type_hint: str
    description: str
    default: str | None = None
    default_factory: str | None = None


@dataclass
class ModelDefinition:
    name: str
    docstring: str
    fields: List[FieldDefinition]


def slug_to_snake(value: str) -> str:
    value = value.replace('-', '_')
    value = re.sub(r'[^0-9a-zA-Z_]', '_', value)
    value = re.sub(r'_+', '_', value).strip('_')
    if not value:
        value = 'section'
    if keyword.iskeyword(value):
        value += '_'
    return value


def slug_to_pascal(value: str) -> str:
    parts = re.findall(r'[0-9a-zA-Z]+', value)
    if not parts:
        return 'Item'
    return ''.join(word.capitalize() for word in parts)


def make_class_name(resource_id: str, title: str, *, suffix: str = '') -> str:
    name = slug_to_pascal(resource_id) + slug_to_pascal(title) + suffix
    return re.sub(r'_{2,}', '_', name)


def read_yaml(path: Path) -> Dict[str, Any]:
    with path.open() as fp:
        return yaml.safe_load(fp) or {}


def ensure_output_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MODELS_PATH.parent.mkdir(parents=True, exist_ok=True)


def load_api_index() -> Dict[str, Any]:
    return read_yaml(PAGES_DIR / 'api.yml')


def normalise_path(value: str) -> Path:
    value = value.lstrip('/')
    return Path('pages') / value


def build_field(
    model_name: str,
    attr: Dict[str, Any],
    *,
    nested_suffix: str = '',
) -> Tuple[FieldDefinition, List[ModelDefinition]]:
    nested_models: List[ModelDefinition] = []
    attr_type = attr.get('type', 'string')
    field_name = slug_to_snake(attr['name'])
    description = (attr.get('description') or '').strip().replace('\n', ' ')

    if attr_type == 'array':
        if attr.get('children'):
            child_model_name = f'{model_name}{slug_to_pascal(attr["name"])}Item'
            nested_models.extend(build_model(child_model_name, attr['children']))
            type_hint = f'List[{child_model_name}]'
        else:
            type_hint = 'List[Any]'
        field_def = FieldDefinition(
            name=field_name,
            type_hint=type_hint,
            description=description,
            default_factory='list',
        )
        return field_def, nested_models

    if attr_type == 'object':
        if attr.get('children'):
            child_model_name = f'{model_name}{slug_to_pascal(attr["name"])}'
            nested_models.extend(build_model(child_model_name, attr['children']))
            type_hint = f'Optional[{child_model_name}]'
        else:
            type_hint = 'Optional[Dict[str, Any]]'
        field_def = FieldDefinition(
            name=field_name,
            type_hint=type_hint,
            description=description,
            default='None',
        )
        return field_def, nested_models

    py_type = TYPE_MAPPING.get(attr_type, 'Any')
    type_hint = f'Optional[{py_type}]'
    field_def = FieldDefinition(
        name=field_name,
        type_hint=type_hint,
        description=description,
        default='None',
    )
    return field_def, nested_models


def build_model(name: str, attributes: Sequence[Dict[str, Any]]) -> List[ModelDefinition]:
    fields: List[FieldDefinition] = []
    nested_models: List[ModelDefinition] = []
    for attr in attributes:
        field_def, child_models = build_field(name, attr)
        fields.append(field_def)
        nested_models.extend(child_models)
    doc = f'Auto-generated model for {name}.'
    current = ModelDefinition(name=name, docstring=doc, fields=fields)
    return [current, *nested_models]


def build_filter_model(name: str, filters: Sequence[Dict[str, Any]]) -> ModelDefinition:
    fields: List[FieldDefinition] = []
    for entry in filters:
        field_name = slug_to_snake(entry['name'])
        description = (entry.get('description') or '').strip().replace('\n', ' ')
        py_type = TYPE_MAPPING.get(entry.get('type', 'string'), 'Any')
        fields.append(
            FieldDefinition(
                name=field_name,
                type_hint=f'Optional[{py_type}]',
                description=description,
                default='None',
            )
        )
    doc = f'Filter parameters for {name}.'
    return ModelDefinition(name=name, docstring=doc, fields=fields)


def format_docstring(text: str) -> str:
    if not text:
        return 'pass'
    cleaned = textwrap.indent(textwrap.dedent(text).strip(), '    ')
    return cleaned


def write_models_file(model_defs: Iterable[ModelDefinition]) -> None:
    header = """\"\"\"Auto-generated data models for the TutorCruncher API.\"\"\"
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional

from .base import APIModel

"""
    lines = [header]
    names: List[str] = []
    for model in model_defs:
        names.append(model.name)
        lines.append(f'@dataclass\nclass {model.name}(APIModel):')
        if not model.fields:
            lines.append('    pass\n')
            continue
        lines.append(f'    """{model.docstring}"""')
        for field_def in model.fields:
            if field_def.default_factory:
                default = f' = field(default_factory={field_def.default_factory})'
            elif field_def.default is not None:
                default = f' = {field_def.default}'
            else:
                default = ''
            comment = f'  # {field_def.description}' if field_def.description else ''
            lines.append(f'    {field_def.name}: {field_def.type_hint}{default}{comment}')
        lines.append('')
    lines.append(f'__all__ = {names!r}\n')
    MODELS_PATH.write_text('\n'.join(lines))


def build_schema() -> Dict[str, Any]:
    api_index = load_api_index()
    resources: List[Dict[str, Any]] = []
    model_defs: List[ModelDefinition] = []
    filter_defs: Dict[str, ModelDefinition] = {}

    for section in api_index.get('endpoint_sections', []):
        layout_path = ROOT / normalise_path(section['layout'])
        layout = read_yaml(layout_path)
        resource_id = section['id']
        attr_name = slug_to_snake(resource_id)
        resource_entry: Dict[str, Any] = {
            'id': resource_id,
            'title': section['title'],
            'attribute_name': attr_name,
            'layout': str(layout_path.relative_to(ROOT)),
            'models': [],
            'operations': [],
        }
        for item in layout.get('sections', []):
            if 'attributes' in item:
                attr_file = ROOT / normalise_path(item['attributes'])
                attr_data = read_yaml(attr_file)
                model_name = make_class_name(resource_id, item['title'])
                model_entry = {
                    'id': item.get('id'),
                    'title': item.get('title'),
                    'name': model_name,
                    'attributes_file': str(attr_file.relative_to(ROOT)),
                    'attributes': attr_data.get('attributes', []),
                    'filters': attr_data.get('filters', []),
                    'description': item.get('description'),
                }
                resource_entry['models'].append(model_entry)
                model_defs.extend(build_model(model_name, model_entry['attributes']))

                if model_entry['filters']:
                    filter_name = model_name + 'Filters'
                    if filter_name not in filter_defs:
                        filter_defs[filter_name] = build_filter_model(filter_name, model_entry['filters'])
                    model_entry['filter_class'] = filter_name
            elif 'code_type' in item:
                description = item.get('description')
                desc_path = ROOT / normalise_path(description) if description else None
                response_path = item.get('response')
                code_path = item.get('code')
                filters_path = item.get('filters')
                filter_name = None
                if filters_path:
                    attrs_file = str((ROOT / normalise_path(filters_path)).relative_to(ROOT))
                    for model in resource_entry['models']:
                        if model['attributes_file'] == attrs_file:
                            filter_name = model.get('filter_class')
                            break
                op_entry = {
                    'id': item.get('id'),
                    'title': item.get('title'),
                    'operation_id': slug_to_snake(item.get('id') or item.get('title')),
                    'method': item.get('code_type'),
                    'path': item.get('code_url'),
                    'description_file': str(desc_path.relative_to(ROOT)) if desc_path else None,
                    'code_example': str((ROOT / normalise_path(code_path)).relative_to(ROOT)) if code_path else None,
                    'response_example': str((ROOT / normalise_path(response_path)).relative_to(ROOT)) if response_path else None,
                    'query_filter_class': filter_name,
                }
                resource_entry['operations'].append(op_entry)
        if resource_entry['models']:
            resource_entry['primary_model'] = resource_entry['models'][-1]['name']
        resources.append(resource_entry)

    schema = {'resources': resources}
    ensure_output_dirs()
    SCHEMA_PATH.write_text(json.dumps(schema, indent=2))
    write_models_file([*model_defs, *filter_defs.values()])
    return schema


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate SDK schema and models.')
    parser.parse_args()
    build_schema()
    print(f'Wrote schema to {SCHEMA_PATH}')
    print(f'Wrote models to {MODELS_PATH}')


if __name__ == '__main__':
    main()
