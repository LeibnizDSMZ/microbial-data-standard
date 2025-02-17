from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, EmailStr, StringConstraints
from microbial_strain_data_model.classes.address import Address
from microbial_strain_data_model.classes.enums import PersonRole, Restriction, SupplyForm
from microbial_strain_data_model.classes.identifier import Identifier

from microbial_strain_data_model.classes.sourcestring import SourceString


class Person(BaseModel):
    """Person - also Basis for every Individual Entity (e.g. Organization)"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name")
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")


class ConnectedPerson(Person):
    """Connected Person = Person + Role"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    role: PersonRole | None = Field(default=None, title="Role")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )


class Organization(BaseModel):
    """Individual Entity of a Organization"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name")
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    legalName: str | None = Field(default=None, title="Legal Name")
    address: Address | None = Field(default=None, title="Address")
    url: HttpUrl | None = Field(default=None, title="URL")
    email: EmailStr | None = Field(default=None, title="Email")


class Collection(Organization):
    """Information about one culture collection"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    resourceNumber: str = Field(title="Resource Number")
    available: bool | None = Field(default=None, title="Availability")
    catalogUrl: HttpUrl | None = Field(default=None, title="Catalog URL")
    restrictionsOnUse: Restriction | None = Field(
        default=None, title="Restrictions On Use"
    )
    axenicCulture: bool | None = Field(default=None, title="Axenic Culture")
    supplyForms: list[SupplyForm] = Field(default_factory=list, title="Supply Forms")
    history: str | None = Field(default=None, title="History")
    depositionDate: (
        Annotated[
            str,
            StringConstraints(
                strip_whitespace=True,
                to_upper=True,
                pattern=r"^(?:\d{4}[-\._]?\d{0,2}[-\._]?\d{0,2})?/?(?:\d{4}[-\._]?\d{0,2}[-\._]?\d{0,2})?$",
            ),
        ]
        | None
    ) = Field(default=None, title="Deposition Date")
    depositor: Person | None = Field(default=None, title="Depositor")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
