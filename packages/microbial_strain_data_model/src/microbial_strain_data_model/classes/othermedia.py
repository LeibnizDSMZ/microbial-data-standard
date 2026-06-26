# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing import Iterable
from microbial_strain_data_model.classes.root import ROOT_HOOK
from microbial_strain_data_model.shared.verify.empty import check_not_completely_empty
from typing import Self
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    model_validator,
)
from microbial_strain_data_model.classes.links import SourceLink


class OtherMedia(BaseModel):
    """A Media object e.g. Photo, Video, Document, etc."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    url: HttpUrl | None = Field(default=None, title="URL", description="Link to medium")
    name: str | None = Field(default=None, title="Name")
    description: str | None = Field(
        default=None,
        title="Description",
        description="Description of the medium and the content in the medium",
    )
    usageInfo: str | None = Field(
        default=None,
        title="Usage Information",
        description="License or other information on usage",
    )
    additionalType: str | None = Field(default=None, title="Additional Type")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def _check_values(self) -> Self:
        if check_not_completely_empty(self):
            return self
        raise ValueError("Wrong other media")

    def _source(self) -> ROOT_HOOK:
        def _hook(nes: list[str]):
            self.source = nes

        return self.source, _hook

    def _related_data(self, /) -> Iterable[ROOT_HOOK]:
        return tuple()
