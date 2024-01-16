from dataclasses import dataclass
from enum import Enum
from typing import List, Literal, Optional, Union
from any_serde.typescript.type_gen import (
    TypescriptTypedefStore,
)
import any_serde.enum
from any_serde.typescript.typescript_utils import TYPESCRIPT_MODULE_DIR


class SampleEnum(str, Enum):
    FIRST = "first value"
    SECOND = "second value"


@any_serde.enum.serialize_by_value
class SampleEnumByValue(int, Enum):
    FIRST_BY_VALUE = 1
    SECOND_BY_VALUE = 10


@dataclass
class SampleDataclass:
    x: float
    y_vec: List[float]
    description: str
    validated: bool
    pathlike: Union[str, List[str]]
    idx: int
    opt: Optional[int]
    enum_value: SampleEnum
    multi_literal: Literal[None, 1, False, "sample value", SampleEnum.FIRST]
    enum_by_value: SampleEnumByValue


def test_dataclass_typedef() -> None:
    typedef_store = TypescriptTypedefStore()
    typedef_store.get_typescript_typedef(
        type_=SampleDataclass,
        name="SampleDataclass",
        filepath=["SampleDataclass.ts"],
    )
    code = typedef_store.get_single_file_code()

    # with (TYPESCRIPT_MODULE_DIR / "tests" / "dataclass_typedef.ts").open("wt") as fout_code:
    #     fout_code.write(code)

    with (TYPESCRIPT_MODULE_DIR / "tests" / "dataclass_typedef.ts").open("rt") as fin_code:
        expected_code = fin_code.read()

    assert code == expected_code
