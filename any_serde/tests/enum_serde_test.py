import enum
from typing import Union
import pytest
from any_serde import from_data, to_data
import any_serde.enum
from any_serde.common import InvalidDeserializationException


class UnspecifiedSimpleEnum(enum.Enum):
    KEY1 = "x"
    KEY2 = "y"


@any_serde.enum.serialize_by_value
class UnspecifiedSimpleEnumByValue(enum.Enum):
    KEY1 = "x"
    KEY2 = "y"


def test_unspecified_enum() -> None:
    assert to_data(UnspecifiedSimpleEnum, UnspecifiedSimpleEnum.KEY1) == "UnspecifiedSimpleEnum.KEY1"
    assert to_data(UnspecifiedSimpleEnumByValue, UnspecifiedSimpleEnum.KEY1) == "x"

    assert to_data(UnspecifiedSimpleEnum, UnspecifiedSimpleEnum.KEY2) == "UnspecifiedSimpleEnum.KEY2"
    assert to_data(UnspecifiedSimpleEnumByValue, UnspecifiedSimpleEnum.KEY2) == "y"

    assert to_data(UnspecifiedSimpleEnum, UnspecifiedSimpleEnumByValue.KEY1) == "UnspecifiedSimpleEnum.KEY1"
    assert to_data(UnspecifiedSimpleEnumByValue, UnspecifiedSimpleEnumByValue.KEY1) == "x"

    assert to_data(UnspecifiedSimpleEnum, UnspecifiedSimpleEnumByValue.KEY2) == "UnspecifiedSimpleEnum.KEY2"
    assert to_data(UnspecifiedSimpleEnumByValue, UnspecifiedSimpleEnumByValue.KEY2) == "y"

    with pytest.raises(InvalidDeserializationException):
        from_data(UnspecifiedSimpleEnum, "x")

    assert from_data(UnspecifiedSimpleEnum, "UnspecifiedSimpleEnum.KEY1") == UnspecifiedSimpleEnum.KEY1

    with pytest.raises(InvalidDeserializationException):
        from_data(UnspecifiedSimpleEnumByValue, "UnspecifiedSimpleEnum.KEY1")

    assert from_data(UnspecifiedSimpleEnumByValue, "y") == UnspecifiedSimpleEnumByValue.KEY2


def test_str_fallback() -> None:
    expected_obj1 = UnspecifiedSimpleEnumByValue.KEY1
    expected_data1 = "x"
    assert (
        to_data(
            Union[UnspecifiedSimpleEnumByValue, str],  # type: ignore[arg-type]
            expected_obj1,
        )
        == expected_data1
    )
    assert (
        from_data(
            Union[UnspecifiedSimpleEnumByValue, str],  # type: ignore[arg-type]
            expected_data1,
        )
        == expected_obj1
    )

    expected_obj2 = "other value"
    expected_data2 = "other value"
    assert (
        to_data(
            Union[UnspecifiedSimpleEnumByValue, str],  # type: ignore[arg-type]
            expected_obj2,
        )
        == expected_data2
    )
    assert (
        from_data(
            Union[UnspecifiedSimpleEnumByValue, str],  # type: ignore[arg-type]
            expected_data2,
        )
        == expected_obj2
    )

    assert from_data(Union[str, UnspecifiedSimpleEnumByValue], "x") == "x"  # type: ignore[arg-type]
