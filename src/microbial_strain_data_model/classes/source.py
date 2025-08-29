from pydantic_extra_types.pendulum_dt import Date
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator
from typing_extensions import Self

from microbial_strain_data_model.classes.enums import CurationMode, SourceType
from microbial_strain_data_model.classes.identifier import Identifier
from microbial_strain_data_model.classes.organization import Organization
from microbial_strain_data_model.classes.person import Person


class Source(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    sourceType: SourceType = Field(
        title="SourceType", description="Source Type", strict=False
    )
    mode: CurationMode = Field(title="Mode", description="Mode of curation", strict=False)
    name: str | None = Field(default=None, title="Name")
    url: HttpUrl | None = Field(default=None, title="URL")
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    datePublished: Date | None = Field(default=None, title="Date Published", strict=False)
    dateRecorded: Date = Field(
        default_factory=Date.today, title="Date Recorded", strict=False
    )
    lastUpdate: Date | None = Field(
        default=None, title="Date of last update", strict=False
    )
    author: list[Person] = Field(default_factory=list, title="Author")
    publisher: list[Organization] = Field(default_factory=list, title="Publisher")

    @model_validator(mode="after")
    def check_if_name_or_url_is_set(self) -> Self:
        if not self.name and not self.url:
            raise ValueError("name or url is needed")
        return self
