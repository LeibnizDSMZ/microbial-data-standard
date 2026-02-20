from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_extra_types.country import CountryAlpha2

from microbial_strain_data_model.utils.functions import check_not_completely_empty


class Address(BaseModel):
    """Address object comparable to schema.org PostalAddress."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    addressCountry: str | None = Field(
        default=None, title="Country name", description="Name of the country"
    )
    addressCountryIso: CountryAlpha2 | None = Field(
        default=None,
        title="Country Iso",
        description="Country ISO code, see ISO 3166-1 alpha-2",
    )
    addressRegion: str | None = Field(
        default=None, title="Region", description="Region within the country"
    )
    addressLocality: str | None = Field(
        default=None, title="Locality", description="Locality within the region"
    )
    postOfficeBoxNumber: str | None = Field(default=None, title="Post Office Box Number")
    postalCode: str | None = Field(default=None, title="Postal Code")
    streetAddress: str | None = Field(
        default=None,
        title="Street Address",
        description="Name of the street and number within street",
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
