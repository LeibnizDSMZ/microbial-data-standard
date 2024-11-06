from microbial_strain_data_model.classes.enums import OrganismType
from microbial_strain_data_model.classes.taxon import TaxonRank, TaxonStatus
import pytest
from microbial_strain_data_model.microbe import Microbe


@pytest.fixture()
def micro():
    return Microbe(
        id=1,
        organismType=OrganismType.bacteria,
        typeStrain=False,
        sample=[
            {
                "tags": [
                    {"level1": "#Host", "level2": "#Fishes", "level3": "#Zebrafish"}
                ],
                "source": "/sources/0",
            }
        ],
        taxon={
            "name": "Somename",
            "taxonRank": TaxonRank.species,
            "taxonStatus": TaxonStatus.valid,
        },
        otherMedia=[{"url": None, "name": "test", "source": "/sources/0"}],
        fattyAcidProfile=[
            {"profile": [{"percent": 10.0}], "temperature": 10, "source": "/sources/0"}
        ],
        sources=[
            {
                "name": "DSMZ",
                "legalName": "Leibniz Institut: Deutsche Sammlung für "
                "Microorganismen und Zellkulturen, GmbH",
                "address": {"addressCountry": "DE"},
            }
        ],
    )


def test_microbe(micro) -> None:
    assert micro.id == 1
    assert micro.organism_type == "Bacteria"
