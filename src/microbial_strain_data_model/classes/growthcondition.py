from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import OxygenTolerance
from microbial_strain_data_model.classes.links import SourceLink, RelationLink


class GrowthRange(BaseModel):
    """Single grow condition test."""

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
    growth: bool = Field(
        title="Growth", description="Does the strain grow within this range?"
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )


class GrowthCondition(BaseModel):
    """Optimal and tested information about growing a Strain."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    optimalTemperature: float | None = Field(
        default=None,
        title="Optimal",
        description="Single optimal growth temperature value in celsius",
    )
    minimalTemperature: float | None = Field(
        default=None,
        title="Minimal",
        description="Known minimal growth temperature value in celsius",
    )
    maximalTemperature: float | None = Field(
        default=None,
        title="Maximal",
        description="Known maximal growth temperature value in celsius",
    )
    testsTemperature: list[GrowthRange] = Field(
        default_factory=list,
        title="Tests",
        description="List of tests and if the strain grows in tested ranges",
    )

    optimalPh: float | None = Field(
        default=None, title="Optimal", description="Single optimal growth pH value"
    )
    minimalPh: float | None = Field(
        default=None, title="Minimal", description="Known minimal growth pH value"
    )
    maximalPh: float | None = Field(
        default=None, title="Maximal", description="Known maximal growth pH value"
    )
    testsPh: list[GrowthRange] = Field(
        default_factory=list,
        title="Tests",
        description="List of tests and if the strain grows in tested ranges",
    )

    oxygenRelation: OxygenTolerance | None = Field(
        default=None, title="Oxygen Relation", description="Aerobic, anaerobic etc."
    )

    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
