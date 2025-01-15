from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints


class CellShape(BaseModel):
    """Cell shape of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    cell_shape: str = Field(title="Cell Shape", alias="cellShape")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
