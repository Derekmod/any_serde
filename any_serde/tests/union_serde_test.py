from dataclasses import dataclass
from typing import Union
from any_serde import union_serde
import any_serde


T1 = union_serde.ExplicitUnion(str, int)
# T1: TypeAlias = str | int
# T2 = union_serde.Boolable[str]
T2 = Union[bool, int]


@dataclass
class ExplicitUnionDataclass:
    x: int
    info: union_serde.ExplicitUnion[str, None]


def get_v2() -> T2:
    return 500


def test_explicit_union() -> None:
    v1_s: T1 = "t1 value"
    d1_s = any_serde.to_data(T1, v1_s)  # type: ignore[arg-type]
    assert d1_s == {
        "type": 0,
        "value": "t1 value",
    }

    # v1_i: T2 = 500
    v2 = get_v2()
    # if asldkfj:
    #     v1_i = True
    d1_i = any_serde.to_data(T2, v2)  # type: ignore[arg-type]
    assert d1_i == {
        "type": 1,
        "value": 500,
    }
