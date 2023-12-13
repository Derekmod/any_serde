from dataclasses import dataclass
from typing import List
from any_serde.typescript.type_gen import (
    TypescriptTypedefStore,
)


@dataclass
class TestDataclass:
    x: float
    y_vec: List[float]
    description: str
    validated: bool


def test_dataclass_typedef() -> None:
    typedef_store = TypescriptTypedefStore()
    typedef_store.get_typescript_typedef(
        type_=TestDataclass,
        name="TestDataclass",
        filepath=["TestDataclass.ts"],
    )
    for tdef in typedef_store.typedefs:
        print(tdef.code)
        print()
