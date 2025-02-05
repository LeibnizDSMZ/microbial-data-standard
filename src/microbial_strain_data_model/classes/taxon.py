from typing import Self

from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import TaxonRank, TaxonStatus
from microbial_strain_data_model.classes.identifier import Identifier

from microbial_strain_data_model.classes.sourcestring import SourceString


class TypeStrain(BaseModel):
    """Information if a strain is the type strain of its species"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    type_strain: bool = Field(title="Type Strain", alias="typeStrain")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )


class ScientificName(BaseModel):
    """Scientific name"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", alias="name")
    author: str = Field(title="Author", alias="author")


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

    name: str = Field(title="Name", alias="name")
    rank: TaxonRank = Field(title="Taxon Rank", alias="taxonRank")
    status: TaxonStatus = Field(title="Taxon Status", alias="taxonStatus")
    identifier: list[Identifier] = Field(
        default_factory=list, title="Identifier", alias="identifier"
    )
    scientific: ScientificName | None = Field(
        default=None, title="Scientific Name", alias="scientificName"
    )
    alternate_name: list[str] = Field(
        default_factory=list, title="Alternate Name", alias="alternateName"
    )
    parent: Self | None = Field(default=None, title="Parent Taxon", alias="parentTaxon")
    same_as: list[str] = Field(default_factory=list, title="Same As", alias="sameAs")


class TaxonWithSource(Taxon):
    """Taxon class with source information"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )
    # overwriting the 'parent' field inherited by Taxon
    parent: Taxon | None = Field(default=None, title="Parent Taxon", alias="parentTaxon")  # type: ignore

    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
