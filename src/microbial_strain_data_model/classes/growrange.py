from typing import Generic, TypeVar
from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints


T = TypeVar("T")


class GrowthRange(BaseModel, Generic[T]):
    """Single grow condition test"""

    minimal: float | None = Field(default=None, title="Minimal", alias="minimal")
    maximal: float | None = Field(default=None, title="Maximal", alias="maximal")
    unit: T
    growth: bool = Field(title="Growth", alias="growth")


class Growth(BaseModel, Generic[T]):
    """Optimal and tested information about growing a Strain"""

    optimal: float | None = Field(default=None, title="Optimal", alias="optimal")
    minimal: float | None = Field(default=None, title="Minimal", alias="minimal")
    maximal: float | None = Field(default=None, title="Maximal", alias="maximal")
    unit: T
    tests: list[GrowthRange[T]] = Field(
        default_factory=list, title="Tests", alias="tested"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
