from dataclasses import dataclass

from any_serde import dataclass_serde
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
