from dataclasses import dataclass

from any_serde.common import JSON
from any_serde.serde import from_data, to_data
from any_serde import dataclass_serde


def test_int_serde() -> None:
    data: JSON = 2
    obj = from_data(JSON, data)
    assert obj == data


@dataclass
class JSONDataclass:
    x: JSON


def test_dataclass_json() -> None:
    x = {
        "a": [1, "2", False],
        "b": None,
    }
    obj = JSONDataclass(x=x)
    data = dataclass_serde.to_data(JSONDataclass, obj)
    deser_obj = dataclass_serde.from_data(JSONDataclass, data)

    assert deser_obj == obj


def test_json_big() -> None:
    data = [
        "abc",
        {
            "2": 123,
            "def": False,
            "key": {
                "key2": 9001,
                "test": [True, None, 456, "789"],
            },
        },
    ]
    obj = from_data(JSON, data)
    assert obj == data
    roundtrip = to_data(JSON, obj)
    assert roundtrip == data
