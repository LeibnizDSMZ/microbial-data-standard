from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import FlagellumArrangement
from microbial_strain_data_model.classes.links import SourceLink


class Motility(BaseModel):
    """Information on motility of a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    motile: bool | None = Field(
        default=None,
        title="Motile",
        description="Are the cells of this strain are motile",
    )
    flagellum: bool | None = Field(
        default=None, title="Flagellum", description="Do the cells have flagella"
    )
    flagellumArrangement: FlagellumArrangement | None = Field(
        default=None,
        title="Flagellum Arrangement",
        description="How are the flagella arranged",
    )
    gliding: bool | None = Field(
        default=None,
        title="Gliding",
        description="Cells can be motile by gliding instead of having flagella",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
