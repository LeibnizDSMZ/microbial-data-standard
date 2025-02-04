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

    name: str = Field(title="Name", alias="name")
    value: str = Field(title="Value", alias="value")
    property: str | None = Field(default=None, title="Property ID", alias="propertyID")
    url: HttpUrl | None = Field(default=None, title="URL", alias="url")


class IdentifierStrain(Identifier):

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
