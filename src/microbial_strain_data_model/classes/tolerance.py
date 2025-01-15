from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from microbial_strain_data_model.classes.chemicalsubstance import ChemicalSubstance
from microbial_strain_data_model.classes.enums import ConcentrationUnit, ToleranceReaction


class ToleranceTest(BaseModel):
    """Tested tolerance of compound"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    reaction: ToleranceReaction = Field(title="Reaction", alias="reaction")
    concentration: str | None = Field(
        default=None, title="Concentration", alias="concentration"
    )
    unit: ConcentrationUnit = Field(title="Unit", alias="unit")


class Tolerance(ChemicalSubstance):
    """Tolerance information - e.g. antibiotic resistance"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    reaction: str | None = Field(default=None, title="Reaction", alias="reaction")
    mic: str | None = Field(default=None, title="MIC", alias="mic")
    unit: ConcentrationUnit | None = Field(default=None, title="Unit", alias="unit")
    tests: list[ToleranceTest] = Field(default_factory=list, title="Tests", alias="tests")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
