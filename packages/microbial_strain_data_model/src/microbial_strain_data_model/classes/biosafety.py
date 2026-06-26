# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from pydantic import BaseModel
from typing import Iterable
from microbial_strain_data_model.classes.root import ROOT_HOOK
from pydantic import ConfigDict, Field, HttpUrl
from microbial_strain_data_model.classes.links import SourceLink


class BioSafety(BaseModel):
    """Biosafety classification."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    riskgroup: str = Field(
        title="Riskgroup", description="In most cases a number system 1-4"
    )
    classification: str | None = Field(
        default=None,
        title="Classification",
        description="Classification Agency or Country, e.g. 'WHO' or "
        "'German classification'",
    )
    url: HttpUrl | None = Field(
        default=None,
        title="URL",
        description="Uniform Resource Locator of a resource on the Internet",
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
