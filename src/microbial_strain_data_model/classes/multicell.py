from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints


class MultiCell(BaseModel):
    """MultiCell ability of the strain"""

    multi_cell: bool = Field(
        title="Multi Cell Complex Forming", alias="multiCellComplexForming"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
