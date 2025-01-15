from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from microbial_strain_data_model.classes.enums import FlagellumArrangement


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
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
