from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints

from microbial_strain_data_model.classes.enums import HemolysisBlood, HemolysisType


class Hemolysis(BaseModel):
    """Hemolysis of bloods"""

    blood: HemolysisBlood = Field(title="Blood", alias="blood")
    hemolysis: HemolysisType = Field(title="Hemolysis Type", alias="hemolysisType")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
