from typing_extensions import Self
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    model_validator,
)
from pydantic_extra_types.pendulum_dt import Date

from microbial_strain_data_model.classes.organization import Organization
from microbial_strain_data_model.classes.person import Person
from microbial_strain_data_model.classes.links import SourceLink


class LiteratureSource(BaseModel):
    """Literature used in Source."""

    name: str | None = Field(default=None, title="Name")
    url: HttpUrl | None = Field(default=None, title="URL")
    datePublished: Date | None = Field(default=None, title="Date Published")
    author: list[Person] = Field(default_factory=list, title="Author")
    publisher: list[Organization] = Field(default_factory=list, title="Publisher")

    @model_validator(mode="after")
    def check_if_name_or_url_is_set(self) -> Self:
        if not self.name and not self.url:
            raise ValueError("name or url is needed")
        return self


class Literature(LiteratureSource):
    """Connected Literature."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
