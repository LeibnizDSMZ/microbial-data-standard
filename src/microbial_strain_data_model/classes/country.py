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
        title="Country Name (ISO 2 Letter Code)", alias="name"
    )
    identifier: list[Identifier] = Field(
        default_factory=list, title="Identifier", alias="identifier"
    )
    cbd_party: bool | None = Field(
        default=None,
        title="Is Convention Of Biological Diversity Party",
        alias="conventionOfBiologicalDiversityParty",
    )
    cartagena_party: bool | None = Field(
        default=None, title="Is Cartagena Protocol Party", alias="cartagenaProtocolParty"
    )
    nagoya_party: bool | None = Field(
        default=None, title="Is Nagoya Protocol Party", alias="nagoyaProtocolParty"
    )
    kuala_lumpur_party: bool | None = Field(
        default=None, title="Is Nagoya Kuala Lumpur Party", alias="nagoyaKualaLumpurParty"
    )
