# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from pydantic import BaseModel
from typing import Iterable
from microbial_strain_data_model.classes.root import ROOT_HOOK
from pydantic import ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class CultivationMedia(BaseModel):
    """Cultivation media, use links to Media Dive or other resources."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name")
    url: HttpUrl | None = Field(default=None, title="URL")
    reagentUsed: list[str] = Field(default_factory=list, title="Reagent Used")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )

    def _source(self) -> ROOT_HOOK:
        def _hook(nes: list[str]):
            self.source = nes

        return self.source, _hook

    def _related_data(self, /) -> Iterable[ROOT_HOOK]:
        def _hook(ner: list[str]):
            self.relatedData = ner

        return ((self.relatedData, _hook),)
