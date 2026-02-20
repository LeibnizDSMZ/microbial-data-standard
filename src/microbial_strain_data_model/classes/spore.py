from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import SporeType

from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class Spore(BaseModel):
    """Spore information about one Strain."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    sporeBuilding: bool | None = Field(default=None, title="sporeBuilding")
    typeOfSpore: SporeType = Field(title="Type Of Spore")
    sporeEjection: str | None = Field(default=None, title="Spore Ejection")
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
