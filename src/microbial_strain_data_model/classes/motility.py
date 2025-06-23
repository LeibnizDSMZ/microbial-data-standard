from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import FlagellumArrangement
from microbial_strain_data_model.classes.sourcestring import SourceLink


class Motility(BaseModel):
    """Information on motility of a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    motile: bool | None = Field(default=None, title="Motile")
    flagellum: bool | None = Field(default=None, title="Flagellum")
    flagellumArrangement: FlagellumArrangement | None = Field(
        default=None, title="Flagellum Arrangement"
    )
    gliding: bool | None = Field(default=None, title="Gliding")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
