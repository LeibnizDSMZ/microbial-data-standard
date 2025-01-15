from typing import Self
from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, model_validator, StringConstraints

from microbial_strain_data_model.classes.chemicalsubstance import FattyAcid


class FattyAcidProfile(BaseModel):
    """Full Fatty Acid Profile"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    profile: list[FattyAcid] = Field(
        default_factory=list, title="Profile", alias="profile"
    )
    temperature: int | None = Field(
        default=None, title="Temperature", alias="temperature"
    )
    medium: str | None = Field(default=None, title="Medium", alias="medium")
    library: str | None = Field(default=None, title="Library", alias="library")
    software: str | None = Field(default=None, title="Software", alias="software")

    @model_validator(mode="after")
    def ensure_list_not_empty(self) -> Self:
        if len(self.profile) < 1:
            raise ValueError("Fatty Acis Profile must contain at least one Fatty Acid")
        return self

    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
