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
from microbial_strain_data_model.classes.taxon import Taxon
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
    id: int = Field(title="ID", alias="id", frozen=True)

    last_update: DateTime = Field(
        default_factory=lambda: DateTime.now(),
        title="lastUpdate",
        alias="lastUpdate",
        frozen=True,
    )

    organism_type: OrganismType = Field(
        title="Organism Type", alias="organismType", frozen=True
    )

    morph_type: Morph | None = Field(
        default=None, title="Morph Type", alias="morphType", frozen=True
    )

    type_strain: bool = Field(title="Type Strain", alias="typeStrain", frozen=True)

    # maybe single data points

    taxon: Taxon = Field(title="Taxon", alias="taxon")

    sample: list[Sample] = Field(default_factory=list, title="Sample", alias="sample")

    isolation: list[Isolation] = Field(
        default_factory=list, title="Isolation", alias="isolation"
    )

    # lists of data objects

    legal: list[Legal] = Field(default_factory=list, title="Legal", alias="legal")

    cell_shape: list[CellShape] = Field(
        default_factory=list, title="Cell Shape", alias="cellShape"
    )

    oxygen: list[OxygenRelation] = Field(
        default_factory=list, title="Oxygen Relation", alias="oxygenRelation"
    )

    multi_cell: list[MultiCell] = Field(
        default_factory=list,
        title="Multi Cell Complex Forming",
        alias="multiCellComplexForming",
    )

    cell_length: list[Size] = Field(
        default_factory=list, title="Cell Length", alias="cellLength"
    )

    cell_width: list[Size] = Field(
        default_factory=list, title="Cell Width", alias="cellWidth"
    )

    cell_motility: list[Motility] = Field(
        default_factory=list, title="Motility", alias="motility"
    )

    colony: list[Colony] = Field(default_factory=list, title="Colony", alias="colony")

    spore: list[Spore] = Field(
        default_factory=list, title="Spore Formation", alias="sporeFormation"
    )

    temperature: list[Growth[CelsiusUnit]] = Field(
        default_factory=list, title="Temperature", alias="temperature"
    )

    ph: list[Growth[PHUnit]] = Field(default_factory=list, title="pH", alias="pH")

    identifier: list[IdentifierStrain] = Field(
        default_factory=list, title="Identifier", alias="identifier"
    )

    connected_persons: list[ConnectedPerson] = Field(
        default_factory=list, title="Connected Persons", alias="connectedPersons"
    )

    pathogenicity: list[Pathogen] = Field(
        default_factory=list, title="pathogenicity", alias="pathogenicity"
    )

    bio_safety: list[BioSafety] = Field(
        default_factory=list, title="Bio Safety", alias="bioSafety"
    )

    sequences: list[Sequence] = Field(
        default_factory=list, title="Sequences", alias="sequences"
    )

    gc: list[GCContent] = Field(
        default_factory=list, title="GC Content", alias="gcContent"
    )

    literature: list[Literature] = Field(
        default_factory=list, title="Literature", alias="literature"
    )

    cell_wall: list[CellWall] = Field(
        default_factory=list, title="Wall Constituents", alias="wallConstituents"
    )

    fatty_acid_profiles: list[FattyAcidProfile] = Field(
        default_factory=list, title="Fatty Acid Profile", alias="fattyAcidProfile"
    )

    stainings: list[Staining] = Field(
        default_factory=list, title="Stainings", alias="stainings"
    )

    hemolysis: list[Hemolysis] = Field(
        default_factory=list, title="Hemolysis", alias="hemolysis"
    )

    cultivation_media: list[CultivationMedia] = Field(
        default_factory=list, title="Cultivation Media", alias="cultivationMedia"
    )

    halophily: list[Halophil] = Field(
        default_factory=list, title="Halophily", alias="halophily"
    )

    tolerances: list[Tolerance] = Field(
        default_factory=list, title="Tolerances", alias="tolerances"
    )

    enzymes: list[Enzyme] = Field(default_factory=list, title="Enzymes", alias="enzymes")
    metabolites: list[Metabolite] = Field(
        default_factory=list, title="Metabolites", alias="metabolites"
    )

    applications: list[Application] = Field(
        default_factory=list, title="Known Applications", alias="knownApplications"
    )

    collections: list[Collection] = Field(
        default_factory=list, title="Collections", alias="collections"
    )

    other_media: list[OtherMedia] = Field(
        default_factory=list, title="Other Media", alias="otherMedia"
    )

    sources: list[Literature | Organization | Person] = Field(
        title="Source", alias="sources"
    )

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )
