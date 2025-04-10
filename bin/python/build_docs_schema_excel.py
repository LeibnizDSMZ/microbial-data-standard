from pathlib import Path
from typing import Any
import jsonref
import json
import pandas as pd

from microbial_strain_data_model.microbe import Microbe

# ruff: noqa: C901


def write_documentation(name, title, type, format, description, id, is_req):
    f_path = Path(f"docs/schema/{id.split('.')[0]}. {name.split('.')[0]}.md")
    with open(f_path, "a") as f_out:
        f_out.write("---\n")
        f_out.write(f"## {id} {name}\n")
        f_out.write(f"{title}  ")
        if is_req:
            f_out.write(f"`Required`\n\n")
        else:
            f_out.write(f"\n\n")
        if description:
            f_out.write(f"Description:\n")
            for line in description.splitlines():
                if len(line) < 2:
                    f_out.write(">\n")
                else:
                    f_out.write(f"> {line}  \n")
            f_out.write("\n")
        f_out.write(f"**{type}**\n\n")
        if format:
            if isinstance(format, list):
                f_out.write(f"Enum:\n\n")
                for x in format:
                    f_out.write(f"\t{x}\n")
            else:
                f_out.write(f"Format:\n\n\t{format}\n")
            f_out.write(f"\n")


def parse_schema() -> None:
    mi = Microbe.model_json_schema()
    main_schema_path = Path("schema/microbe_schema.json")
    with main_schema_path.open("w") as f_out:
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

    def get_type(schema: dict[Any, Any] | list[Any]) -> Any:
        if type := schema.get("type"):
            if type == "array":
                return f"{type}[{schema.get('items').get('type')}]"
            return type
        if any := schema.get("anyOf", None):
            return ", ".join([x.get("type") for x in any])
        if all := schema.get("allOf", None):
            return ", ".join([x.get("type") for x in all])
        return "?"

    def get_value(schema: dict) -> Any:
        if format := schema.get("format"):
            return format
        if enum := schema.get("enum"):
            return enum
        if enum := schema.get("anyOf", [{}])[0].get("enum", None):
            return enum
        if enum := schema.get("allOf", [{}])[0].get("enum", None):
            return enum

    def recursive_parser(
        schema_part: dict, name_prefix: str, counter_pre: str, required: list
    ) -> dict:
        counter = 0
        for key, value in schema_part.items():
            counter = counter + 1

            if counter_pre:
                id = f"{counter_pre}{counter!s}."
            else:
                id = f"{'0' if counter < 10 else ''}{counter!s}."

            name = f"{name_prefix}{key}"
            title = value.get("title", "")
            type = get_type(value)
            value_resolved = get_value(value)
            description = value.get(
                "description", value.get("items", {}).get("description")
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
                name, title, type, value_resolved, description, id, is_req
            )

            if next_schema := value.get("properties"):
                recursive_parser(next_schema, f"{name}.", id, value.get("required"))
            if next_schema := value.get("items", {}).get("properties"):
                recursive_parser(
                    next_schema, f"{name}.", id, value.get("items", {}).get("required")
                )
            for any in value.get("anyOf", []):
                if next_schema := any.get("properties"):
                    if name != "taxon.parentTaxon" and name != "unifiedTaxon.parentTaxon":
                        recursive_parser(next_schema, f"{name}.", id, any.get("required"))

    recursive_parser(main_schema.get("properties"), "", "", main_schema.get("required"))
    return transformed_schema


def export_excel(data_struc):
    mi_norm = pd.DataFrame(data_struc)
    # print(mi_norm.columns)
    mi_norm.to_excel("output_test.xlsx")


def clear_docs_schema():
    for file in Path("docs/schema").glob("*.md"):
        file.unlink()


def clean_end_of_files():
    for file in Path("docs/schema").glob("*.md"):
        lines = []
        with open(file, "r") as f_in:
            lines = f_in.readlines()[:-1]
        with open(file, "w") as f_out:
            for line in lines:
                f_out.write(line)


if __name__ == "__main__":
    clear_docs_schema()
    data_structure = parse_schema()
    export_excel(data_structure)
    clean_end_of_files()
