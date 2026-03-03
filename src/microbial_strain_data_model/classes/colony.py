from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator

from microbial_strain_data_model.classes.enums import ColonyColor
from microbial_strain_data_model.classes.links import RelationLink, SourceLink
from microbial_strain_data_model.classes.size import Size
from microbial_strain_data_model.utils.functions import check_not_completely_empty


class Colony(BaseModel):
    """Colony morphology"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    colonySize: Size | None = Field(default=None, title="Size of Colony")
    colonyColor: ColonyColor | None = Field(
        default=None, title="Color of Colony", description="Color of the colony on the"
    )

    class ColonyAppearance(str, Enum):
        ARACHNOID = "arachnoid"
        FARINOSE = "farinose"
        SMOOTH = "smooth"
        VENOSE = "venose"
        WARTY = "warty"
        FURROWED = "furrowed"
        STRIATE = "striate"

    colonyAppearance: ColonyAppearance | None = Field(
        default=None,
        title="Colony Appearance",
        description="Specifies the shape appearance of the colony "
        "(controlled vocabulary)",
    )

    class ColonyTexture(str, Enum):
        FLUID = "fluid"
        MUCOID = "mucoid"
        BUTYROUS = "butyrous"
        MEMBRANOUS = "membranous"
        DRY = "dry"
        VELVETY = "velvety"
        POWDERY = "powdery"

    colonyTexture: ColonyTexture | None = Field(
        default=None,
        title="Colony Texture",
        description="Specifies the texture of the colony (controlled vocabulary)",
    )

    class DiffusingPigment(str, Enum):
        WHITE = "white"
        CREAM = "cream"
        YELLOWISH = "yellowish"
        ORANGE = "orange"
        PINK = "pink"
        RED = "red"
        BUFF = "buff"
        BLACK = "black"
        GREYISH = "greyish"
        TANNISH = "tannish"
        BEIGE = "beige"
        BROWN = "brown"
        BLUE = "blue"

    diffusingPigment: DiffusingPigment | None = Field(
        default=None,
        title="Diffusing Pigment",
        description="Specifies the color of a diffusing pigment from the colony "
        "(controlled vocabulary)",
    )

    class ColonyMargin(str, Enum):
        ENTIRE = "entire"
        ERODED = "eroded"
        OTHER = "other"

    colonyMargin: ColonyMargin | None = Field(
        default=None,
        title="Colony Margin",
        description="Specifies the margin of the colony (controlled vocabulary)",
    )

    multiCellComplexForming: bool | None = Field(
        default=None,
        title="Multi-cell Complex Forming",
        description="Indicates if the colony forms multi-cellular complexes",
    )

    visualAppearance: str | None = Field(
        default=None,
        title="Visual Appearance",
        description="Free text for non-standardized description of colony appearance",
    )

    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )

    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
