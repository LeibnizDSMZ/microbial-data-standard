from microbial_strain_data_model.shared.verify.empty import is_empty
from typing import Any


def clean_dict(dct: dict[str, Any]) -> dict[str, Any]:
    final = {}
    for k, v in dct.items():
        if isinstance(v, dict):
            v = clean_dict(v)
        elif isinstance(v, list):
            v = clean_list(v)
        if not is_empty(v):
            final[k] = v
    return final


def clean_list(lst: list[Any]) -> list[Any]:
    final = []
    for v in lst:
        if isinstance(v, list):
            v = clean_list(v)
        elif isinstance(v, dict):
            v = clean_dict(v)
        if not is_empty(v):
            final.append(v)
    return final
