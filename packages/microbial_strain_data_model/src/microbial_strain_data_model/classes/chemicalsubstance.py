from microbial_strain_data_model.shared.verify.empty import check_not_completely_empty
from typing import Self
from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, model_validator

from microbial_strain_data_model.classes.enums import ConcentrationUnit
from microbial_strain_data_model.classes.growthcondition import GrowthRange
from microbial_strain_data_model.classes.metabolitetest import MetaboliteTest
from microbial_strain_data_model.classes.identifier import Identifier
from microbial_strain_data_model.classes.links import SourceLink


class ChemicalSubstance(BaseModel):
    """Chemical Substance base class."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str | None = Field(
        default=None,
        title="Name of Chemical Substance",
        description="Valid scientific name",
    )
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    alternateName: list[str] = Field(
        default_factory=list,
        title="Alternate Name",
        description="List of alternative names for this substance",
    )


class CellWall(ChemicalSubstance):
    """Cell Wall constituent - ChemSubstance + percent of CellWall."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    percent: Annotated[float, Field(ge=0, le=100)] | None = Field(
        default=None, title="Percent"
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def _check_values(self) -> Self:
        if check_not_completely_empty(self):
            return self
        raise ValueError("Wrong cell wall definition")


class FattyAcid(ChemicalSubstance):
    """Single Fatty Acid - used in Fatty Acid Profile."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    percent: Annotated[float, Field(ge=0, le=100)] | None = Field(
        default=None, title="Percent"
    )
    ecl: str | None = Field(default=None, title="ECL")

    @model_validator(mode="after")
    def _check_values(self) -> Self:
        if check_not_completely_empty(self):
            return self
        raise ValueError("Wrong fatty acid definition")


class Halophil(ChemicalSubstance):
    """Halophily abilities of a Strain."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )
    minimal: float | None = Field(
        default=None, title="Optimal", description="Single optimal growth value"
    )
    maximal: float | None = Field(
        default=None, title="Optimal", description="Single optimal growth value"
    )
    optimal: float | None = Field(
        default=None, title="Optimal", description="Single optimal growth value"
    )
    unit: ConcentrationUnit = Field(title="Unit", description="")

    tests: list[GrowthRange] = Field(
        default_factory=list,
        title="Tests",
        description="List of tests and if the strain grows in tested ranges",
    )

    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def _check_values(self) -> Self:
        if check_not_completely_empty(self):
            return self
        raise ValueError("Wrong halophil definition")


class Metabolite(ChemicalSubstance):
    """Information about tested Metabolites."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    tests: list[MetaboliteTest] = Field(
        default_factory=list,
        title="Tests",
        description="List of performed tests on this metabolite",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def _check_values(self) -> Self:
        if check_not_completely_empty(self):
            return self
        raise ValueError("Wrong metabolite definition")
