# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing import Literal
from microbial_strain_data_model.classes.root import split_item
from copy import deepcopy
from microbial_strain_data_model.shared.data_ops.mapping import (
    build_link_mapping_and_split,
)
from collections import defaultdict
import uuid
from typing import Any
from typing import Iterable
from pydantic.fields import PrivateAttr
import re
from typing import Self
from pydantic import BaseModel, ConfigDict, Field
from deepdiff import DeepHash

from microbial_strain_data_model.classes.links import LinkType
from microbial_strain_data_model.classes.root import join_links
from microbial_strain_data_model.classes.root import Root
from microbial_strain_data_model.classes.root import fix_related_data
from microbial_strain_data_model.classes.root import fix_source
from microbial_strain_data_model.shared.data_ops.mapping import (
    build_link_mapping_and_merge,
)
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
type _MAPPING = tuple[
    dict[str, str | None],
    dict[str, str | None],
    dict[str, str | None],
    dict[str, str | None],
    list[Source],
    list[RelatedData],
]


class Strain(BaseModel):
    """Microbial Strain - main class of the new microbial strain data standard."""

    model_config = ConfigDict(
        strict=True,
        extra="allow",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    # version

    version: Literal[1]

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
        default_factory=lambda: defaultdict(dict),
    )

    def check_constrains(self, r_mi: Self) -> bool:
        """Hard constrains, add more if necessary"""
        # check if organism types are equal
        if self.organismType is not r_mi.organismType:
            raise ValueError(
                f"Organism types do not match: {self.organismType} != {r_mi.organismType}"
            )
        return True

    def _join_field_unique(
        self,
        field_name: str,
        attr_list: list[Any],
        source_map: dict[str, str],
        related_data_map: dict[str, str],
        /,
    ) -> Iterable[Root | RelatedData]:
        for data_obj in attr_list:
            if not isinstance(data_obj, _ROOT_TYPES):
                continue
            fix_source(data_obj, source_map)
            fix_related_data(data_obj, related_data_map)
            hash_right = DeepHash(
                (data_obj_right_d := data_obj.model_dump()),
                exclude_regex_paths=[_SRC_PATH, _REL_PATH],
            )[data_obj_right_d]
            same_obj: Root | None = self._cache.get(field_name, {}).get(hash_right, None)
            if same_obj is not None:
                join_links(same_obj, data_obj)
            else:
                self._cache[field_name][hash_right] = data_obj
                yield data_obj

    def join(self, to_join: Self, re_validate: bool = False, /) -> Self:
        """Joins this instance with another instance of the same type.

        Combines data from two Strain instances by first validating constraints between
        instances, then merging source references and fixing related data, followed by merging
        related data references, and finally joining all other fields while maintaining
        uniqueness.

        Args:
            to_join: Another Strain instance to join with this one

        Returns:
            Self: The modified instance with joined data

        Raises:
            ValueError: If constraint validation fails
        """
        # Step 1
        self.check_constrains(to_join)
        # Step 2
        source_map_l, source_map_r, links = build_link_mapping_and_merge(
            self.sources, to_join.sources, LinkType.source
        )
        self.sources = links
        to_fix = (
            (self.relatedData, source_map_l),
            (to_join.relatedData, source_map_r),
        )
        for rel_dat, src_map in to_fix:
            for rel in rel_dat:
                fix_source(rel, src_map)
        # Step 3
        related_data_map_l, related_data_map_r, links = build_link_mapping_and_merge(
            self.relatedData, to_join.relatedData, LinkType.related_data
        )
        self.relatedData = links
        # Step 4
        not_cached = len(self._cache) == 0
        for field_name in Strain.model_fields.keys():
            if field_name == "sources" or field_name == "relatedData":
                continue
            attr_right = getattr(to_join, field_name)
            attr_left = getattr(self, field_name)
            if not (isinstance(attr_right, list) and isinstance(attr_left, list)):
                continue

            if not_cached:
                joined = list(
                    self._join_field_unique(
                        field_name, attr_left, source_map_l, related_data_map_l
                    )
                )
                setattr(self, field_name, joined)
            attr_left.extend(
                self._join_field_unique(
                    field_name, attr_right, source_map_r, related_data_map_r
                )
            )
        if re_validate:
            self.model_validate(self)
        return self

    def _create_mapping(self, to_split: int, /) -> _MAPPING:
        source_map_l, source_map_r, src_l, src_r = build_link_mapping_and_split(
            self.sources, {to_split}, LinkType.source
        )
        self.sources = src_l
        rel_to_split = set()
        for rel_i, rel in enumerate(self.relatedData):
            left, right = split_item(to_split, rel, (source_map_l, source_map_r))
            if right is not None:
                rel_to_split.add(rel_i)

        related_data_map_l, related_data_map_r, rel_l, rel_r = (
            build_link_mapping_and_split(
                self.relatedData, rel_to_split, LinkType.related_data
            )
        )
        self.relatedData = rel_l
        return (
            source_map_l,
            source_map_r,
            related_data_map_l,
            related_data_map_r,
            src_r,
            rel_r,
        )

    def _split_by_index(self, to_split: int, re_validate: bool, /) -> tuple[Self, Self]:
        to_copy_right: dict[str, list[Root]] = defaultdict(list)

        (
            source_map_l,
            source_map_r,
            related_data_map_l,
            related_data_map_r,
            src_r,
            rel_r,
        ) = self._create_mapping(to_split)

        for field_name in Strain.model_fields.keys():
            if field_name == "sources" or field_name == "relatedData":
                continue
            attr_left = getattr(self, field_name)
            if not isinstance(attr_left, list):
                continue
            clean_roots = []
            for data_obj in attr_left:
                if not isinstance(data_obj, _ROOT_TYPES):
                    continue
                left, right = split_item(
                    to_split,
                    data_obj,
                    (source_map_l, source_map_r),
                    (related_data_map_l, related_data_map_r),
                )
                if right is not None:
                    to_copy_right[field_name].append(right)
                if left is not None:
                    clean_roots.append(left)
            setattr(self, field_name, clean_roots)
        if re_validate:
            self.model_validate(self)
        return self, type(self).model_validate(
            {
                "version": 1,
                "primaryId": str(uuid.uuid4()),
                "organismType": deepcopy(self.organismType),
                "sources": src_r,
                "relatedData": rel_r,
                **to_copy_right,
            }
        )

    def split(
        self, to_split: int | Source, re_validate: bool = False, /
    ) -> tuple[Self, Self]:
        """Splits the Strain instance into two distinct instances based on a specific Source.

        This method separates the data associated with a specific source (identified by index
        or object) from the rest of the data. It effectively creates two new strain records:
        one containing data linked to the specified source, and another containing the
        remaining data.

        The method splits the strain instance into two by identifying a specific source,
        separating its associated data and links from the rest, and assigning a new
        UUID to the resulting instance.

        Args:
            to_split (int | Source): The source to split by. Can be the integer index of
                the source in the `sources` list, or the `Source` object itself.

        Returns:
            tuple[Self, Self]: A tuple containing two Strain instances.
                - The first element is the modified original instance (self), containing
                  data *not* linked to the split source.
                - The second element is the new instance containing data *only* linked
                  to the split source.

        Raises:
            IndexError: If the provided integer index is out of bounds or if the
                provided Source object is not found in the `sources` list.
        """
        to_split_index = to_split
        if isinstance(to_split, Source):
            for sid, source in enumerate(self.sources):
                if source._index() == to_split._index():
                    to_split_index = sid
                    break
        if not (
            isinstance(to_split_index, int) and 0 <= to_split_index < len(self.sources)
        ):
            raise IndexError("Received incorrect source or index")
        return self._split_by_index(to_split_index, re_validate)
