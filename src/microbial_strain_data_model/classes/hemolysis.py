from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from microbial_strain_data_model.classes.enums import HemolysisBlood, HemolysisType


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
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
