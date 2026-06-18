# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_utils.builder.load_env import git_add_schema_files
from microbial_strain_data_utils.builder.load_env import SchemaPaths
from microbial_strain_data_utils.builder.load_env import load_schema_paths
from typing import Any
import jsonref
import json
import tomllib
import tomli_w
from microbial_strain_data_model.strain import Strain


def write_documentation(
    paths: SchemaPaths,
    name: str,
    title: str,
    type: str,
    format: str | list[str],
    description: str,
    mid: str,
    is_req: bool,
):
    f_path = paths.docs_schema.joinpath(f"{mid.split('.')[0]}. {name.split('.')[0]}.md")
    with f_path.open("a") as f_out:
        f_out.write("---\n")
        f_out.write(f"## {mid} {name}\n")
        f_out.write(f"{title}  ")
        if is_req:
            f_out.write("`Required`\n\n")
        else:
            f_out.write("\n\n")
        if description != "":
            f_out.write("Description:\n")
            for line in description.splitlines():
                if len(line) < 2:
                    f_out.write(">\n")
                else:
                    f_out.write(f"> {line}  \n")
            f_out.write("\n")
        f_out.write(f"**{type}**\n\n")
        if format:
            if isinstance(format, list):
                f_out.write("Enum:\n\n")
                for val in format:
                    f_out.write(f"\t{val}\n")
            else:
                f_out.write(f"Format:\n\n\t{format}\n")
            f_out.write("\n")


def _get_type(schema: dict[str, Any]) -> Any:
    if type := schema.get("type"):
        if type == "array":
            return f"`{type}` of `{schema.get('items', {}).get('type')}`"
        return type
    if any := schema.get("anyOf", None):
        return ", ".join([x.get("type") for x in any])
    if all := schema.get("allOf", None):
        return ", ".join([x.get("type") for x in all])
    return "?"


def _get_value(schema: dict[str, Any]) -> Any:
    if format := schema.get("format"):
        return format
    if enum := schema.get("enum"):
        return enum
    if enum := schema.get("anyOf", [{}])[0].get("enum", None):
        return enum
    if enum := schema.get("allOf", [{}])[0].get("enum", None):
        return enum


def parse_schema(paths: SchemaPaths) -> None:
    mi = Strain.model_json_schema()
    with paths.json_schema.open("w") as f_out:
        f_out.write(json.dumps(mi, indent=2))

    schema = json.dumps(mi)
    main_schema = jsonref.loads(schema)

    transformed_schema: dict[Any, Any] = {
        "id": [],
        "Structure": [],
        "Title": [],
        "Type": [],
        "Required": [],
        "Value": [],
        "Description": [],
        "Rest": [],
    }

    def recursive_parser(
        paths: SchemaPaths,
        schema_part: dict[str, Any],
        name_prefix: str,
        counter_pre: str,
        required: list[str],
    ):
        counter = 0
        for key, value in schema_part.items():
            counter = counter + 1

            if counter_pre:
                id = f"{counter_pre}{counter!s}."
            else:
                id = f"{'0' if counter < 10 else ''}{counter!s}."

            name = f"{name_prefix}{key}"
            title = value.get("title", "")
            if not isinstance(title, str):
                title = ""
            type = _get_type(value)
            value_resolved = _get_value(value)
            description = value.get(
                "description", value.get("items", {}).get("description", "")
            )

            is_req = True if required and key in required else False

            transformed_schema["id"].append(id)
            transformed_schema["Structure"].append(name)
            transformed_schema["Title"].append(title)
            transformed_schema["Type"].append(type)
            transformed_schema["Required"].append(is_req)
            transformed_schema["Value"].append(value_resolved)
            transformed_schema["Description"].append(description)
            transformed_schema["Rest"].append(value)

            write_documentation(
                paths, name, title, type, value_resolved, description, id, is_req
            )

            if next_schema := value.get("properties"):
                recursive_parser(
                    paths, next_schema, f"{name}.", id, value.get("required")
                )
            if next_schema := value.get("items", {}).get("properties"):
                recursive_parser(
                    paths,
                    next_schema,
                    f"{name}.",
                    id,
                    value.get("items", {}).get("required"),
                )
            for any in value.get("anyOf", []):
                if next_schema := any.get("properties"):
                    if name != "taxon.parentTaxon" and name != "unifiedTaxon.parentTaxon":
                        recursive_parser(
                            paths, next_schema, f"{name}.", id, any.get("required")
                        )

    recursive_parser(
        paths, main_schema.get("properties"), "", "", main_schema.get("required")
    )


def update_nav_config(paths: SchemaPaths, schemas: list[str]) -> None:
    with paths.docs_config.open("rb") as fze:
        config = tomllib.load(fze)

    if "project" not in config:
        project: dict[str, Any] = {}
        config["project"] = project

    if "nav" not in config["project"]:
        pr_nav: list[dict[str, list[str]]] = []
        config["project"]["nav"] = pr_nav

    nav_entries = config["project"]["nav"]

    for ind, entry in enumerate(nav_entries):
        if isinstance(entry, dict) and "Data schema" in entry:
            nav_entries[ind]["Data schema"] = schemas
            break
    else:
        nav_entries.append({"Data schema": schemas})

    with paths.docs_config.open("wb") as fze:
        tomli_w.dump(config, fze)


def clear_docs_schema(paths: SchemaPaths):
    for file in paths.docs_schema.glob("*.md"):
        file.unlink()


def clean_end_of_files(paths: SchemaPaths):
    for file in paths.docs_schema.glob("*.md"):
        lines: list[str] = []
        with file.open("r") as f_in:
            lines = f_in.readlines()[:-1]
        with file.open("w") as f_out:
            for line in lines:
                f_out.write(line)
        yield str(file.relative_to(paths.docs_schema.parent))


def run() -> None:
    paths = load_schema_paths()
    clear_docs_schema(paths)
    parse_schema(paths)
    md_list = list(sorted(clean_end_of_files(paths)))
    update_nav_config(paths, md_list)
    git_add_schema_files(paths)


if __name__ == "__main__":
    run()
