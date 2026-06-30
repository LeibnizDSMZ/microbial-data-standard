# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.shared.data_ops.cast import to_string
from typing import Self
from pydantic.fields import PrivateAttr
from pydantic_extra_types.country import CountryAlpha2
from pydantic import EmailStr
from pydantic_extra_types.pendulum_dt import Date
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator

from microbial_strain_data_model.classes.enums import CurationMode, SourceType
from microbial_strain_data_model.classes.identifier import Identifier
from microbial_strain_data_model.classes.organization import Organization
from microbial_strain_data_model.classes.person import Person

type _INDEX = tuple[str | None | EmailStr | CountryAlpha2, ...]


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

    _ca_index: _INDEX | None = PrivateAttr(default=None)

    @model_validator(mode="after")
    def _check_if_name_or_url_is_set(self) -> Self:
        if not self.name and not self.url:
            raise ValueError("name or url is needed")
        return self

    def _index(self) -> _INDEX:
        if self._ca_index is None:
            self._ca_index = (
                self.sourceType.value,
                self.mode.value,
                self.name,
                to_string(self.url),
                to_string(self.datePublished, lambda dat: dat.to_date_string()),
                to_string(self.dateRecorded, lambda dat: dat.to_date_string()),
                to_string(self.lastUpdate, lambda dat: dat.to_date_string()),
                *(ind for idi in self.identifier for ind in idi._index()),
                *(ind for aut in self.author for ind in aut._index()),
                *(ind for org in self.publisher for ind in org._index()),
            )
        return self._ca_index
