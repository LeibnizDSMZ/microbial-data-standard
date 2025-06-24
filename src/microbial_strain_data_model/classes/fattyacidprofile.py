from typing import Self
from pydantic import BaseModel, ConfigDict, Field, model_validator

from microbial_strain_data_model.classes.chemicalsubstance import FattyAcid

from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class FattyAcidProfile(BaseModel):
    """Full Fatty Acid Profile"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    profile: list[FattyAcid] = Field(default_factory=list, title="Profile")
    library: str | None = Field(default=None, title="Library")
    software: str | None = Field(default=None, title="Software")
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def ensure_list_not_empty(self) -> Self:
        if len(self.profile) < 1:
            raise ValueError("Fatty Acis Profile must contain at least one Fatty Acid")
        return self
