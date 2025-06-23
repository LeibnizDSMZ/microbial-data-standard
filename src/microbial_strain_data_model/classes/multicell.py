from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.sourcestring import SourceLink


class MultiCell(BaseModel):
    """MultiCell ability of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    multiCellComplexForming: bool = Field(title="Multi Cell Complex Forming")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
