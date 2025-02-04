from pydantic import BaseModel, ConfigDict, Field, PositiveFloat

from microbial_strain_data_model.classes.enums import SizeUnit

from microbial_strain_data_model.classes.sourcestring import SourceString


class Size(BaseModel):
    """size object, use only for micro and millimeter"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    min: PositiveFloat = Field(title="Minimal", alias="minimal")
    max: PositiveFloat = Field(title="Maximal", alias="maximal")
    unit: SizeUnit = Field(title="Unit", alias="unit")


class CellSize(BaseModel):
    """object to hold cell size information"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    cell_length: Size = Field(title="Cell Length", alias="cellLength", description="")
    cell_width: Size = Field(title="Cell Width", alias="cellWidth", description="")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
