from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.links import SourceLink


class RelatedData(BaseModel):
    """RelatedData."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    relation: str = Field(
        title="Relation",
        description="The kind or type of relation of the data points, e.g. "
        "growthCondition, testCondition, API20",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
