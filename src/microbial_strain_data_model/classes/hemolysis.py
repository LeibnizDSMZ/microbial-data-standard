from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import HemolysisBlood, HemolysisType

from microbial_strain_data_model.classes.links import SourceLink


class Hemolysis(BaseModel):
    """Hemolysis of bloods"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    blood: HemolysisBlood = Field(
        title="Blood", description="Type of blood used for the test"
    )
    hemolysisType: HemolysisType = Field(
        title="Hemolysis Type",
        description="Type of hemolysis that the strain is capable of",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
