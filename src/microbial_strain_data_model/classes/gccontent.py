from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.links import SourceLink


class GCContent(BaseModel):
    """GC content of the microorganism"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    method: str | None = Field(
        default=None,
        title="Method",
        description="Name of the method used to measure the GC content",
    )
    value: Annotated[float, Field(ge=0, le=100)] = Field(
        title="Percent Value",
        description="Percent value of how much percent of the DNA is GC pairs",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
