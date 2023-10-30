import dataclasses
import functools
from typing import (
    Any,
    Dict,
    List,
    Type,
)

from any_serde import dataclass_serde


def export_typescript(types: Dict[Type[Any], str]) -> str:
    if len(set(types.values())) < len(types):
        raise AssertionError("Exported types have duplicate names!")

    result_sections: List[str] = []

    @functools.lru_cache(None)
    def _export_typescript(type_: Type[Any], type_name: str) -> None:
        if not dataclass_serde.is_dataclass_type(type_):
            raise NotImplementedError(f"Cannot export {type_} yet!")

        # dataclass_fields = {field.name: field for field in dataclasses.fields(type_)}
        field_types = dataclass_serde._get_type_hints(type_)  # type: ignore

        class_code = ""
        class_code += f"interface {type_name} {{\n"

        validator_code = ""
        validator_code += "// eslint-disable-next-line @typescript-eslint/no-explicit-any"
        validator_code += "\n"
        validator_code += f"function validate_{type_name}(data: any): {type_name} {{"
        validator_code += "\n"
        validator_code += '  if (typeof data !== "object" || Array.isArray(data) || data === null) {'
        validator_code += "\n"
        validator_code += '    throw Error("Data is not valid!");'
        validator_code += "\n"
        validator_code += "  }"
        validator_code += "\n"
        validator_code += "\n"

        for field in dataclasses.fields(type_):
            field_type = field_types[field.name]
            if field_type in types:
                field_type_name = types[field_type]
                _export_typescript(field_type, field_type_name)  # type: ignore[arg-type]
                class_code += f"  {field.name}: {field_type_name};\n"
                validator_code += f"  const __{field.name} = validate_{field_type_name}(data.{field.name});\n"
                continue

            if isinstance(field_type, bool):
                class_code += f"  {field.name}: boolean;\n"
                validator_code += f"  const __{field.name} = data.{field.name};\n"
                validator_code += (
                    f'  if (__{field.name} === undefined || __{field.name} typeof __{field.name} !== "boolean") {{\n'
                )
                validator_code += '    throw Error("Data is not valid!")\n'
                validator_code += "  }\n"
                continue

            if isinstance(field_type, float):
                class_code += f"  {field.name}: number;\n"
                validator_code += f"  const __{field.name} = data.{field.name};\n"
                validator_code += (
                    f'  if (__{field.name} === undefined || __{field.name} typeof __{field.name} !== "number") {{\n'
                )
                validator_code += '    throw Error("Data is not valid!")\n'
                validator_code += "  }\n"
                continue

            if isinstance(field_type, int):
                class_code += f"  {field.name}: number;\n"
                validator_code += f"  const __{field.name} = data.{field.name};\n"
                validator_code += (
                    f'  if (__{field.name} === undefined || __{field.name} typeof __{field.name} !== "number"'
                )
                validator_code += f" || !Number.isInteger(__{field.name})) {{\n"
                validator_code += '    throw Error("Data is not valid!")\n'
                validator_code += "  }\n"
                continue

            if isinstance(field_type, str):
                class_code += f"  {field.name}: string;\n"
                validator_code += f"  const __{field.name} = data.{field.name};\n"
                validator_code += (
                    f'  if (__{field.name} === undefined || __{field.name} typeof __{field.name} !== "string") {{\n'
                )
                validator_code += '    throw Error("Data is not valid!")\n'
                validator_code += "  }\n"
                continue

            # TODO: unions
            # TODO: nulls
            # TODO: lists and dicts and others
            # TODO: enums

        pass

    for type_, type_name in types.items():
        _export_typescript(type_, type_name)  # type: ignore[arg-type]

    return "\n\n".join(result_sections)
