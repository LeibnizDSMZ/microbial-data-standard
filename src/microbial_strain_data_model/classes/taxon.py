from typing import Self

from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import TaxonRank, TaxonStatus
from microbial_strain_data_model.classes.identifier import Identifier

from microbial_strain_data_model.classes.sourcestring import SourceLink


class TypeStrain(BaseModel):
    """Information if a strain is the type strain of its species"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    typeStrain: bool = Field(title="Type Strain")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )


class ScientificName(BaseModel):
    """Scientific name"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name")
    author: str = Field(title="Author")


class Taxon(BaseModel):
    """
    A class to take all information about a taxon for the new microbial data standard.
    """

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name")
    taxonRank: TaxonRank = Field(title="Taxon Rank")
    taxonStatus: TaxonStatus = Field(title="Taxon Status")
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    scientificName: ScientificName | None = Field(default=None, title="Scientific Name")
    alternateName: list[str] = Field(default_factory=list, title="Alternate Name")
    parentTaxon: Self | None = Field(default=None, title="Parent Taxon")
    sameAs: list[str] = Field(default_factory=list, title="Same As")


class TaxonWithSource(Taxon):
    """Taxon class with source information"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )
    # overwriting the 'parent' field inherited by Taxon
    parentTaxon: Taxon | None = Field(default=None, title="Parent Taxon")  # type: ignore

    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
