import json
from pathlib import Path


def write_mermaid(classes, links):
    f_path = Path("/workspace/docs/graph.md")
    with open(f_path, "w") as f_out:
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
                        f_out.write(
                            f"{field_name}: {type.replace('_Literal__', '[').replace('___', ']')}\n"
                        )
                f_out.write("}\n\n")

        for link in links:
            f_out.write(
                f"`{link[0].replace('_Literal__', '[').replace('___', ']')}` ..> `{link[1].replace('_Literal__', '[').replace('___', ']')}`\n"
            )

        f_out.write("```\n")


def get_prop_type_and_links(prop):
    types = []
    links = []

    if ref := prop.get("$ref"):
        types = [ref.split("/")[-1]]
        links = [ref.split("/")[-1]]
    elif t := prop.get("type"):
        if t == "array":
            items = prop.get("items")
            if ref := items.get("$ref"):
                types.append(f"array[{ref.split('/')[-1]}]")
                links.append(ref.split("/")[-1])
            elif array_type := items.get("type"):
                types.append(array_type)
        else:
            types = [t]
    elif any_of := prop.get("anyOf"):
        for a in any_of:
            if ref := a.get("$ref"):
                types.append(ref.split("/")[-1])
                links.append(ref.split("/")[-1])
            if t := a.get("type"):
                types.append(t)

    return " | ".join(x for x in types), links


def parse_object(schema, classes, links, title, whole_schema):
    attr = {}
    for name, prop in schema.get("properties", {}).items():
        attr[name], prop_links = get_prop_type_and_links(prop)
        for p_link in prop_links:
            links.append((title, p_link))
            if not p_link in classes.keys():
                classes[p_link] = {}
                parse_object(
                    whole_schema["$defs"][p_link], classes, links, p_link, whole_schema
                )
    if enum := schema.get("enum"):
        attr["enum"] = enum

    classes[title] = attr


def parse_schema(schema):
    classes = {}
    links = []
    title = schema.get("title")

    parse_object(schema, classes, links, title, schema)

    return classes, links


if __name__ == "__main__":
    schema_path = Path("/workspace/schema/microbe_schema.json")
    with open(schema_path, "r") as schema_file:
        schema = json.load(schema_file)
    classes, links = parse_schema(schema)
    write_mermaid(classes, links)
