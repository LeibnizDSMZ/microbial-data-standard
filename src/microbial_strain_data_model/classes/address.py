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

    country: CountryAlpha2 | None = Field(title="Country", alias="addressCountry")
    locality: str | None = Field(default=None, title="Locality", alias="addressLocality")
    region: str | None = Field(default=None, title="Region", alias="addressRegion")
    post_office_box_number: str | None = Field(
        default=None, title="Post Office Box Number", alias="postOfficeBoxNumber"
    )
    postal_code: str | None = Field(default=None, title="Post Code", alias="postalCode")
    street_address: str | None = Field(
        default=None, title="Street Address", alias="streetAddress"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
