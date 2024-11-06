from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints

from microbial_strain_data_model.classes.enums import SizeUnit


class Size(BaseModel):
    """size object, use only for micro and millimeter"""

    min: float = Field(title="Minimal", alias="minimal")
    max: float = Field(title="Maximal", alias="maximal")
    unit: SizeUnit = Field(title="Unit", alias="unit")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
