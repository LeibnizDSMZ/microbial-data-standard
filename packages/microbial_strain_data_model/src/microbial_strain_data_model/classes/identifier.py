# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.classes.root import ROOT_HOOK
from typing import Iterable
from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.links import SourceLink

type _INDEX = tuple[str, str, str | None, HttpUrl | None, HttpUrl | None]


class Identifier(BaseModel):
    """Identifier of every Kind, compare to schema.org PropertyValue class."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", description="Name of the identifier")
    value: str = Field(
        title="Value", description="Value of the identifier (can also be a URL)"
    )
    propertyID: str | None = Field(
        default=None, title="Property ID", description="See schema.org/propertyID"
    )
    url: HttpUrl | None = Field(
        default=None,
        title="URL",
        description="Uniform Resource Locator of a resource on the Internet",
    )
    logo: HttpUrl | None = Field(
        default=None,
        title="Logo",
        description="Logo of the Identifier Organization (e.g. DOI, ORCID, ROR, ...)",
    )

    def _index(self) -> _INDEX:
        return (self.name, self.value, self.propertyID, self.url, self.logo)


class IdentifierStrain(Identifier):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
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
