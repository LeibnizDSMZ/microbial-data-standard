# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.strain import Strain


pytest_plugins = (
    "tests.fixture.core",
    "tests.fixture.bacteria",
    "tests.fixture.fungi",
)


def test_microbe(micro: Strain) -> None:
    assert micro.organismType == "Bacteria"


def test_populate_new_class(micro: Strain) -> None:
    new_micro = Strain(
        primaryId=micro.primaryId,
        organismType=micro.organismType,
        typeStrain=micro.typeStrain,
        taxon=micro.taxon,
        sources=micro.sources,
        identifier=micro.identifier,
    )
    assert new_micro


def test_fixture_bacteria(bacteria: Strain) -> None:
    assert isinstance(bacteria, Strain)


def test_fixture_fungi(fungi: None) -> None:
    # TODO add fungi tests
    assert fungi is None


def test_fixture_fungi_min(fungi_min: Strain) -> None:
    assert isinstance(fungi_min, Strain)
