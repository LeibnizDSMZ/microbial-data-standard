# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.shared.data_ops.mapping import (
    build_link_mapping_and_merge,
)
from typing import Any
from typing import Iterable
from microbial_strain_data_model.classes.root import join_links
from microbial_strain_data_model.classes.root import Root
from microbial_strain_data_model.classes.root import fix_related_data
from microbial_strain_data_model.classes.root import fix_source
from pydantic.fields import PrivateAttr
from microbial_strain_data_model.classes.links import LinkType
import re
from typing import Self
from pydantic import BaseModel, ConfigDict, Field
from deepdiff import DeepHash


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


_SRC_PATH = re.compile(r"root\['source'\].*")
_REL_PATH = re.compile(r"\['relatedData'\]")
_ROOT_TYPES = (
    TypeStrain,
    TaxonWithSource,
    IdentifierStrain,
    Origin,
    Legal,
    Pathogen,
    BioSafety,
    Morphology,
    CellWall,
    Staining,
    Spore,
    GrowthCondition,
    CultivationMedia,
    Sequence,
    GCContent,
    FattyAcidProfile,
    Hemolysis,
    Halophil,
    Tolerance,
    Enzyme,
    Metabolite,
    Application,
    Collection,
    Literature,
    OtherMedia,
)


class Strain(BaseModel):
    """Microbial Strain - main class of the new microbial strain data standard."""

    model_config = ConfigDict(
        strict=True,
        extra="allow",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    # single data points

    primaryId: str = Field(
        title="Primary Identifier", description="Primary Identifier for this dataset"
    )

    organismType: OrganismType = Field(title="Organism Type", description="", frozen=True)

    morphType: Morph | None = Field(
        default=None,
        title="Morph Type",
        description="Applicable and required for fungi only",
        frozen=True,
    )

    # lists of data objects

    typeStrain: list[TypeStrain] = Field(
        default_factory=list, title="Type Strain", description=""
    )

    taxon: list[TaxonWithSource] = Field(
        default_factory=list, title="Taxon", description=""
    )

    identifier: list[IdentifierStrain] = Field(
        title="Identifier", description="", min_length=1
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

    ###

    _cache: dict[str, dict[str, Root]] = PrivateAttr(
        default_factory=dict,
    )

    def check_constrains(self, r_mi: Self) -> bool:
        """Hard constrains, add more if necessary"""
        # check if organism types are equal
        if self.organismType is not r_mi.organismType:
            raise ValueError(
                f"Organism types do not match: {self.organismType} != {r_mi.organismType}"
            )
        return True

    def _join_field_right(
        self,
        field_name: str,
        attr_right: list[Any],
        source_map: dict[str, str],
        related_data_map: dict[str, str],
        /,
    ) -> Iterable[Root | RelatedData]:
        for data_obj_right in attr_right:
            if not (
                isinstance(data_obj_right, _ROOT_TYPES)
                or isinstance(data_obj_right, RelatedData)
            ):
                continue
            fix_source(data_obj_right, source_map)
            if isinstance(data_obj_right, RelatedData):
                yield data_obj_right
                continue
            fix_related_data(data_obj_right, related_data_map)
            hash_right = DeepHash(
                (data_obj_right_d := data_obj_right.model_dump()),
                exclude_regex_paths=[_SRC_PATH, _REL_PATH],
            )[data_obj_right_d]
            same_obj: Root | None = self._cache.get(field_name, {}).get(hash_right, None)
            if same_obj is not None:
                join_links(same_obj, data_obj_right)
            else:
                self._cache[field_name][hash_right] = data_obj_right
                yield data_obj_right

    def join(self, to_join: Self, /) -> Self:
        # Step 1
        self.check_constrains(to_join)
        # Step 2
        source_map, links = build_link_mapping_and_merge(
            self.sources, to_join.sources, LinkType.source
        )
        self.sources.extend(links)
        # Step 3
        related_data_map, links = build_link_mapping_and_merge(
            self.relatedData, to_join.relatedData, LinkType.related_data
        )
        self.relatedData.extend(links)
        # Step 4
        not_cached = len(self._cache) == 0
        for field_name in Strain.model_fields.keys():
            if field_name == "sources":
                continue
            attr_right = getattr(to_join, field_name)
            attr_left = getattr(self, field_name)
            if not (isinstance(attr_right, list) and isinstance(attr_left, list)):
                continue

            if not_cached and field_name != "relatedData":
                self._cache[field_name] = {
                    DeepHash(
                        (ele_d := ele.model_dump()),
                        exclude_regex_paths=[_SRC_PATH, _REL_PATH],
                    )[ele_d]: ele
                    for ele in attr_left
                    if isinstance(ele, _ROOT_TYPES)
                }
            attr_left.extend(
                self._join_field_right(
                    field_name, attr_right, source_map, related_data_map
                )
            )
        return self
