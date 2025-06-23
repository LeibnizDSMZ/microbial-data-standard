from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.sourcestring import SourceLink


class GCContent(BaseModel):
    """GC content of the microorganism"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    method: str | None = Field(default=None, title="Method")
    value: Annotated[float, Field(ge=0, le=100)] = Field(title="Percent Value")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
