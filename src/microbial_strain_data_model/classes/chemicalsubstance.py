from typing_extensions import Annotated
from microbial_strain_data_model.classes.enums import ConcentrationUnit
from microbial_strain_data_model.classes.metabolitetest import MetaboliteTest
from microbial_strain_data_model.utils.functions import check_not_completely_empty

from pydantic import BaseModel, ConfigDict, Field, model_validator

from microbial_strain_data_model.classes.growrange import Growth
from microbial_strain_data_model.classes.identifier import Identifier

from microbial_strain_data_model.classes.sourcestring import SourceString


class ChemicalSubstance(BaseModel):
    """Chemical Substance base class"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str | None = Field(default=None, title="Name of Chemical Substance")
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    alternateName: list[str] = Field(default_factory=list, title="Alternate Name")

    _check_values = model_validator(mode="after")(check_not_completely_empty)


class CellWall(ChemicalSubstance):
    """Cell Wall constituent - ChemSubstance + percent of CellWall"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    percent: Annotated[float, Field(ge=0, le=100)] | None = Field(
        default=None, title="Percent"
    )
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )


class FattyAcid(ChemicalSubstance):
    """Single Fatty Acid - used in Fatty Acid Profile"""

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


class Halophil(Growth[ConcentrationUnit], ChemicalSubstance):
    """Halophily abilities of a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )


class Metabolite(ChemicalSubstance):
    """Information about tested Metabolites"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    tests: list[MetaboliteTest] = Field(default_factory=list, title="Tests")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
