""" A Serializable Dataclass Implementation """
from __future__ import annotations

import dataclasses
from functools import lru_cache
import functools
from typing import Any, Dict, Type, TypeVar, get_type_hints
from any_serde.common import (
    JSON,
    InvalidDeserializationException,
)


ATTR_SERIALIZATION_RENAMES = "__serialization_renames__"


T_Dataclass = TypeVar("T_Dataclass")


def is_dataclass_type(typ: Any) -> bool:
    return isinstance(typ, type) and dataclasses.is_dataclass(typ)


@lru_cache(maxsize=None)
def _get_type_hints(typ: Type[object]) -> Dict[str, Type[Any]]:
    return get_type_hints(typ)


def _field_is_required(field: dataclasses.Field) -> bool:
    if not isinstance(field.default, dataclasses._MISSING_TYPE):
        return False

    if not isinstance(field.default_factory, dataclasses._MISSING_TYPE):
        return False

    return True


@functools.lru_cache(None)
def _get_serialization_renames(dataclass_type: Type[object]) -> Dict[str, str]:
    error_msg_start = f"Illegal {ATTR_SERIALIZATION_RENAMES} value for {dataclass_type}!"

    serialization_renames = getattr(dataclass_type, ATTR_SERIALIZATION_RENAMES)
    if serialization_renames is None:
        return {}

    if not isinstance(serialization_renames, dict):
        raise AssertionError(f"{error_msg_start} Not a dictionary!")

    for attribute_key, data_key in serialization_renames.items():
        if not isinstance(attribute_key, str) or not isinstance(data_key, str):
            raise AssertionError(f"{error_msg_start} Found non-string values!")

    attribute_keys = set(serialization_renames)
    data_keys = set(serialization_renames.values())
    if len(data_keys) < len(attribute_keys):
        raise AssertionError(f"{error_msg_start} Duplicate data keys!")

    dataclass_field_names = {field.name for field in dataclasses.fields(dataclass_type)}  # type: ignore[arg-type]
    if attribute_keys - dataclass_field_names:
        raise AssertionError(f"{error_msg_start} Mapping attributes that don't exist!")

    unmapped_attribute_keys = dataclass_field_names - attribute_keys
    if unmapped_attribute_keys & data_keys:
        raise AssertionError(f"{error_msg_start} Data keys conflict with existing fields!")

    return serialization_renames


def from_data(type_: Type[T_Dataclass], data: JSON) -> T_Dataclass:
    if not isinstance(data, dict):
        raise InvalidDeserializationException(f"Dataclasses serialize to dict. Got {type(data)} instead!")

    assert is_dataclass_type(type_), "Can only call dataclass_serde.from_data on dataclass types!"

    field_types = _get_type_hints(type_)  # type: ignore
    dataclass_fields = {x.name: x for x in dataclasses.fields(type_)}  # type: ignore

    fields_without_types = set(dataclass_fields) - set(field_types)
    assert not fields_without_types, f"Fields without types: {fields_without_types}"

    data_without_fields = set(data) - set(dataclass_fields)
    assert not data_without_fields, f"Data keys without fields: {data_without_fields}"

    required_field_names = [field_name for field_name, field in dataclass_fields.items() if _field_is_required(field)]

    missing_required_fields = set(required_field_names) - set(data)
    if missing_required_fields:
        raise InvalidDeserializationException(f"Data is missing required fields: {missing_required_fields}")

    serialization_renames = _get_serialization_renames(type_)  # type: ignore[arg-type]
    deserialization_renames = {data_key: attribute_key for attribute_key, data_key in serialization_renames.items()}

    from any_serde import serde

    casted_data = {
        deserialization_renames.get(field_name, field_name): serde.from_data(field_types[field_name], field_data)
        for field_name, field_data in data.items()
    }

    return type_(**casted_data)


def to_data(item: object) -> JSON:
    type_ = type(item)

    assert is_dataclass_type(type_), "Can only call dataclass_serde.to_data on dataclass instances!"

    field_types = _get_type_hints(type_)  # type: ignore
    dataclass_fields = {x.name: x for x in dataclasses.fields(type_)}  # type: ignore

    fields_without_types = set(dataclass_fields) - set(field_types)
    assert not fields_without_types, f"Fields without types: {fields_without_types}"

    serialization_renames = _get_serialization_renames(type_)  # type: ignore[arg-type]

    from any_serde import serde

    return {
        serialization_renames.get(field_name, field_name): serde.to_data(
            field_types[field_name], getattr(item, field_name)
        )
        for field_name in dataclass_fields
    }
