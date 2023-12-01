from dataclasses import dataclass
from typing import Any, List, Tuple
from any_serde import primitives_serde
from any_serde.common import InvalidSerializationException, JSONPrimitive
import pytest


@dataclass
class DummyDataclass:
    x: int


PRIMITIVES: List[Tuple[Any, JSONPrimitive]] = [
    (str, "test_str"),
    (int, 42),
    (float, 3.14),
    (bool, False),
    (None, None),
]
PRIMITIVES_PROD = [
    (expected_type, actual_type, actual_value)
    for actual_type, actual_value in PRIMITIVES
    for expected_type, _ in PRIMITIVES
]


@pytest.mark.parametrize(["expected_type", "actual_type", "actual_value"], PRIMITIVES_PROD)
def test_invalid_serialization(expected_type: Any, actual_type: Any, actual_value: JSONPrimitive) -> None:
    with pytest.raises(InvalidSerializationException):
        primitives_serde.to_data(expected_type, DummyDataclass(2))

    if actual_type is expected_type:
        primitives_serde.to_data(expected_type, actual_value)
    else:
        with pytest.raises(InvalidSerializationException):
            primitives_serde.to_data(expected_type, actual_value)
