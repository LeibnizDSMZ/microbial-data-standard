# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from pydantic import BaseModel
from typing import Iterable
from microbial_strain_data_model.classes.root import ROOT_HOOK
from pydantic import ConfigDict, Field

from microbial_strain_data_model.classes.enums import SequenceLevel, SequenceType
from microbial_strain_data_model.classes.identifier import Identifier
from microbial_strain_data_model.classes.links import SourceLink


class Sequence(BaseModel):
    """Information on a Sequence."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    type: SequenceType = Field(title="Type")
    level: SequenceLevel = Field(title="Level")
    accessionNumber: str = Field(title="Accession Number")
    description: str | None = Field(default=None, title="Description")
    length: str | None = Field(default=None, title="Length")
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    def _source(self) -> ROOT_HOOK:
        def _hook(nes: list[str]):
            self.source = nes

        return self.source, _hook

    def _related_data(self, /) -> Iterable[ROOT_HOOK]:
        return tuple()
