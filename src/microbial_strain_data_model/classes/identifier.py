from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.sourcestring import SourceString


class Identifier(BaseModel):
    """Identifier of every Kind, compare to schema.org PropertyValue class"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name")
    value: str = Field(title="Value")
    propertyID: str | None = Field(default=None, title="Property ID")
    url: HttpUrl | None = Field(default=None, title="URL")


class IdentifierStrain(Identifier):

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
