from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints


class GCContent(BaseModel):
    """GC content of the microorganism"""

    method: str | None = Field(default=None, title="Method", alias="method")
    value: Annotated[float, Field(ge=0, le=100)] = Field(
        title="Percent Value", alias="value"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
