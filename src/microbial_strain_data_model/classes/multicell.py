from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints


class MultiCell(BaseModel):
    """MultiCell ability of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    multi_cell: bool = Field(
        title="Multi Cell Complex Forming", alias="multiCellComplexForming"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
