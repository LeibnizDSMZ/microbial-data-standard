from typing import Self

from pydantic import BaseModel, Field

from microbial_strain_data_model.classes.enums import TaxonRank, TaxonStatus
from microbial_strain_data_model.classes.identifier import Identifier


class ScientificName(BaseModel):
    name: str = Field(title="Name", alias="name")
    author: str = Field(title="Author", alias="author")


class Taxon(BaseModel):
    """
    A class to take all information about a taxon for the new microbial data standard.
    """

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
