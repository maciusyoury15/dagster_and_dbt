from pathlib import Path

from dagster import definitions, load_from_defs_folder


# @definitions
# def defs():
#     return load_from_defs_folder(project_root=Path(__file__).parent.parent.parent)



def find_project_root() -> Path:
    current = Path(__file__).resolve().parent

    for directory in (current, *current.parents):
        if (
            (directory / "pyproject.toml").is_file()
            or (directory / "dg.toml").is_file()
        ):
            return directory

    raise FileNotFoundError(
        "Could not find pyproject.toml or dg.toml"
    )


@definitions
def defs():
    project_root = find_project_root()

    return load_from_defs_folder(
        project_root=project_root
    )