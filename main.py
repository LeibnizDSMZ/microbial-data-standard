import json
from pathlib import Path

from microbial_strain_data_model.classes.actors import Collection
from microbial_strain_data_model.microbe import Microbe


def dump_all_schemas() -> None:
    mi = Microbe.model_json_schema()
    main_schema_path = Path("schema/microbe_schema.json")
    with main_schema_path.open("w") as f_out:
        f_out.write(json.dumps(mi, indent=2))

    col = Collection.model_json_schema()
    col_schema_path = Path("schema/collection_schema.json")
    with col_schema_path.open("w") as f_out:
        f_out.write(json.dumps(col, indent=2))


def test_validation() -> None:
    if Microbe(
        id=1,
        organismType="Bacteria",
        typeStrain=False,
        nagoyaRestrictions="No known restrictions under the Nagoya protocol",
        source={
            "name": "DSMZ",
            "legalName": "Leibniz Institut: Deutsche Sammlung für "
            "Microorganismen und Zellkulturen, GmbH",
            "address": {"addressCountry": "DE"},
        },
        sample={
            "tags": [{"level1": "#Host", "level2": "#Fishes", "level3": "#Zebrafish"}]
        },
        taxon={"name": "", "taxonRank": "Species", "taxonStatus": "Validly published"},
        otherMedia=[{"url": None, "name": "test"}],
        fattyAcidProfile=[{"profile": [{"percent": 10.0}], "temperature": 10}],
    ):
        print("Mircobe works")


if __name__ == "__main__":
    dump_all_schemas()
    # test_validation()
