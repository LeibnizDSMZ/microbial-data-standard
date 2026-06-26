# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from pydantic import BaseModel
from typing import Iterable
from microbial_strain_data_model.classes.root import ROOT_HOOK
from typing_extensions import Annotated
from pydantic import ConfigDict, Field

from microbial_strain_data_model.classes.enums import GCMethod
from microbial_strain_data_model.classes.links import SourceLink


class GCContent(BaseModel):
    """GC content of the microorganism."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    method: GCMethod | None = Field(
        default=None,
        title="Method",
        description="Name of the method used to measure the GC content",
    )
    noteMethod: str | None = Field(
        default=None, title="Note Method", description="Note about the used method"
    )
    value: Annotated[float, Field(ge=0, le=100)] = Field(
        title="Percent Value",
        description="Percent value of how much percent of the DNA is GC pairs",
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
