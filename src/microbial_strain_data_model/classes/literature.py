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

    name: str | None = Field(default=None, title="Name", alias="name")
    url: HttpUrl | None = Field(default=None, title="URL", alias="url")
    date: Date | None = Field(default=None, title="Date Published", alias="datePublished")
    author: list[Person] = Field(default_factory=list, title="Author", alias="author")
    publisher: list[Organization] = Field(
        default_factory=list, title="Publisher", alias="publisher"
    )
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def check_if_name_or_url_is_set(self) -> Self:
        if not self.name and not self.url:
            raise ValueError("name or url is needed")
        return self
