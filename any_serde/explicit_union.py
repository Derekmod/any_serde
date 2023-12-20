from typing import (
    Any,
    Type,
    TypeVar,
    Union,
    overload,
)


class _MissingType:
    ...


_MISSING = _MissingType()


T_Any = TypeVar("T_Any")
T_Any1 = TypeVar("T_Any1")
T_Any2 = TypeVar("T_Any2")
T_Any3 = TypeVar("T_Any3")
T_Any4 = TypeVar("T_Any4")
T_Any5 = TypeVar("T_Any5")
T_Any6 = TypeVar("T_Any6")
T_Any7 = TypeVar("T_Any7")
T_Any8 = TypeVar("T_Any8")
T_Any9 = TypeVar("T_Any9")
T_Any10 = TypeVar("T_Any10")


class _ExplicitUnionType:
    def __init__(self, *union_types: T_Any) -> None:
        pass


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
) -> Type[Union[T_Any1, T_Any2,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
) -> Type[Union[T_Any1, T_Any2, T_Any3,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
    union_type4: Type[T_Any4],
) -> Type[Union[T_Any1, T_Any2, T_Any3, T_Any4,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
    union_type4: Type[T_Any4],
    union_type5: Type[T_Any5],
) -> Type[Union[T_Any1, T_Any2, T_Any3, T_Any4, T_Any5,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
    union_type4: Type[T_Any4],
    union_type5: Type[T_Any5],
    union_type6: Type[T_Any6],
) -> Type[Union[T_Any1, T_Any2, T_Any3, T_Any4, T_Any5, T_Any6,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
    union_type4: Type[T_Any4],
    union_type5: Type[T_Any5],
    union_type6: Type[T_Any6],
    union_type7: Type[T_Any7],
) -> Type[Union[T_Any1, T_Any2, T_Any3, T_Any4, T_Any5, T_Any6, T_Any7,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
    union_type4: Type[T_Any4],
    union_type5: Type[T_Any5],
    union_type6: Type[T_Any6],
    union_type7: Type[T_Any7],
    union_type8: Type[T_Any8],
) -> Type[Union[T_Any1, T_Any2, T_Any3, T_Any4, T_Any5, T_Any6, T_Any7, T_Any8,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
    union_type4: Type[T_Any4],
    union_type5: Type[T_Any5],
    union_type6: Type[T_Any6],
    union_type7: Type[T_Any7],
    union_type8: Type[T_Any8],
    union_type9: Type[T_Any9],
) -> Type[Union[T_Any1, T_Any2, T_Any3, T_Any4, T_Any5, T_Any6, T_Any7, T_Any8, T_Any9,]]:
    ...


@overload
def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Type[T_Any3],
    union_type4: Type[T_Any4],
    union_type5: Type[T_Any5],
    union_type6: Type[T_Any6],
    union_type7: Type[T_Any7],
    union_type8: Type[T_Any8],
    union_type9: Type[T_Any9],
    union_type10: Type[T_Any10],
) -> Type[Union[T_Any1, T_Any2, T_Any3, T_Any4, T_Any5, T_Any6, T_Any7, T_Any8, T_Any9, T_Any10,]]:
    ...


def ExplicitUnion(
    union_type1: Type[T_Any1],
    union_type2: Type[T_Any2],
    union_type3: Union[Type[T_Any3], _MissingType] = _MISSING,
    union_type4: Union[Type[T_Any4], _MissingType] = _MISSING,
    union_type5: Union[Type[T_Any5], _MissingType] = _MISSING,
    union_type6: Union[Type[T_Any6], _MissingType] = _MISSING,
    union_type7: Union[Type[T_Any7], _MissingType] = _MISSING,
    union_type8: Union[Type[T_Any8], _MissingType] = _MISSING,
    union_type9: Union[Type[T_Any9], _MissingType] = _MISSING,
    union_type10: Union[Type[T_Any10], _MissingType] = _MISSING,
) -> Type[Any]:
    if not isinstance(union_type10, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
            union_type4,
            union_type5,
            union_type6,
            union_type7,
            union_type8,
            union_type9,
            union_type10,
        )
    if not isinstance(union_type9, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
            union_type4,
            union_type5,
            union_type6,
            union_type7,
            union_type8,
            union_type9,
        )
    if not isinstance(union_type8, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
            union_type4,
            union_type5,
            union_type6,
            union_type7,
            union_type8,
        )
    if not isinstance(union_type7, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
            union_type4,
            union_type5,
            union_type6,
            union_type7,
        )
    if not isinstance(union_type6, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
            union_type4,
            union_type5,
            union_type6,
        )
    if not isinstance(union_type5, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
            union_type4,
            union_type5,
        )
    if not isinstance(union_type4, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
            union_type4,
        )
    if not isinstance(union_type3, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
            union_type3,
        )
    if not isinstance(union_type2, _MissingType):
        return _ExplicitUnionType(  # type: ignore[return-value]
            union_type1,
            union_type2,
        )
