from typing import Union, TypeVar, Type, Dict, List


JSON_PRIMITIVE_TYPES = [
    str,
    int,
    float,
    bool,
    None,
    type(None),
]
JSONPrimitive = Union[
    str,
    int,
    float,
    bool,
    None,
]
JSON = Union[
    JSONPrimitive,
    Dict[str, "JSON"],
    List["JSON"],
]

# class _JSONType(typing._UnionGenericAlias):
# class _JSONType:
#     def __repr__(self) -> str:
#         if self is JSON:
#             return "JSON"
#         return JSON.__class__.__repr__(self)

#     def __str__(self) -> str:
#         return "JSON"


# JSON.__class__.__repr__ = _JSONType.__repr__

# _JSON_ARGS = list(JSON.__args__)
# _JSON_ARGS[-1] = typing.List[JSON]
# _JSON_ARGS[-2] = typing.Dict[str, JSON]
# JSON.__args__ = tuple(_JSON_ARGS)


T_Any = TypeVar("T_Any")


def resolve_newtypes(typ: Type[T_Any]) -> Type[T_Any]:
    # https://github.com/python/mypy/issues/3325
    while hasattr(typ, "__supertype__"):
        typ = getattr(typ, "__supertype__")
    return typ


class InvalidDeserializationException(Exception):
    """Indicates that the given data is not valid for the target type given."""


class InvalidSerializationException(Exception):
    """Indicates that the given variable could not be serialized."""
