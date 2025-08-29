from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.chemicalsubstance import ChemicalSubstance
from microbial_strain_data_model.classes.enums import ConcentrationUnit, ToleranceReaction

from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class ToleranceTest(BaseModel):
    """Tested tolerance of compound"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    reaction: ToleranceReaction = Field(title="Reaction")
    concentration: float | None = Field(
        default=None, title="Concentration", description="Concentration value"
    )
    unit: ConcentrationUnit = Field(
        title="Unit", description="Unit of concentration e.g. g/ml"
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )


class Tolerance(ChemicalSubstance):
    """Tolerance information - e.g. antibiotic resistance"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    reaction: ToleranceReaction | None = Field(default=None, title="Reaction")
    mic: str | None = Field(
        default=None, title="MIC", description="The minimal inhibitory concentration"
    )
    unit: ConcentrationUnit | None = Field(default=None, title="Unit")
    tests: list[ToleranceTest] = Field(default_factory=list, title="Tests")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
