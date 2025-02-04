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

    name: str = Field(title="Name", alias="name")
    identifier: list[Identifier] = Field(
        default_factory=list, title="Identifier", alias="identifier"
    )


class ConnectedPerson(Person):
    """Connected Person = Person + Role"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    role: PersonRole | None = Field(default=None, title="Role", alias="role")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )


class Organization(BaseModel):
    """Individual Entity of a Organization"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", alias="name")
    identifier: list[Identifier] = Field(
        default_factory=list, title="Identifier", alias="identifier"
    )
    legal_name: str | None = Field(default=None, title="Legal Name", alias="legalName")
    address: Address | None = Field(default=None, title="Address", alias="address")
    url: HttpUrl | None = Field(default=None, title="URL", alias="url")
    email: EmailStr | None = Field(default=None, title="Email", alias="email")


class Collection(Organization):
    """Information about one culture collection"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    resource_num: str = Field(title="Resource Number", alias="resourceNumber")
    available: bool | None = Field(
        default=None, title="Availability", alias="availability"
    )
    catalog_link: HttpUrl | None = Field(
        default=None, title="Catalog URL", alias="catalogUrl"
    )
    restrictions: Restriction | None = Field(
        default=None, title="Restrictions On Use", alias="restrictionsOnUse"
    )
    axenic: bool | None = Field(
        default=None, title="Axenic Culture", alias="axenicCulture"
    )
    supply_forms: list[SupplyForm] = Field(
        default_factory=list, title="Supply Forms", alias="supplyForms"
    )
    history: str | None = Field(default=None, title="History", alias="history")
    date: (
        Annotated[
            str,
            StringConstraints(
                strip_whitespace=True,
                to_upper=True,
                pattern=r"^(?:\d{4}[-\._]?\d{0,2}[-\._]?\d{0,2})?/?(?:\d{4}[-\._]?\d{0,2}[-\._]?\d{0,2})?$",
            ),
        ]
        | None
    ) = Field(default=None, title="Deposition Date", alias="depositionDate")
    depositor: Person | None = Field(default=None, title="Depositor", alias="depositor")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
