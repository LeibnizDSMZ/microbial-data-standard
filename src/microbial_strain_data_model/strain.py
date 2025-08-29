from pydantic import BaseModel, ConfigDict, Field


from microbial_strain_data_model.classes.application import Application
from microbial_strain_data_model.classes.biosafety import BioSafety
from microbial_strain_data_model.classes.chemicalsubstance import (
    CellWall,
    Halophil,
    Metabolite,
)
from microbial_strain_data_model.classes.cultivationmedia import CultivationMedia
from microbial_strain_data_model.classes.enzyme import Enzyme
from microbial_strain_data_model.classes.fattyacidprofile import FattyAcidProfile
from microbial_strain_data_model.classes.gccontent import GCContent
from microbial_strain_data_model.classes.growthcondition import GrowthCondition
from microbial_strain_data_model.classes.hemolysis import Hemolysis
from microbial_strain_data_model.classes.legal import Legal
from microbial_strain_data_model.classes.literature import Literature
from microbial_strain_data_model.classes.morphology import Morphology
from microbial_strain_data_model.classes.organization import Collection
from microbial_strain_data_model.classes.othermedia import OtherMedia
from microbial_strain_data_model.classes.pathogen import Pathogen
from microbial_strain_data_model.classes.identifier import IdentifierStrain
from microbial_strain_data_model.classes.origin import Origin
from microbial_strain_data_model.classes.relateddata import RelatedData
from microbial_strain_data_model.classes.sequence import Sequence
from microbial_strain_data_model.classes.source import Source
from microbial_strain_data_model.classes.spore import Spore
from microbial_strain_data_model.classes.staining import Staining
from microbial_strain_data_model.classes.taxon import TaxonWithSource, TypeStrain
from microbial_strain_data_model.classes.tolerance import Tolerance
from microbial_strain_data_model.classes.enums import (
    Morph,
    OrganismType,
)


class Strain(BaseModel):
    """Microbial Strain - main class of the new microbial strain data standard"""

    # single data points

    organismType: OrganismType = Field(title="Organism Type", description="", frozen=True)

    morphType: Morph | None = Field(
        default=None,
        title="Morph Type",
        description="Applicable and required for fungi only",
        frozen=True,
    )

    # lists of data objects

    typeStrain: list[TypeStrain] = Field(title="Type Strain", description="")

    taxon: list[TaxonWithSource] = Field(title="Taxon", description="")

    identifier: list[IdentifierStrain] = Field(
        default_factory=list, title="Identifier", description=""
    )

    origin: list[Origin] = Field(
        default_factory=list, title="Origin", description="Sample and isolation data"
    )

    legal: list[Legal] = Field(default_factory=list, title="Legal", description="")

    pathogenicity: list[Pathogen] = Field(
        default_factory=list, title="pathogenicity", description=""
    )

    bioSafety: list[BioSafety] = Field(
        default_factory=list, title="Bio Safety", description=""
    )

    morphology: list[Morphology] = Field(
        default_factory=list, title="Morphology", description="Morphology information"
    )

    wallConstituents: list[CellWall] = Field(
        default_factory=list,
        title="Wall Constituents",
        description="",
    )

    staining: list[Staining] = Field(
        default_factory=list, title="Stainings", description=""
    )

    sporeFormation: list[Spore] = Field(
        default_factory=list,
        title="Spore Formation",
        description="",
    )

    growthConditions: list[GrowthCondition] = Field(
        default_factory=list,
        title="Growth conditions",
        description="Temperature and pH values",
    )

    cultivationMedia: list[CultivationMedia] = Field(
        default_factory=list,
        title="Cultivation Media",
        description="",
    )

    sequences: list[Sequence] = Field(
        default_factory=list, title="Sequences", description=""
    )

    gcContent: list[GCContent] = Field(
        default_factory=list, title="GC Content", description=""
    )

    fattyAcidProfiles: list[FattyAcidProfile] = Field(
        default_factory=list,
        title="Fatty Acid Profile",
        description="",
    )

    hemolysis: list[Hemolysis] = Field(
        default_factory=list, title="Hemolysis", description=""
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

    literature: list[Literature] = Field(
        default_factory=list, title="Literature", description=""
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
        extra="allow",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )
