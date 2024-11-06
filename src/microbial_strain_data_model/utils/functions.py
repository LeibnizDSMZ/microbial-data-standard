from typing import Any, TypeVar


_OBJ = TypeVar("_OBJ", bound=object)


def check_not_completely_empty(class_obj: _OBJ) -> _OBJ:
    for key, val in class_obj.__dict__.items():
        if val and key != "source":
            return class_obj
    raise ValueError("Model is completely empty")


def empty(x: Any) -> bool:
    return x is None or x == {} or x == [] or x == ""


def clean_dict(dct: dict[str, Any]) -> dict[str, Any]:
    final = {}
    for k, v in dct.items():
        if isinstance(v, dict):
            v = clean_dict(v)
        elif isinstance(v, list):
            v = clean_list(v)
        if not empty(v):
            final[k] = v
    return final


def clean_list(lst: list[Any]) -> list[Any]:
    final = []
    for v in lst:
        if isinstance(v, list):
            v = clean_list(v)
        elif isinstance(v, dict):
            v = clean_dict(v)
        if not empty(v):
            final.append(v)
    return final
