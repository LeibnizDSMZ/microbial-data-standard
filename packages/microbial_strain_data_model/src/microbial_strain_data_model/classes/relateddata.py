# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.classes.root import ROOT_HOOK
from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.links import SourceLink


class RelatedData(BaseModel):
    """RelatedData."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    relation: str = Field(
        title="Relation",
        description="The kind or type of relation of the data points, e.g. "
        "growthCondition, testCondition, API20",
    )
    source: SourceLink = Field(title="Source", description="JSON path to source object")

    def index(self) -> tuple[str, str]:
        return self.relation, self.source

    def _source(self) -> ROOT_HOOK:
        def _hook(nes: list[str]):
            self.source, *_ = nes

        return (self.source,), _hook
