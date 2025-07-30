from typing import Generic, TypeVar
from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.links import SourceLink, RelationLink

T = TypeVar("T")


class GrowthRange(BaseModel, Generic[T]):
    """Single grow condition test"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    minimal: float | None = Field(
        default=None, title="Minimal", description="Minimal value of tested range"
    )
    maximal: float | None = Field(
        default=None, title="Maximal", description="Maximal value of tested range"
    )
    unit: T
    growth: bool = Field(
        title="Growth", description="Does the strain grow within this range?"
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )


class Growth(BaseModel, Generic[T]):
    """Optimal and tested information about growing a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    optimal: float | None = Field(
        default=None, title="Optimal", description="Single optimal growth value"
    )
    minimal: float | None = Field(
        default=None, title="Minimal", description="Known minimal growth value"
    )
    maximal: float | None = Field(
        default=None, title="Maximal", description="Known maximal growth value"
    )
    unit: T
    tests: list[GrowthRange[T]] = Field(
        default_factory=list,
        title="Tests",
        description="List of tests and if the strain grows in tested ranges",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
