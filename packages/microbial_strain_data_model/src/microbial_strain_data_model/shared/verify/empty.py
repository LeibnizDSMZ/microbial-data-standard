from typing import Any
from typing import TypeVar

_OBJ = TypeVar("_OBJ", bound=object)


def check_not_completely_empty(class_obj: _OBJ) -> _OBJ:
    for key, val in class_obj.__dict__.items():
        if val and key != "source":
            return class_obj
    raise ValueError("Model is completely empty")


def is_empty(x: Any) -> bool:
    return x is None or x == {} or x == [] or x == ""
