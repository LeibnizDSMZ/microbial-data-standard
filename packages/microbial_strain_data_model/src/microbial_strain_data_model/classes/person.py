# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from pydantic import HttpUrl
from pydantic import BaseModel, ConfigDict, Field
from microbial_strain_data_model.classes.identifier import Identifier

type _INDEX = tuple[str, *tuple[HttpUrl | str | None, ...]]


class Person(BaseModel):
    """Person."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(
        title="Name", description="Name of the person, preferable: `Last`, `First`"
    )
    identifier: list[Identifier] = Field(
        default_factory=list,
        title="Identifier",
        description="Person identifiers like ORCID",
    )

    def _index(self) -> _INDEX:
        return (
            self.name,
            *(ind for idi in self.identifier for ind in idi._index()),
        )
