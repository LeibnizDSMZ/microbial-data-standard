from typing_extensions import Self
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    model_validator,
)
from pydantic_extra_types.pendulum_dt import Date

from microbial_strain_data_model.classes.actors import Organization, Person
from microbial_strain_data_model.classes.sourcestring import SourceString


class Literature(BaseModel):
    """Connected Literature information"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str | None = Field(default=None, title="Name")
    url: HttpUrl | None = Field(default=None, title="URL")
    datePublished: Date | None = Field(default=None, title="Date Published")
    author: list[Person] = Field(default_factory=list, title="Author")
    publisher: list[Organization] = Field(default_factory=list, title="Publisher")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def check_if_name_or_url_is_set(self) -> Self:
        if not self.name and not self.url:
            raise ValueError("name or url is needed")
        return self
