from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.sourcestring import SourceString


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
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
