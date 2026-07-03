# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_utils.builder.load_env import SchemaPaths
from microbial_strain_data_utils.builder.load_env import load_schema_paths
from typing import Sequence
from typing import Any
import json


def write_mermaid(
    paths: SchemaPaths, classes: dict[str, Any], links: Sequence[tuple[str, str]]
):
    with paths.docs_mermaid.open("w") as f_out:
        f_out.write("---\nhide:\n  - navigation\n  - toc\n")
        f_out.write("search:\n  exclude: true\n---\n\n")
        f_out.write("``` mermaid\n")
        f_out.write("classDiagram\n")
        f_out.write("direction LR\n")

        for name, class_data in classes.items():
            if class_data:
                f_out.write(
                    f"class `{name.replace('_Literal__', '[').replace('___', ']')}`"
                    + "{\n"
                )
                for field_name, type in class_data.items():
                    if field_name == "enum":
                        f_out.write("<<enumeration>>\n")
                        for x in type:
                            f_out.write(f"{x}\n")
                    else:
                        type_repl = type.replace("_Literal__", "[").replace("___", "]")
                        f_out.write(f"{field_name}: {type_repl}\n".replace(" \n", "\n"))
                f_out.write("}\n\n")

        for link in links:
            link_0 = link[0].replace("_Literal__", "[").replace("___", "]")
            link_1 = link[1].replace("_Literal__", "[").replace("___", "]")
            f_out.write(f"`{link_0}` ..> `{link_1}`\n")

        f_out.write("```\n")


def get_prop_type_and_links(prop: dict[str, Any]):
    types = []
    links = []

    if ref := prop.get("$ref"):
        types = [ref.split("/")[-1]]
        links = [ref.split("/")[-1]]
    elif typ := prop.get("type"):
        if typ == "array":
            items = prop.get("items", {})
            if ref := items.get("$ref"):
                types.append(f"array[{ref.split('/')[-1]}]")
                links.append(ref.split("/")[-1])
            elif array_type := items.get("type"):
                types.append(array_type)
        else:
            types = [typ]
    elif any_of := prop.get("anyOf"):
        for a in any_of:
            if ref := a.get("$ref"):
                types.append(ref.split("/")[-1])
                links.append(ref.split("/")[-1])
            if t := a.get("type"):
                types.append(t)

    return " | ".join(x for x in types), links


def parse_object(
    schema: dict[str, Any],
    classes: dict[str, Any],
    links: list[tuple[str, str]],
    title: str,
    whole_schema: dict[str, Any],
):
    attr = {}
    for name, prop in schema.get("properties", {}).items():
        attr[name], prop_links = get_prop_type_and_links(prop)
        for p_link in prop_links:
            links.append((title, p_link))
            if p_link not in classes.keys():
                classes[p_link] = {}
                parse_object(
                    whole_schema["$defs"][p_link], classes, links, p_link, whole_schema
                )
    if enum := schema.get("enum"):
        attr["enum"] = enum

    classes[title] = attr


def parse_schema(schema: dict[str, Any]):
    classes: dict[str, Any] = {}
    links: list[tuple[str, str]] = []
    title = schema.get("title")
    if not isinstance(title, str):
        title = ""

    parse_object(schema, classes, links, title, schema)

    return classes, links


def run() -> None:
    paths = load_schema_paths()
    with paths.json_schema.open("r") as schema_file:
        schema = json.load(schema_file)
    classes, links = parse_schema(schema)
    write_mermaid(paths, classes, links)


if __name__ == "__main__":
    run()
