from typing import Generic, TypeVar
from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.links import SourceLink

T = TypeVar("T")


class GrowthRange(BaseModel, Generic[T]):
    """Single grow condition test"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    minimal: float | None = Field(default=None, title="Minimal")
    maximal: float | None = Field(default=None, title="Maximal")
    unit: T
    growth: bool = Field(title="Growth")


class Growth(BaseModel, Generic[T]):
    """Optimal and tested information about growing a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    optimal: float | None = Field(default=None, title="Optimal")
    minimal: float | None = Field(default=None, title="Minimal")
    maximal: float | None = Field(default=None, title="Maximal")
    unit: T
    tests: list[GrowthRange[T]] = Field(default_factory=list, title="Tests")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
