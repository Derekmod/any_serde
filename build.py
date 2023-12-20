from jinja2 import Template
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT_DIR = SCRIPT_PATH.parent


def write_explicit_union() -> None:
    explicit_union_template_path = PROJECT_ROOT_DIR / "any_serde" / "explicit_union.py.jinja2"
    with explicit_union_template_path.open("rt") as fin_template:
        explicit_union_template = Template(fin_template.read())
    explicit_union_code = explicit_union_template.render(
        MAX_UNION_ARGS=10,
    )
    explicit_union_path = PROJECT_ROOT_DIR / "any_serde" / "explicit_union.py"
    with explicit_union_path.open("wt") as fout_code:
        fout_code.write(explicit_union_code)


def main() -> None:
    write_explicit_union()


if __name__ == "__main__":
    main()
