from dataclasses import dataclass
from typing import List, Union
from any_serde.typescript.type_gen import (
    TypescriptTypedefStore,
)
from any_serde.typescript.typescript_utils import TYPESCRIPT_MODULE_DIR


@dataclass
class TestDataclass:
    x: float
    y_vec: List[float]
    description: str
    validated: bool
    pathlike: Union[str, List[str]]


def test_dataclass_typedef() -> None:
    typedef_store = TypescriptTypedefStore()
    typedef_store.get_typescript_typedef(
        type_=TestDataclass,
        name="TestDataclass",
        filepath=["TestDataclass.ts"],
    )
    code = typedef_store.get_single_file_code()

    with (TYPESCRIPT_MODULE_DIR / "tests" / "dataclass_typedef.ts").open("rt") as fin_code:
        expected_code = fin_code.read()

    assert code == expected_code
