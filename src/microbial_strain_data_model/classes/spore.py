from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from microbial_strain_data_model.classes.enums import SporeType


class Spore(BaseModel):
    """Spore information about one Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    building: bool | None = Field(
        default=None, title="sporeBuilding", alias="sporeBuilding"
    )
    type: SporeType = Field(title="Type Of Spore", alias="typeOfSpore")
    ejection: str | None = Field(
        default=None, title="Spore Ejection", alias="sporeEjection"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
