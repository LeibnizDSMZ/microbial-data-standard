from pydantic import HttpUrl
from microbial_strain_data_model.classes.identifier import Identifier
from microbial_strain_data_model.classes.address import Address
from microbial_strain_data_model.classes.organization import Organization
from microbial_strain_data_model.classes.source import Source
from microbial_strain_data_model.classes.chemicalsubstance import FattyAcid
from microbial_strain_data_model.classes.fattyacidprofile import FattyAcidProfile
from microbial_strain_data_model.classes.othermedia import OtherMedia
from microbial_strain_data_model.classes.isolationtag import IsolationTag
from microbial_strain_data_model.classes.taxon import TaxonWithSource
from microbial_strain_data_model.classes.origin import Origin
from microbial_strain_data_model.classes.taxon import TypeStrain
from microbial_strain_data_model.classes.identifier import IdentifierStrain
from microbial_strain_data_model.classes.enums import OrganismType
from microbial_strain_data_model.classes.taxon import TaxonRank, TaxonStatus
import pytest
from microbial_strain_data_model.strain import Strain


@pytest.fixture
def micro():
    return Strain(
        primaryId="DSM 1",
        organismType=OrganismType.bacteria,
        identifier=[
            IdentifierStrain(
                name="DSMZ internal ID",
                propertyID="https://www.wikidata.org/wiki/Property:P6782",
                url=None,
                value="DSM 1",
                source=["/sources/0"],
            )
        ],
        typeStrain=[TypeStrain(typeStrain=False, source=["/sources/0"])],
        origin=[
            Origin(
                tags=[
                    IsolationTag(level1="#Host", level2="#Fishes", level3="#Zebrafish")
                ],
                source=["/sources/0"],
            )
        ],
        taxon=[
            TaxonWithSource(
                name="Somename",
                taxonRank=TaxonRank.species,
                taxonStatus=TaxonStatus.valid,
                source=["/sources/0"],
            )
        ],
        otherMedia=[OtherMedia(url=None, name="test", source=["/sources/0"])],
        fattyAcidProfiles=[
            FattyAcidProfile(profile=[FattyAcid(percent=10.0)], source=["/sources/0"])
        ],
        sources=[
            Source(
                sourceType="dataset",
                mode="automated",
                name="DSMZ internal database",
                url=None,
                identifier=[],
                datePublished="2024-12",
                dateRecorded="2025-06-24",
                author=[],
                publisher=[
                    Organization(
                        address=Address(
                            addressCountry="DE",
                            addressLocality="Braunschweig",
                            postalCode="38124",
                            streetAddress="Inhoffenstraße 7B",
                        ),
                        email="info@dsmz.de",
                        identifier=[
                            Identifier(
                                name="ROR",
                                propertyID="https://www.wikidata.org/wiki/Property:P6782",
                                url=None,
                                value="https://ror.org/02tyer376",
                            )
                        ],
                        legalName="Leibniz-Institut DSMZ-Deutsche Sammlung "
                        + "von Mikroorganismen und Zellkulturen GmbH",
                        name="DSMZ",
                        url=HttpUrl("https://www.dsmz.de/"),
                        logo=HttpUrl(
                            "https://www.dsmz.de/fileadmin/templates/main/img/logo_en.svg"
                        ),
                    )
                ],
            )
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
        identifier=micro.identifier,
    )
    assert new_micro
