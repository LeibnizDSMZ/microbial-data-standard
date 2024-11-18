from pydantic import BaseModel, ConfigDict, Field
from pydantic_extra_types.pendulum_dt import DateTime


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
from microbial_strain_data_model.classes.growrange import Growth
from microbial_strain_data_model.classes.hemolysis import Hemolysis
from microbial_strain_data_model.classes.legal import Legal
from microbial_strain_data_model.classes.literature import Literature
from microbial_strain_data_model.classes.multicell import MultiCell
from microbial_strain_data_model.classes.othermedia import OtherMedia
from microbial_strain_data_model.classes.oxygenrelation import OxygenRelation
from microbial_strain_data_model.classes.pathogen import Pathogen
from microbial_strain_data_model.classes.actors import (
    Collection,
    ConnectedPerson,
    Organization,
    Person,
)
from microbial_strain_data_model.classes.identifier import IdentifierStrain
from microbial_strain_data_model.classes.isolation import Isolation
from microbial_strain_data_model.classes.motility import Motility
from microbial_strain_data_model.classes.sample import Sample
from microbial_strain_data_model.classes.sequence import Sequence
from microbial_strain_data_model.classes.size import Size
from microbial_strain_data_model.classes.spore import Spore
from microbial_strain_data_model.classes.stainings import Staining
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

    # single data points
    id: int = Field(
        title="ID",
        alias="id",
        description="Unique identification number of the dataset",
        frozen=True,
    )

    last_update: DateTime = Field(
        default_factory=lambda: DateTime.now(),
        title="lastUpdate",
        alias="lastUpdate",
        description="Time of last update of the dataset",
        frozen=True,
    )

    organism_type: OrganismType = Field(
        title="Organism Type", alias="organismType", description="", frozen=True
    )

    morph_type: Morph | None = Field(
        default=None,
        title="Morph Type",
        alias="morphType",
        description="Applicable to fungi only",
        frozen=True,
    )

    unified_type_strain: bool = Field(
        title="Unified Type Strain",
        alias="unifiedTypeStrain",
        description="Is this strain type for unified species",
        frozen=True,
    )

    type_strain: list[TypeStrain] = Field(
        default_factory=list, title="Type Strain", alias="typeStrain", description=""
    )

    # maybe single data points

    unified_taxon: Taxon = Field(
        title="Unified Taxon",
        alias="unifiedTaxon",
        description="Evaluated and updated taxonomy",
    )

    taxon: list[TaxonWithSource] = Field(
        default_factory=list, title="Taxon", alias="taxon", description=""
    )

    sample: list[Sample] = Field(
        default_factory=list, title="Sample", alias="sample", description=""
    )

    isolation: list[Isolation] = Field(
        default_factory=list, title="Isolation", alias="isolation", description=""
    )

    # lists of data objects

    legal: list[Legal] = Field(
        default_factory=list, title="Legal", alias="legal", description=""
    )

    cell_shape: list[CellShape] = Field(
        default_factory=list, title="Cell Shape", alias="cellShape", description=""
    )

    oxygen_relation: list[OxygenRelation] = Field(
        default_factory=list,
        title="Oxygen Relation",
        alias="oxygenRelation",
        description="",
    )

    multi_cell_complex_forming: list[MultiCell] = Field(
        default_factory=list,
        title="Multi Cell Complex Forming",
        alias="multiCellComplexForming",
        description="",
    )

    cell_length: list[Size] = Field(
        default_factory=list, title="Cell Length", alias="cellLength", description=""
    )

    cell_width: list[Size] = Field(
        default_factory=list, title="Cell Width", alias="cellWidth", description=""
    )

    motility: list[Motility] = Field(
        default_factory=list, title="Motility", alias="motility", description=""
    )

    colony: list[Colony] = Field(
        default_factory=list, title="Colony", alias="colony", description=""
    )

    spore_formation: list[Spore] = Field(
        default_factory=list,
        title="Spore Formation",
        alias="sporeFormation",
        description="",
    )

    temperature: list[Growth[CelsiusUnit]] = Field(
        default_factory=list, title="Temperature", alias="temperature", description=""
    )

    ph: list[Growth[PHUnit]] = Field(
        default_factory=list, title="pH", alias="pH", description=""
    )

    identifier: list[IdentifierStrain] = Field(
        default_factory=list, title="Identifier", alias="identifier", description=""
    )

    connected_persons: list[ConnectedPerson] = Field(
        default_factory=list,
        title="Connected Persons",
        alias="connectedPersons",
        description="",
    )

    pathogenicity: list[Pathogen] = Field(
        default_factory=list, title="pathogenicity", alias="pathogenicity", description=""
    )

    bio_safety: list[BioSafety] = Field(
        default_factory=list, title="Bio Safety", alias="bioSafety", description=""
    )

    sequences: list[Sequence] = Field(
        default_factory=list, title="Sequences", alias="sequences", description=""
    )

    gc_content: list[GCContent] = Field(
        default_factory=list, title="GC Content", alias="gcContent", description=""
    )

    literature: list[Literature] = Field(
        default_factory=list, title="Literature", alias="literature", description=""
    )

    wall_constituents: list[CellWall] = Field(
        default_factory=list,
        title="Wall Constituents",
        alias="wallConstituents",
        description="",
    )

    fatty_acid_profiles: list[FattyAcidProfile] = Field(
        default_factory=list,
        title="Fatty Acid Profile",
        alias="fattyAcidProfiles",
        description="",
    )

    stainings: list[Staining] = Field(
        default_factory=list, title="Stainings", alias="stainings", description=""
    )

    hemolysis: list[Hemolysis] = Field(
        default_factory=list, title="Hemolysis", alias="hemolysis", description=""
    )

    cultivation_media: list[CultivationMedia] = Field(
        default_factory=list,
        title="Cultivation Media",
        alias="cultivationMedia",
        description="",
    )

    halophily: list[Halophil] = Field(
        default_factory=list, title="Halophily", alias="halophily", description=""
    )

    tolerances: list[Tolerance] = Field(
        default_factory=list, title="Tolerances", alias="tolerances", description=""
    )

    enzymes: list[Enzyme] = Field(
        default_factory=list, title="Enzymes", alias="enzymes", description=""
    )
    metabolites: list[Metabolite] = Field(
        default_factory=list, title="Metabolites", alias="metabolites", description=""
    )

    known_applications: list[Application] = Field(
        default_factory=list,
        title="Known Applications",
        alias="knownApplications",
        description="",
    )

    collections: list[Collection] = Field(
        default_factory=list, title="Collections", alias="collections", description=""
    )

    other_media: list[OtherMedia] = Field(
        default_factory=list, title="Other Media", alias="otherMedia", description=""
    )

    sources: list[Literature | Organization | Person] = Field(
        title="Source", alias="sources", description=""
    )

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )
