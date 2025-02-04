from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import StainingValue

from microbial_strain_data_model.classes.sourcestring import SourceString


class Staining(BaseModel):
    """Stainings tested on the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", alias="name")
    value: StainingValue = Field(title="Value", alias="value")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
