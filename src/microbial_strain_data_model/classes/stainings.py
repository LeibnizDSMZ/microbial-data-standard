from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints

from microbial_strain_data_model.classes.enums import StainingValue


class Staining(BaseModel):
    """Stainings tested on the strain"""

    name: str = Field(title="Name", alias="name")
    value: StainingValue = Field(title="Value", alias="value")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
