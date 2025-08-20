from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.links import SourceLink


class Identifier(BaseModel):
    """Identifier of every Kind, compare to schema.org PropertyValue class"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", description="Name of the identifier")
    value: str = Field(
        title="Value", description="Value of the identifier (can also be a URL)"
    )
    propertyID: str | None = Field(
        default=None, title="Property ID", description="See schema.org/propertyID"
    )
    url: HttpUrl | None = Field(
        default=None,
        title="URL",
        description="Uniform Resource Locator of a resource on the Internet",
    )
    logo: HttpUrl | None = Field(
        default=None,
        title="Logo",
        description="Logo of the Identifier Organization (e.g. DOI, ORCID, ROR, ...)",
    )


class IdentifierStrain(Identifier):

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
