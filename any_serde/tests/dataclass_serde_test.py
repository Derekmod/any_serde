from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
import pytest

from any_serde import InvalidDeserializationException, dataclass_serde
from any_serde.common import JSON


@dataclass
class BasicDataclass:
    name: str
    value: int


def test_basic_dataclass() -> None:
    expected_object = BasicDataclass(name="test", value=9001)
    expected_data: JSON = {
        "name": "test",
        "value": 9001,
    }

    assert dataclass_serde.to_data(BasicDataclass, expected_object) == expected_data
    assert dataclass_serde.from_data(BasicDataclass, expected_data) == expected_object


@dataclass
class RemappedDataclass:
    my_name: str
    some_weird_key: str


dataclass_serde.register_serialization_renames(
    serialization_renames={
        "my_name": "myName",
        "some_weird_key": "see this key is allowed to have spaces",
    },
    type_=RemappedDataclass,
)


def test_remapped_dataclass() -> None:
    expected_object = RemappedDataclass(
        my_name="test name",
        some_weird_key="scooby",
    )
    expected_data: JSON = {
        "myName": "test name",
        "see this key is allowed to have spaces": "scooby",
    }

    assert dataclass_serde.to_data(RemappedDataclass, expected_object) == expected_data
    assert dataclass_serde.from_data(RemappedDataclass, expected_data) == expected_object


@dataclass
class RecursiveDataclass:
    name: str
    children: list[RecursiveDataclass]


def test_recursive_dataclass() -> None:
    expected_object = RecursiveDataclass(
        name="root",
        children=[
            RecursiveDataclass(
                name="brother",
                children=[],
            ),
            RecursiveDataclass(
                name="sister",
                children=[
                    RecursiveDataclass(
                        name="granddaughter",
                        children=[],
                    ),
                ],
            ),
        ],
    )
    expected_data: JSON = {
        "name": "root",
        "children": [
            {
                "name": "brother",
                "children": [],
            },
            {
                "name": "sister",
                "children": [
                    {
                        "name": "granddaughter",
                        "children": [],
                    }
                ],
            },
        ],
    }

    assert dataclass_serde.to_data(RecursiveDataclass, expected_object) == expected_data
    assert dataclass_serde.from_data(RecursiveDataclass, expected_data) == expected_object


def test_unknown_data_keys_fails() -> None:
    with pytest.raises(InvalidDeserializationException):
        dataclass_serde.from_data(
            BasicDataclass,
            {
                "name": "test name",
                "value": 0,
                "extra_key": True,
            },
        )


@dataclass
class BasicDataclassAllowUnknown:
    name: str
    value: int


dataclass_serde.allow_unknown_data_keys(BasicDataclassAllowUnknown, roundtrip=False)


def test_unknown_data_keys() -> None:
    data: Dict[str, JSON] = {
        "name": "test name",
        "value": 0,
        "extra_key": True,
    }
    expected_obj = BasicDataclassAllowUnknown(
        name="test name",
        value=0,
    )
    expected_roundtrip_data = {
        "name": "test name",
        "value": 0,
    }
    deserde_obj = dataclass_serde.from_data(BasicDataclassAllowUnknown, data)

    assert deserde_obj == expected_obj
    assert dataclass_serde.to_data(BasicDataclassAllowUnknown, expected_obj) == expected_roundtrip_data
    assert not hasattr(deserde_obj, dataclass_serde.ATTR_INJECTED_DATA)
    assert dataclass_serde.to_data(BasicDataclassAllowUnknown, deserde_obj) == expected_roundtrip_data


@dataclass
class BasicDataclassAllowUnknownRoundtrip:
    name: str
    value: int


dataclass_serde.allow_unknown_data_keys(BasicDataclassAllowUnknownRoundtrip, roundtrip=True)


def test_unknown_data_keys_roundtrip() -> None:
    data: Dict[str, JSON] = {
        "name": "test name",
        "value": 0,
        "extra_key": True,
    }
    expected_obj = BasicDataclassAllowUnknownRoundtrip(
        name="test name",
        value=0,
    )
    expected_roundtrip_data = data
    deserde_obj = dataclass_serde.from_data(BasicDataclassAllowUnknownRoundtrip, data)

    assert deserde_obj == expected_obj
    assert dataclass_serde.to_data(BasicDataclassAllowUnknownRoundtrip, expected_obj) != expected_roundtrip_data
    assert dataclass_serde.to_data(BasicDataclassAllowUnknownRoundtrip, deserde_obj) == expected_roundtrip_data
