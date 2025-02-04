from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.sourcestring import SourceString


class CellShape(BaseModel):
    """Cell shape of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    cell_shape: str = Field(title="Cell Shape", alias="cellShape")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
