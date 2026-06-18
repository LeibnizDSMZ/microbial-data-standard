# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.shared.data_con.isolation_sources_tree import (
    create_iso_src_root,
)
from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, Field, model_validator
from anytree.resolver import Resolver, ChildResolverError


class IsolationTag(BaseModel):
    """Isolation tag system, original used by BacDive."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    level1: str = Field(title="Level 1")
    level2: str | None = Field(default=None, title="Level 2")
    level3: str | None = Field(default=None, title="Level 3")

    @model_validator(mode="after")
    def _check_isolation_tag(self) -> Self:
        resolver = Resolver("name")
        path = "" + self.level1
        for x in [self.level2, self.level3]:
            if isinstance(x, str):
                path += "|"
                path += x
        try:
            resolver.get(create_iso_src_root(), path)
        except ChildResolverError as e:
            raise ValueError from ValueError(
                f"Isolation Source Tags are not valid isolation tag path: {e}"
            )
        return self
