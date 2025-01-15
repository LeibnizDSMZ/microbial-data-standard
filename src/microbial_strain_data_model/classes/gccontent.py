from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints


class GCContent(BaseModel):
    """GC content of the microorganism"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    method: str | None = Field(default=None, title="Method", alias="method")
    value: Annotated[float, Field(ge=0, le=100)] = Field(
        title="Percent Value", alias="value"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
