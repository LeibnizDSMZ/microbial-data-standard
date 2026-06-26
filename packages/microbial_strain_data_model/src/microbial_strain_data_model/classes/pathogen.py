# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.classes.root import ROOT_HOOK
from typing import Iterable
from pydantic import BaseModel, ConfigDict, HttpUrl, Field

from microbial_strain_data_model.classes.enums import Host, PathogenLevel

from microbial_strain_data_model.classes.links import SourceLink


class Pathogen(BaseModel):
    """Pathogen, defining Host, pathogenicity and under what classification."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    host: Host = Field(
        title="Host",
        description="Organism or group of organisms that can be infected",
    )
    pathogen: PathogenLevel = Field(
        title="Pathogen",
        description="Frequency of pathogenicity: no pathogen, opportunistic or obligate",
    )
    classification: str | None = Field(
        default=None,
        title="Classification",
        description="Type of classification, e.g. German classification "
        "or WHO classification",
    )
    url: HttpUrl | None = Field(
        default=None, title="URL", description="Link to classification document"
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    def _source(self) -> ROOT_HOOK:
        def _hook(nes: list[str]):
            self.source = nes

        return self.source, _hook

    def _related_data(self, /) -> Iterable[ROOT_HOOK]:
        return tuple()
