from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.sourcestring import SourceString


class OxygenRelation(BaseModel):
    """OxygenRelation of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    oxygenRelation: str = Field(title="Oxygen Relation")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
