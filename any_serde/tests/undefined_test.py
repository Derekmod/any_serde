from dataclasses import dataclass, field
from typing import Union

import any_serde


@dataclass
class MigrationType1:
    x: int
    why: Union[str, any_serde.Undefined] = field(default_factory=any_serde.Undefined)
    y: Union[int, any_serde.Undefined] = field(default_factory=any_serde.Undefined)


def test_migration_type_1() -> None:
    initial_value = MigrationType1(
        x=2,
        why="whoops",
    )
    initial_data = any_serde.to_data(MigrationType1, initial_value)
    assert initial_data == {
        "x": 2,
        "why": "whoops",
    }
    rt_value = any_serde.from_data(MigrationType1, initial_data)
    assert rt_value == initial_value
    rt_value.why = any_serde.Undefined()
    rt_value.y = 4
    migration_data = any_serde.to_data(MigrationType1, rt_value)
    assert migration_data == {
        "x": 2,
        "y": 4,
    }
    rt_migration_value = any_serde.from_data(MigrationType1, migration_data)
    assert rt_migration_value == rt_value
