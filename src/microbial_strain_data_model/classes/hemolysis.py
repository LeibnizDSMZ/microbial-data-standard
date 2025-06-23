from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import HemolysisBlood, HemolysisType

from microbial_strain_data_model.classes.sourcestring import SourceLink


class Hemolysis(BaseModel):
    """Hemolysis of bloods"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    blood: HemolysisBlood = Field(title="Blood")
    hemolysisType: HemolysisType = Field(title="Hemolysis Type")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
