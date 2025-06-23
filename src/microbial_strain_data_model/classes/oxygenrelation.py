from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class OxygenRelation(BaseModel):
    """OxygenRelation of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    oxygenRelation: str = Field(title="Oxygen Relation")
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
