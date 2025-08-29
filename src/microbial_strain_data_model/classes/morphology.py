from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import ColonyColor, FlagellumArrangement
from microbial_strain_data_model.classes.links import SourceLink
from microbial_strain_data_model.classes.size import Size


class Morphology(BaseModel):
    """Morphology of a cell"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    cellShape: str = Field(title="Cell Shape", description="The shape type the cells")
    cellLength: Size = Field(title="Cell Length", description="Length of a cell")
    cellWidth: Size = Field(title="Cell Width", description="Width of a cell")
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
    colonySize: Size | None = Field(default=None, title="Size of Colony")
    colonyColor: ColonyColor | None = Field(
        default=None, title="Color of Colony", description="Color of the colony on the"
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
