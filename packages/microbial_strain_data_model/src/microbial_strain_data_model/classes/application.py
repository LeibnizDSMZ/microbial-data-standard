# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing import Iterable
from microbial_strain_data_model.classes.root import ROOT_HOOK
from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.links import SourceLink


class Application(BaseModel):
    """Application of the strain."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    application: str = Field(
        title="Application", description="Name of the application or patent"
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
