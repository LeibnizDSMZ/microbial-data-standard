from pydantic import BaseModel, ConfigDict, Field, model_validator

from microbial_strain_data_model.classes.enums import ColonyColor, FlagellumArrangement
from microbial_strain_data_model.classes.links import SourceLink
from microbial_strain_data_model.classes.size import Size

from microbial_strain_data_model.utils.functions import check_not_completely_empty


class Morphology(BaseModel):
    """Morphology of a cell"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    cellShape: str | None = Field(
        default=None, title="Cell Shape", description="The shape type the cells"
    )
    cellLength: Size | None = Field(
        default=None, title="Cell Length", description="Length of a cell"
    )
    cellWidth: Size | None = Field(
        default=None, title="Cell Width", description="Width of a cell"
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
    colonySize: Size | None = Field(default=None, title="Size of Colony")
    colonyColor: ColonyColor | None = Field(
        default=None, title="Color of Colony", description="Color of the colony on the"
    )
    multiCellComplexForming: bool | None = Field(
        default=None,
        title="Multi Cell Complex Forming",
        description="Do the cells form complexes",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
