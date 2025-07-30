from pydantic_extra_types.pendulum_dt import Date
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


from microbial_strain_data_model.classes.application import Application
from microbial_strain_data_model.classes.biosafety import BioSafety
from microbial_strain_data_model.classes.cellshape import CellShape
from microbial_strain_data_model.classes.chemicalsubstance import (
    CellWall,
    Halophil,
    Metabolite,
)
from microbial_strain_data_model.classes.colony import Colony
from microbial_strain_data_model.classes.cultivationmedia import CultivationMedia
from microbial_strain_data_model.classes.enzyme import Enzyme
from microbial_strain_data_model.classes.fattyacidprofile import FattyAcidProfile
from microbial_strain_data_model.classes.gccontent import GCContent
from microbial_strain_data_model.classes.growthrange import Growth
from microbial_strain_data_model.classes.hemolysis import Hemolysis
from microbial_strain_data_model.classes.legal import Legal
from microbial_strain_data_model.classes.literature import Literature
from microbial_strain_data_model.classes.multicell import MultiCell
from microbial_strain_data_model.classes.organization import Collection
from microbial_strain_data_model.classes.othermedia import OtherMedia
from microbial_strain_data_model.classes.oxygenrelation import OxygenRelation
from microbial_strain_data_model.classes.pathogen import Pathogen
from microbial_strain_data_model.classes.person import ConnectedPerson
from microbial_strain_data_model.classes.identifier import IdentifierStrain
from microbial_strain_data_model.classes.isolation import Isolation
from microbial_strain_data_model.classes.motility import Motility
from microbial_strain_data_model.classes.relateddata import RelatedData
from microbial_strain_data_model.classes.sample import Sample
from microbial_strain_data_model.classes.sequence import Sequence
from microbial_strain_data_model.classes.size import CellSize
from microbial_strain_data_model.classes.source import Source
from microbial_strain_data_model.classes.spore import Spore
from microbial_strain_data_model.classes.staining import Staining
from microbial_strain_data_model.classes.taxon import Taxon, TaxonWithSource, TypeStrain
from microbial_strain_data_model.classes.tolerance import Tolerance
from microbial_strain_data_model.classes.enums import (
    CelsiusUnit,
    Morph,
    OrganismType,
    PHUnit,
)


class Microbe(BaseModel):
    """Microbe - main class of the new microbial data standard"""

    version: Literal["0.6"]

    creation_date: Date = Field(default_factory=Date.today)

    # single data points

    organismType: OrganismType = Field(title="Organism Type", description="", frozen=True)

    morphType: Morph | None = Field(
        default=None,
        title="Morph Type",
        description="Applicable and required for fungi only",
        frozen=True,
    )

    unifiedTypeStrain: bool | None = Field(
        default=None,
        title="Unified Type Strain",
        description="Is this strain type for unified species",
        frozen=True,
    )

    unifiedTaxon: Taxon | None = Field(
        default=None,
        title="Unified Taxon",
        description="Evaluated and updated taxonomy",
    )

    # lists of data objects

    typeStrain: list[TypeStrain] = Field(title="Type Strain", description="")

    taxon: list[TaxonWithSource] = Field(title="Taxon", description="")

    sample: list[Sample] = Field(default_factory=list, title="Sample", description="")

    isolation: list[Isolation] = Field(
        default_factory=list, title="Isolation", description=""
    )

    legal: list[Legal] = Field(default_factory=list, title="Legal", description="")

    cellShape: list[CellShape] = Field(
        default_factory=list, title="Cell Shape", description=""
    )

    oxygenRelation: list[OxygenRelation] = Field(
        default_factory=list,
        title="Oxygen Relation",
        description="",
    )

    multiCellComplexForming: list[MultiCell] = Field(
        default_factory=list,
        title="Multi Cell Complex Forming",
        description="",
    )

    cellSize: list[CellSize] = Field(
        default_factory=list, title="Cell Size", description=""
    )

    motility: list[Motility] = Field(
        default_factory=list, title="Motility", description=""
    )

    colony: list[Colony] = Field(default_factory=list, title="Colony", description="")

    sporeFormation: list[Spore] = Field(
        default_factory=list,
        title="Spore Formation",
        description="",
    )

    temperature: list[Growth[CelsiusUnit]] = Field(
        default_factory=list, title="Temperature", description=""
    )

    ph: list[Growth[PHUnit]] = Field(default_factory=list, title="pH", description="")

    identifier: list[IdentifierStrain] = Field(
        default_factory=list, title="Identifier", description=""
    )

    connectedPersons: list[ConnectedPerson] = Field(
        default_factory=list,
        title="Connected Persons",
        description="",
    )

    pathogenicity: list[Pathogen] = Field(
        default_factory=list, title="pathogenicity", description=""
    )

    bioSafety: list[BioSafety] = Field(
        default_factory=list, title="Bio Safety", description=""
    )

    sequences: list[Sequence] = Field(
        default_factory=list, title="Sequences", description=""
    )

    gcContent: list[GCContent] = Field(
        default_factory=list, title="GC Content", description=""
    )

    literature: list[Literature] = Field(
        default_factory=list, title="Literature", description=""
    )

    wallConstituents: list[CellWall] = Field(
        default_factory=list,
        title="Wall Constituents",
        description="",
    )

    fattyAcidProfiles: list[FattyAcidProfile] = Field(
        default_factory=list,
        title="Fatty Acid Profile",
        description="",
    )

    staining: list[Staining] = Field(
        default_factory=list, title="Stainings", description=""
    )

    hemolysis: list[Hemolysis] = Field(
        default_factory=list, title="Hemolysis", description=""
    )

    cultivationMedia: list[CultivationMedia] = Field(
        default_factory=list,
        title="Cultivation Media",
        description="",
    )

    halophily: list[Halophil] = Field(
        default_factory=list, title="Halophily", description=""
    )

    tolerances: list[Tolerance] = Field(
        default_factory=list, title="Tolerances", description=""
    )

    enzymes: list[Enzyme] = Field(default_factory=list, title="Enzymes", description="")
    metabolites: list[Metabolite] = Field(
        default_factory=list, title="Metabolites", description=""
    )

    knownApplications: list[Application] = Field(
        default_factory=list,
        title="Known Applications",
        description="",
    )

    collections: list[Collection] = Field(
        default_factory=list, title="Collections", description=""
    )

    otherMedia: list[OtherMedia] = Field(
        default_factory=list, title="Other Media", description=""
    )

    relatedData: list[RelatedData] = Field(
        default_factory=list, title="Related Data", description=""
    )

    sources: list[Source] = Field(title="Sources", description="")

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )
