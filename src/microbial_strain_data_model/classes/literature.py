from typing_extensions import Annotated, Self
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    model_validator,
)
from pydantic_extra_types.pendulum_dt import Date

from microbial_strain_data_model.classes.actors import Organization, Person


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
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )

    @model_validator(mode="after")
    def check_if_name_or_url_is_set(self) -> Self:
        if not self.name and not self.url:
            raise ValueError("name or url is needed")
        return self
