from typing import Generic, TypeVar
from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.sourcestring import SourceString

T = TypeVar("T")


class GrowthRange(BaseModel, Generic[T]):
    """Single grow condition test"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    minimal: float | None = Field(default=None, title="Minimal", alias="minimal")
    maximal: float | None = Field(default=None, title="Maximal", alias="maximal")
    unit: T
    growth: bool = Field(title="Growth", alias="growth")


class Growth(BaseModel, Generic[T]):
    """Optimal and tested information about growing a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    optimal: float | None = Field(default=None, title="Optimal", alias="optimal")
    minimal: float | None = Field(default=None, title="Minimal", alias="minimal")
    maximal: float | None = Field(default=None, title="Maximal", alias="maximal")
    unit: T
    tests: list[GrowthRange[T]] = Field(
        default_factory=list, title="Tests", alias="tested"
    )
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
