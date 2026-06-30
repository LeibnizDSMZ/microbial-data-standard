# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.classes.source import Source
from microbial_strain_data_model.strain import Strain
import pytest

pytest_plugins = ("tests.fixture.split",)


def test_integration_split_object(split: Strain) -> None:
    source_dict = {
        "mode": "automated",
        "name": "B",
        "publisher": [
            {
                "address": None,
                "email": None,
                "legalName": "BBBBBBB",
                "name": "B",
                "url": None,
            }
        ],
        "sourceType": "dataset",
    }
    extract_source = Source.model_validate(source_dict)

    micro_purged, micro_extracted = split.split(extract_source)

    assert Strain.model_validate(micro_purged)
    assert Strain.model_validate(micro_extracted)

    assert len(micro_purged.sources) == 2
    assert len(micro_extracted.sources) == 1

    assert extract_source._index() not in (mic._index() for mic in micro_purged.sources)
    assert extract_source._index() in (mic._index() for mic in micro_extracted.sources)

    assert "/sources/2" not in micro_purged.model_dump_json()

    assert "/sources/1" not in micro_extracted.model_dump_json()
    assert "/sources/2" not in micro_extracted.model_dump_json()


def test_integration_split_object_error(split: Strain) -> None:
    org = Source.model_validate(
        {"sourceType": "dataset", "mode": "automated", "name": "Z"}
    )
    with pytest.raises(IndexError, match=r"Received incorrect source or index"):
        split.split(org)


def test_integration_split_index(split: Strain) -> None:
    source_dict = {
        "sourceType": "dataset",
        "mode": "automated",
        "name": "B",
        "publisher": [
            {
                "address": None,
                "email": None,
                "legalName": "BBBBBBB",
                "name": "B",
                "url": None,
            }
        ],
    }
    extract_source = Source.model_validate(source_dict)

    micro_purged, micro_extracted = split.split(1)

    assert Strain.model_validate(micro_purged)
    assert Strain.model_validate(micro_extracted)

    assert extract_source not in micro_purged.sources
    assert extract_source in micro_extracted.sources

    assert len(micro_purged.sources) == 2
    assert len(micro_extracted.sources) == 1

    assert "/sources/2" not in micro_purged.model_dump_json()

    assert "/sources/1" not in micro_extracted.model_dump_json()
    assert "/sources/2" not in micro_extracted.model_dump_json()


def test_integration_split_index_error(split: Strain) -> None:
    with pytest.raises(IndexError, match=r"Received incorrect source or index"):
        split.split(3)
