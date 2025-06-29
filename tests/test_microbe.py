from microbial_strain_data_model.classes.enums import OrganismType
from microbial_strain_data_model.classes.taxon import TaxonRank, TaxonStatus
import pytest
from microbial_strain_data_model.microbe import Microbe


@pytest.fixture
def micro():
    return Microbe(
        organismType=OrganismType.bacteria,
        typeStrain=[{"typeStrain": False, "source": ["/sources/0"]}],
        sample=[
            {
                "tags": [
                    {"level1": "#Host", "level2": "#Fishes", "level3": "#Zebrafish"}
                ],
                "source": ["/sources/0"],
            }
        ],
        taxon=[
            {
                "name": "Somename",
                "taxonRank": TaxonRank.species,
                "taxonStatus": TaxonStatus.valid,
                "source": ["/sources/0"],
            }
        ],
        otherMedia=[{"url": None, "name": "test", "source": ["/sources/0"]}],
        fattyAcidProfiles=[{"profile": [{"percent": 10.0}], "source": ["/sources/0"]}],
        sources=[
            {
                "name": "DSMZ",
                "legalName": "Leibniz Institut: Deutsche Sammlung für Microorganismen "
                "und Zellkulturen, GmbH",
                "address": {"addressCountry": "DE"},
            }
        ],
    )


def test_microbe(micro: Microbe) -> None:
    assert micro.organismType == "Bacteria"


def test_populate_new_class(micro: Microbe) -> None:
    new_micro = Microbe(
        organismType=micro.organismType,
        typeStrain=micro.typeStrain,
        taxon=micro.taxon,
        sources=micro.sources,
    )
    assert new_micro
