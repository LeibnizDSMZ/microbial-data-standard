from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, EmailStr, StringConstraints
from microbial_strain_data_model.classes.address import Address
from microbial_strain_data_model.classes.enums import PersonRole, Restriction, SupplyForm
from microbial_strain_data_model.classes.identifier import Identifier

from microbial_strain_data_model.classes.sourcestring import SourceString


class Person(BaseModel):
    """Person"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", description="Name of the person")
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

    name: str = Field(title="Name", description="Short name of the organization")
    identifier: list[Identifier] = Field(
        default_factory=list,
        title="Identifier",
        description="Identifiers of the organization, e.g. ROR",
    )
    legalName: str | None = Field(
        default=None,
        title="Legal Name",
        description="Full legal name of the organization",
    )
    address: Address | None = Field(
        default=None, title="Address", description="Address of the organization"
    )
    url: HttpUrl | None = Field(default=None, title="URL", description="Link to homepage")
    email: EmailStr | None = Field(
        default=None, title="Email", description="Contact email"
    )
    logo: HttpUrl | None = Field(default=None, title="Logo", description="Link to logo")


class Collection(Organization):
    """Information about one culture collection"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    resourceNumber: str = Field(
        title="Resource Number", description="The CCNO of the strain at this collection"
    )
    available: bool | None = Field(
        default=None,
        title="Availability",
        description="Is the strain in the current catalog",
    )
    catalogUrl: HttpUrl | None = Field(
        default=None, title="Catalog URL", description="Link to catalog"
    )
    restrictionsOnUse: Restriction | None = Field(
        default=None,
        title="Restrictions On Use",
        description="Restrictions of use by the collection",
    )
    policyUrl: HttpUrl | None = Field(
        default=None, title="Policy URL", description="Link to collections policy"
    )
    axenicCulture: bool | None = Field(
        default=None,
        title="Axenic Culture",
        description="Is the culture pure or mixed with other microbes",
    )
    supplyForms: list[SupplyForm] = Field(
        default_factory=list,
        title="Supply Forms",
        description="How the strain are available",
    )
    history: str | None = Field(
        default=None, title="History", description="Exchange history of the strain"
    )
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
    ) = Field(
        default=None,
        title="Deposition Date",
        description="Date of deposition at this collection",
    )
    depositor: Person | None = Field(
        default=None,
        title="Depositor",
        description="Person who deposited the strain at this collection",
    )
    depositedAs: str | None = Field(
        default=None,
        title="Deposited as",
        description="The CCNO or designation before deposition",
    )
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
