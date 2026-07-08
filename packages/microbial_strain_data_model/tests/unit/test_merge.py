# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.classes.links import LinkType
from microbial_strain_data_model.shared.data_ops.mapping import (
    build_link_mapping_and_merge,
)
from microbial_strain_data_model.strain import Strain
from pathlib import Path
import pytest
from microbial_strain_data_model.classes.source import Source, SourceType, CurationMode

_ROOT = Path(__file__).parent

pytest_plugins = (
    "tests.fixture.fungi",
    "tests.fixture.merge",
)


def test_integration_merge(micro_left: Strain, micro_right: Strain) -> None:
    assert len(micro_left.sources) == 2
    assert len(micro_left.relatedData) == 2
    assert len(micro_right.sources) == 2
    assert len(micro_right.relatedData) == 2
    mm = micro_left.join(micro_right, True)
    assert len(mm.sources) == 3
    assert len(mm.relatedData) == 3

    assert mm.sources[0].name == "DSMZ"
    assert mm.sources[1].name == "DSMZ 2"
    assert mm.sources[2].name == "Source2"

    assert mm.relatedData[0].relation == "test relation 1"
    assert mm.relatedData[1].relation == "test relation 2"
    assert mm.relatedData[2].relation == "test relation 2"

    assert len(mm.cultivationMedia) == 2

    assert mm.cultivationMedia[0].source == ["/sources/0"]
    assert mm.cultivationMedia[0].relatedData == ["/relatedData/0"]

    assert set(mm.cultivationMedia[1].source) == {"/sources/1", "/sources/2"}
    assert set(mm.cultivationMedia[1].relatedData) == {"/relatedData/1", "/relatedData/2"}


def test_unit_build_source_mapping() -> None:
    list_a = [
        Source(
            sourceType=SourceType("literature"),
            mode=CurationMode("automated"),
            name="A literature",
        ),
        Source(
            sourceType=SourceType("website"),
            mode=CurationMode("automated"),
            name="A Person",
        ),
        Source(
            sourceType=SourceType("dataset"),
            mode=CurationMode("automated"),
            name="A Organisation",
        ),
    ]
    list_b = [
        Source(
            sourceType=SourceType("literature"),
            mode=CurationMode("automated"),
            name="B literature",
        ),
        Source(
            sourceType=SourceType("website"),
            mode=CurationMode("automated"),
            name="A Person",
        ),
        Source(
            sourceType=SourceType("dataset"),
            mode=CurationMode("automated"),
            name="B Organisation",
        ),
    ]

    # mapping includes for str from list_b the new strings for merged result
    map_l, map_r, _ = build_link_mapping_and_merge(list_a, list_b, LinkType.source)

    assert isinstance(map_l, dict)
    assert isinstance(map_r, dict)
    assert len(map_r.keys()) == 3
    assert len(map_l.keys()) == 3
    assert map_r["/sources/0"] == "/sources/3"  # first element list_b
    assert map_r["/sources/1"] == "/sources/1"  # second element list_b
    assert map_r["/sources/2"] == "/sources/4"  # third element list_b


def test_unit_check_constrains(micro_left: Strain, micro_right: Strain) -> None:
    assert len(micro_left.sources) == 2
    assert len(micro_right.sources) == 2
    assert micro_left.check_constrains(micro_right)


def test_value_error(micro_left: Strain, fungi_min: Strain) -> None:
    with pytest.raises(ValueError, match=r".*"):
        micro_left.check_constrains(fungi_min)
