from typing_extensions import Annotated
from microbial_strain_data_model.classes.enums import ConcentrationUnit
from microbial_strain_data_model.classes.metabolitetest import MetaboliteTest
from microbial_strain_data_model.utils.functions import check_not_completely_empty

from pydantic import BaseModel, ConfigDict, Field, model_validator, StringConstraints

from microbial_strain_data_model.classes.growrange import Growth
from microbial_strain_data_model.classes.identifier import Identifier


class ChemicalSubstance(BaseModel):
    """Chemical Substance base class"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str | None = Field(
        default=None, title="Name of Chemical Substance", alias="name"
    )
    identifier: list[Identifier] = Field(
        default_factory=list, title="Identifier", alias="identifier"
    )
    alternate_name: list[str] = Field(
        default_factory=list, title="Alternate Name", alias="alternateName"
    )

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
        default=None, title="Percent", alias="percent"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
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
        default=None, title="Percent", alias="percent"
    )
    ecl: str | None = Field(default=None, title="ECL", alias="ecl")


class Halophil(Growth[ConcentrationUnit], ChemicalSubstance):
    """Halophily abilities of a Strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )


class Metabolite(ChemicalSubstance):
    """Information about tested Metabolites"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    tests: list[MetaboliteTest] = Field(
        default_factory=list, title="Tests", alias="tests"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
