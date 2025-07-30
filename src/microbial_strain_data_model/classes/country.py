from pydantic import BaseModel, ConfigDict, Field
from pydantic_extra_types.country import CountryAlpha2
from microbial_strain_data_model.classes.enums import (
    CountryHistoricalAlpha2,
    CountryOtherCodes,
)
from microbial_strain_data_model.classes.identifier import Identifier


class Country(BaseModel):
    """Country information, mostly on nagoya protocol"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: CountryAlpha2 | CountryHistoricalAlpha2 | CountryOtherCodes = Field(
        title="Country name", description="Country code, see ISO 3166-1 alpha-2"
    )
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    conventionOfBiologicalDiversityParty: bool | None = Field(
        default=None, title="Is Convention Of Biological Diversity Party"
    )
    cartagenaProtocolParty: bool | None = Field(
        default=None, title="Is Cartagena Protocol Party"
    )
    nagoyaProtocolParty: bool | None = Field(
        default=None, title="Is Nagoya Protocol Party"
    )
    nagoyaKualaLumpurParty: bool | None = Field(
        default=None, title="Is Nagoya Kuala Lumpur Party"
    )
