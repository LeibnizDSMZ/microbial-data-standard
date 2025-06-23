from pydantic import BaseModel, ConfigDict, Field, PositiveFloat

from microbial_strain_data_model.classes.enums import SizeUnit

from microbial_strain_data_model.classes.links import SourceLink


class Size(BaseModel):
    """size object, use only for micro and millimeter"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    minimal: PositiveFloat = Field(title="Minimal")
    maximal: PositiveFloat = Field(title="Maximal")
    unit: SizeUnit = Field(title="Unit")


class CellSize(BaseModel):
    """object to hold cell size information"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    cellLength: Size = Field(title="Cell Length", description="")
    cellWidth: Size = Field(title="Cell Width", description="")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
