from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import HemolysisBlood, HemolysisType

from microbial_strain_data_model.classes.sourcestring import SourceString


class Hemolysis(BaseModel):
    """Hemolysis of bloods"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    blood: HemolysisBlood = Field(title="Blood", alias="blood")
    hemolysis: HemolysisType = Field(title="Hemolysis Type", alias="hemolysisType")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
