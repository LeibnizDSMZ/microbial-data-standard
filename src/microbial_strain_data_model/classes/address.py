from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_extra_types.country import CountryAlpha2

from microbial_strain_data_model.utils.functions import check_not_completely_empty


class Address(BaseModel):
    """
    Address object comparable to schema.org PostalAddress
    """

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    addressCountry: CountryAlpha2 | None = Field(default=None, title="Country")
    addressLocality: str | None = Field(default=None, title="Locality")
    addressRegion: str | None = Field(default=None, title="Region")
    postOfficeBoxNumber: str | None = Field(default=None, title="Post Office Box Number")
    postalCode: str | None = Field(default=None, title="Post Code")
    streetAddress: str | None = Field(default=None, title="Street Address")

    _check_values = model_validator(mode="after")(check_not_completely_empty)
