from microbial_strain_data_model.classes.enums import OrganismType
from microbial_strain_data_model.classes.taxon import TaxonRank, TaxonStatus
import pytest
from microbial_strain_data_model.strain import Strain

# ruff: noqa: E501


@pytest.fixture
def micro():
    return Strain(
        primaryId="DSM 1",
        organismType=OrganismType.bacteria,
        typeStrain=[{"typeStrain": False, "source": ["/sources/0"]}],
        origin=[
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
                "sourceType": "dataset",
                "mode": "automated",
                "name": "DSMZ internal database",
                "url": None,
                "identifier": [],
                "datePublished": "2024-12",
                "dateRecorded": "2025-06-24",
                "author": [],
                "publisher": [
                    {
                        "address": {
                            "addressCountry": "DE",
                            "addressLocality": "Braunschweig",
                            "postalCode": "38124",
                            "streetAddress": "Inhoffenstraße 7B",
                        },
                        "email": "info@dsmz.de",
                        "identifier": [
                            {
                                "name": "ROR",
                                "propertyID": "https://www.wikidata.org/wiki/Property:P6782",
                                "url": None,
                                "value": "https://ror.org/02tyer376",
                            }
                        ],
                        "legalName": "Leibniz-Institut DSMZ-Deutsche Sammlung von Mikroorganismen und Zellkulturen GmbH",
                        "name": "DSMZ",
                        "url": "https://www.dsmz.de/",
                        "logo": "https://www.dsmz.de/fileadmin/templates/main/img/logo_en.svg",
                    }
                ],
            }
        ],
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
    )
    assert new_micro
