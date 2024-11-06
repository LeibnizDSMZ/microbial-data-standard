from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints


class CellShape(BaseModel):
    """Cell shape of the strain"""

    cell_shape: str = Field(title="Cell Shape", alias="cellShape")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
