from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.sourcestring import SourceLink


class CellShape(BaseModel):
    """Cell shape of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    cellShape: str = Field(title="Cell Shape")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
