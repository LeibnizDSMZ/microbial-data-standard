from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import FlagellumArrangement
from microbial_strain_data_model.classes.sourcestring import SourceString


class Motility(BaseModel):
    """Information on motility of a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    motile: bool | None = Field(default=None, title="Motile", alias="motile")
    flagellum: bool | None = Field(default=None, title="Flagellum", alias="flagellum")
    flag_arr: FlagellumArrangement | None = Field(
        default=None, title="Flagellum Arrangement", alias="flagellumArrangement"
    )
    gliding: bool | None = Field(default=None, title="Gliding", alias="gliding")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
