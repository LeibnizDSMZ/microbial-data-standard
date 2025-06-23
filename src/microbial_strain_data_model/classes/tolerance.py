from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.chemicalsubstance import ChemicalSubstance
from microbial_strain_data_model.classes.enums import ConcentrationUnit, ToleranceReaction

from microbial_strain_data_model.classes.links import SourceLink


class ToleranceTest(BaseModel):
    """Tested tolerance of compound"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    reaction: ToleranceReaction = Field(title="Reaction")
    concentration: str | None = Field(default=None, title="Concentration")
    unit: ConcentrationUnit = Field(title="Unit")


class Tolerance(ChemicalSubstance):
    """Tolerance information - e.g. antibiotic resistance"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    reaction: str | None = Field(default=None, title="Reaction")
    mic: str | None = Field(default=None, title="MIC")
    unit: ConcentrationUnit | None = Field(default=None, title="Unit")
    tests: list[ToleranceTest] = Field(default_factory=list, title="Tests")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
