from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints, PositiveFloat

from microbial_strain_data_model.classes.enums import SizeUnit


class Size(BaseModel):
    """size object, use only for micro and millimeter"""

    min: PositiveFloat = Field(title="Minimal", alias="minimal")
    max: PositiveFloat = Field(title="Maximal", alias="maximal")
    unit: SizeUnit = Field(title="Unit", alias="unit")


class CellSize(BaseModel):
    """object to hold cell size information"""

    cell_length: Size = Field(title="Cell Length", alias="cellLength", description="")
    cell_width: Size = Field(title="Cell Width", alias="cellWidth", description="")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
