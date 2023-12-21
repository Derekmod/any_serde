import types
from typing import (
    Any,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
    get_args,
    get_origin,
)
from any_serde.common import (
    InvalidSerializationException,
    InvalidDeserializationException,
    JSON,
    SerdeConfig,
    resolve_newtypes,
)

# ExplicitUnion = NewType("ExplicitUnion", Union)
"""Serializes which union option is used, not just the value."""


T_Any = TypeVar("T_Any")


# # class ExplicitUnion(Generic[T_Any]):
# #     # def __init__(self, union_type: Type[Any]) -> None:
# #     #     self.union_type = union_type
# #     pass


# ExplicitUnion = Union[T_Any, T_Any]
# Boolable = Union[bool, T_Any]


# def get_explicit_union(union_type: T_Any) -> T_Any:
#     return Union[*union_type]
#     # # TODO: assert is a union
#     # explicit_type = copy.copy(union_type)
#     # setattr
#     # setattr(explicit_type, "__any_serde_explicit_union__", True)
#     # return explicit_type


def _get_union_args(type_: Type[T_Any]) -> Sequence[Type[Any]]:
    type_origin_nullable = get_origin(type_)

    assert type_origin_nullable is not None, f"Calling union serde on non-union type: {type_}"

    type_origin = resolve_newtypes(type_origin_nullable)
    union_args = [resolve_newtypes(type_arg) for type_arg in get_args(type_)]

    assert type_origin in (Union, types.UnionType), f"Calling union serde on non-union type: {type_}"

    deduped_union_args = list(set(union_args))

    return deduped_union_args


def from_data(
    type_: Type[T_Any],
    data: JSON,
    serde_config: Optional[SerdeConfig],
) -> T_Any:
    if serde_config is None:
        serde_config = SerdeConfig()

    union_args = _get_union_args(type_)

    from any_serde import serde

    if serde_config.read_explicit_unions:
        if not isinstance(data, dict):
            raise InvalidDeserializationException(f"Expected explicit union type, got {type(data)}")
        if len(data) != 1:
            raise InvalidDeserializationException("Malformed explicit union data - multiple keys!")
        ((union_arg_idx_str, union_data),) = data.items()
        try:
            union_arg_idx = int(union_arg_idx_str)
        except ValueError:
            raise InvalidDeserializationException(f"Malformed explicit union data - key: {union_arg_idx}")
        union_arg = union_args[union_arg_idx]
        return serde.from_data(union_arg, union_data)

    for union_arg in union_args:
        try:
            return serde.from_data(union_arg, data)
        except InvalidDeserializationException:
            pass

    raise InvalidDeserializationException("Could not deserialize to any union option.")


def to_data(
    type_: Type[T_Any],
    item: T_Any,
    serde_config: Optional[SerdeConfig],
) -> JSON:
    if serde_config is None:
        serde_config = SerdeConfig()

    union_args = _get_union_args(type_)

    from any_serde import serde

    if serde_config.write_explicit_unions:
        for union_arg_idx, union_arg in enumerate(union_args):
            try:
                return {str(union_arg_idx): serde.to_data(union_arg, item)}
            except InvalidSerializationException:
                pass

        raise InvalidSerializationException("Could not serialize from any union option.")

    for union_arg in union_args:
        try:
            return serde.to_data(union_arg, item)
        except InvalidSerializationException:
            pass

    raise InvalidSerializationException("Could not serialize from any union option.")
