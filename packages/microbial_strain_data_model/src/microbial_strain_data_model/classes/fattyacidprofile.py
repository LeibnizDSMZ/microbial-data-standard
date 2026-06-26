# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from pydantic import BaseModel
from typing import Iterable
from microbial_strain_data_model.classes.root import ROOT_HOOK
from typing import Self
from pydantic import ConfigDict, Field, model_validator

from microbial_strain_data_model.classes.chemicalsubstance import FattyAcid
from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class FattyAcidProfile(BaseModel):
    """Full Fatty Acid Profile."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    profile: list[FattyAcid] = Field(
        default_factory=list,
        title="Profile",
        description="List of fatty acids and their percentages",
    )
    library: str | None = Field(
        default=None, title="Library", description="The used library"
    )
    software: str | None = Field(
        default=None, title="Software", description="The used software"
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    @model_validator(mode="after")
    def _ensure_list_not_empty(self) -> Self:
        if len(self.profile) < 1:
            raise ValueError("Fatty Acis Profile must contain at least one Fatty Acid")
        return self

    def _source(self) -> ROOT_HOOK:
        def _hook(nes: list[str]):
            self.source = nes

        return self.source, _hook

    def _related_data(self, /) -> Iterable[ROOT_HOOK]:
        def _hook(ner: list[str]):
            self.relatedData = ner

        return ((self.relatedData, _hook),)
