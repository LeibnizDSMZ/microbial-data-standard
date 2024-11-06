# Fungi

This is a example data for a yeast. The data is artificial and should only demonstrate
what the data in this schema look like.

```JSON
{
    "id": 2,
    "last_update": "2024-07-16T00:00:00Z",
    "organism_type": "Fungi",
    "morph_type": "yeast",
    "type_strain": true,
    "taxon": {
        "name": "Candida albicans",
        "rank": "species",
        "status": "validly published",
        "identifier": [
            {
                "name": "NCBI:txid",
                "value": "5476",
                "property": "https://www.wikidata.org/wiki/Property:P685",
                "url": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5476"
            },
            {
                "name": "MycoBank",
                "value": "256187",
                "property": "https://www.wikidata.org/wiki/Property:P962",
                "url": "https://www.mycobank.org/page/Name%20details%20page/106232"
            }
        ],
        "scientific": {
            "name": "Candida albicans",
            "author": "(Robin) Berkhout 1923"
        },
        "alternate_name": [],
        "parent": {
            "name": "Candida",
            "rank": "genus",
            "status": "validly published",
            "identifier": [
                {
                    "name": "NCBI:txid",
                    "value": "5475",
                    "property": "https://www.wikidata.org/wiki/Property:P685",
                    "url": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=5475"
                },
                {
                    "name": "MycoBank",
                    "value": "7487",
                    "property": "https://www.wikidata.org/wiki/Property:P962",
                    "url": "https://www.mycobank.org/page/Name%20details%20page/56219"
                }
            ],
            "scientific": {
                "name": "Candida",
                "author": "Berkhout 1923"
            },
            "alternate_name": [
                "Oidium albicans, C.P. Robin (1853)",
                "Myceloblastanon albicans, (C.P. Robin, 1928)"
            ],
            "parent": null,
            "same_as": []
        },
        "same_as": [
            "https://www.ncbi.nlm.nih.gov/datasets/taxonomy/5475/",
            "https://en.wikipedia.org/wiki/Candida_albicans"
        ]
    },
    "sample": [
        {
            "date": "/1987-06-11",
            "country": null,
            "description": "Skin of man with interdigital mycosis",
            "location": {
                "name": "Montevideo",
                "description": "",
                "geo": {
                    "latitude": -34.883611,
                    "longitude": -56.181944,
                    "elevation": null,
                    "precision": null
                }
            },
            "tags": [],
            "source": "/sources/0"
        }
    ],
    "isolation": [
        {
            "date": null,
            "isolator": null,
            "source": "/sources/0"
        }
    ],
    "legal": [
        {
            "dual_use": false,
            "quarantine": null,
            "nagoya": "No known restrictions under the Nagoya protocol",
            "QPS": false,
            "GRAS": false,
            "gmo": false,
            "gmo_information": null,
            "source": "/sources/0"
        }
    ],
    "cell_shape": [
        {
            "cell_shape": "round",
            "source": "/sources/0"
        }
    ],
    "oxygen": [
        {
            "relation": "aerobe",
            "source": "/sources/0"
        }
    ],
    "multi_cell": [
        {
            "multi_cell": false,
            "source": "/sources/0"
        }
    ],
    "cell_length": [
        {
            "min": 2.0,
            "max": 7.0,
            "unit": "µm",
            "source": "/sources/0"
        }
    ],
    "cell_width": [
        {
            "min": 1.0,
            "max": 3.0,
            "unit": "µm",
            "source": "/sources/0"
        }
    ],
    "cell_motility": [
        {
            "motile": false,
            "flagellum": null,
            "flag_arr": null,
            "gliding": null,
            "source": "/sources/0"
        }
    ],
    "colony": [],
    "spore": [
        {
            "building": null,
            "type": "spore",
            "ejection": null,
            "source": "/sources/0"
        }
    ],
    "temperature": [
        {
            "optimal": 25.0,
            "minimal": null,
            "maximal": null,
            "unit": "C",
            "tests": [],
            "source": "/sources/0"
        }
    ],
    "ph": [
        {
            "optimal": null,
            "minimal": null,
            "maximal": null,
            "unit": "pH",
            "tests": [],
            "source": "/sources/0"
        }
    ],
    "identifier": [
        {
            "name": "CCNO",
            "value": "ATCC 18804",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "CBS 562",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "CCRC 20512",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "CECT 1002",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "DBVPG 6133",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "IFO 1385",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "IGC 3436",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "JCM 1542",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "KCTC 7270",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "NCYC 597",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "NRRL Y-12983",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "PYCC 3436",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "Designation",
            "value": "DBVPG 6133",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "TheYeastsStrain",
            "value": "309",
            "property": null,
            "url": "https://theyeasts.org/page/yeasts-strains-display/309",
            "source": "/sources/0"
        },
        {
            "name": "SI-ID",
            "value": "14077",
            "property": null,
            "url": "https://straininfo.dsmz.de/strain/14077",
            "source": "/sources/0"
        }
    ],
    "connected_persons": [],
    "pathogenicity": [
        {
            "host": "human",
            "pathogen": "obligate",
            "classification": null,
            "source": "/sources/0"
        }
    ],
    "bio_safety": [
        {
            "group": "2",
            "classification": "German classification",
            "url": "https://www.baua.de/EN/Service/Legislative-texts-and-technical-rules/Rules/TRBA/TRBA-466.html",
            "source": "/sources/0"
        }
    ],
    "sequences": [
        {
            "type": "nucleotide",
            "level": "identifier sequence",
            "accession": "AY497682",
            "description": "Candida albicans strain CBS 562 26S ribosomal RNA gene, partial sequence",
            "length": "525",
            "url": [
                "https://www.ncbi.nlm.nih.gov/nuccore/AY497682"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "identifier sequence",
            "accession": "JN882343",
            "description": "Candida albicans strain NRRL Y-12983 18S ribosomal RNA gene, partial sequence; internal transcribed spacer 1, 5.8S ribosomal RNA gene, and internal transcribed spacer 2, complete sequence; and 28S ribosomal RNA gene, partial sequence",
            "length": "498",
            "url": [
                "https://www.ncbi.nlm.nih.gov/nuccore/JN882343"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "identifier sequence",
            "accession": "JN882349",
            "description": "Candida albicans strain NRRL Y-12983 28S ribosomal RNA gene, partial sequence",
            "length": "546",
            "url": [
                "https://www.ncbi.nlm.nih.gov/nuccore/JN882349"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "identifier sequence",
            "accession": "CAU45776",
            "description": "Candida albicans 26S ribosomal RNA gene, partial sequence",
            "length": "546",
            "url": [
                "https://www.ncbi.nlm.nih.gov/nuccore/CAU45776"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "genome",
            "accession": "GCA_015344825",
            "description": "Genome assembly ASM1534482",
            "length": "",
            "url": [
                "https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_015344825"
            ],
            "source": "/sources/0"
        }
    ],
    "gc": [
        {
            "method": null,
            "value": 33.5,
            "source": "/sources/0"
        }
    ],
    "literature": [
        {
            "name": null,
            "url": "https://doi.org/10.1099/00207713-51-4-1593",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": null,
            "url": "https://doi.org/10.1128/JCM.42.12.5624-5635.2004",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": null,
            "url": "https://doi.org/10.1128/jcm.35.5.1216-1223.1997",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": null,
            "url": "https://doi.org/10.1099/13500872-141-7-1523",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": null,
            "url": "https://doi.org/10.1007/BF02049775",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": null,
            "url": "https://doi.org/10.1016/S0723-2020(99)80030-7",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": null,
            "url": "https://doi.org/10.1128/JCM.37.6.1985-1993.1999",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        }
    ],
    "cell_wall": [
        {
            "name": "glucose",
            "identifier": [
                {
                    "name": "PubChem",
                    "value": "5793",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/5793"
                },
                {
                    "name": "ChEBI",
                    "value": "CHEBI:4167",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:4167"
                }
            ],
            "alternate_name": [
                "D-Glc",
                "D-Glucopyranose",
                "D-Glucopyranoside",
                "D-Glucose",
                "Glc",
                "Glucopyranose",
                "Glucopyranoside",
                "Glucose",
                "dextrose",
                "2280-44-6",
                "Grape sugar"
            ],
            "percent": null,
            "source": "/sources/0"
        },
        {
            "name": "mannose",
            "identifier": [
                {
                    "name": "PubChem",
                    "value": "18950",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/18950"
                },
                {
                    "name": "ChEBI",
                    "value": "CHEBI:4208",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:4208"
                }
            ],
            "alternate_name": [
                "D-Man",
                "D-Mannopyranose",
                "D-Mannopyranoside",
                "D-Mannose",
                "Man",
                "Mannopyranose",
                "Mannopyranoside",
                "Mannose",
                "Carubinose",
                "Seminose"
            ],
            "percent": null,
            "source": "/sources/0"
        }
    ],
    "fatty_acid_profiles": [],
    "stainings": [
        {
            "name": "Diazonium Blue B reaction",
            "value": "negative",
            "source": "/sources/0"
        }
    ],
    "hemolysis": [],
    "cultivation_media": [
        {
            "name": "GPYA",
            "url": null,
            "reagents": [
                "glucose",
                "peptone",
                "yeast extract",
                "agar",
                "distilled water"
            ],
            "source": "/sources/0"
        }
    ],
    "halophily": [
        {
            "name": "Sodium Chloride",
            "identifier": [
                {
                    "name": "PubChem",
                    "value": "5234",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/5234"
                },
                {
                    "name": "ChEBI",
                    "value": "CHEBI:26710",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:26710"
                }
            ],
            "alternate_name": [
                "Table salt",
                "sodium chloride",
                "ClNa"
            ],
            "optimal": null,
            "minimal": null,
            "maximal": null,
            "unit": "unknown",
            "tests": [
                {
                    "minimal": 10.0,
                    "maximal": 10.0,
                    "unit": "v/v%",
                    "growth": true
                },
                {
                    "minimal": 16.0,
                    "maximal": 16.0,
                    "unit": "v/v%",
                    "growth": false
                }
            ],
            "source": "/sources/0"
        }
    ],
    "tolerances": [
        {
            "name": "flucytosine",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": "CHEBI:5100",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:5100"
                },
                {
                    "name": "PubChem",
                    "value": "3366",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/3366"
                }
            ],
            "alternate_name": [
                "5-FC",
                "5FC",
                "5-Fluorocystosine",
                "5-Fluorocytosine",
                "Ancobon (TN)",
                "Ancobon"
            ],
            "reaction": "senisitive",
            "mic": "0.124",
            "unit": null,
            "tests": [],
            "source": "/sources/0"
        },
        {
            "name": "amphotericin B",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": "CHEBI:2682",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:2682"
                },
                {
                    "name": "PubChem",
                    "value": "14956",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/14956"
                }
            ],
            "alternate_name": [
                "Amphotericine B",
                "AMPH-B",
                "Liposomal Amphotericin B",
                "SCHEMBL1648719",
                "CHEMBL4785395"
            ],
            "reaction": "senisitive",
            "mic": "0.03",
            "unit": null,
            "tests": [],
            "source": "/sources/0"
        },
        {
            "name": "caspofungin",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": "CHEBI:474180",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:474180"
                }
            ],
            "alternate_name": [
                "Caspofungin"
            ],
            "reaction": "resistant",
            "mic": "8",
            "unit": null,
            "tests": [],
            "source": "/sources/0"
        }
    ],
    "enzymes": [],
    "metabolites": [
        {
            "name": "D-Glucose",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:4167",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:4167"
                },
                {
                    "name": "PubChem",
                    "value": "5793",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/5793"
                }
            ],
            "alternate_name": [
                "D-Glc",
                "D-Glucopyranose",
                "D-Glucopyranoside",
                "D-Glucose",
                "Glc",
                "Glucopyranose",
                "Glucopyranoside",
                "Glucose"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": "F1",
                    "utilization": null
                },
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": "C1",
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "Sucrose",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:17992",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17992"
                },
                {
                    "name": "PubChem",
                    "value": "5988",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/5988"
                }
            ],
            "alternate_name": [
                "sucrose",
                "57-50-1",
                "saccharose",
                "sugar",
                "Table sugar",
                "Cane sugar",
                "White sugar",
                "D-Sucrose"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": false,
                    "protocol": "F5",
                    "utilization": null
                },
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": "C1",
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "L-Sorbose",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:48649",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:48649"
                },
                {
                    "name": "PubChem",
                    "value": "439192",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/439192"
                }
            ],
            "alternate_name": [
                "L-Sor",
                "L-Sorbopyranose",
                "L-Sorbopyranoside",
                "L-Sorbose",
                "L-Xylo-Hex-2-ulo-Pyranose",
                "L-Xylo-Hexopyran-2-ulose",
                "Sor",
                "Sorbopyranose",
                "Sorbopyranoside",
                "Sorbose"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": "C3",
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        }
    ],
    "applications": [
        {
            "application": "US Patent 3,726,763",
            "source": "/sources/0"
        },
        {
            "application": "production of citric acid",
            "source": "/sources/0"
        }
    ],
    "collections": [
        {
            "name": "CBS",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/030a5r161",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "Westerdijk Fungal Biodiversity Institute",
            "address": null,
            "url": "https://wi.knaw.nl/",
            "email": null,
            "resource_num": "CBS 562",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo",
                "Agar"
            ],
            "history": null,
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        },
        {
            "name": "ATCC",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/03thhhv76",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "American Type Culture Collection",
            "address": null,
            "url": "http://www.atcc.org/",
            "email": null,
            "resource_num": "ATCC 18804",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo"
            ],
            "history": "ATCC <-- CBS <-- JE Mackinnon 572",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        },
        {
            "name": "CECT",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/043nxc105",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "Universitat de València",
            "address": null,
            "url": "https://www.uv.es/",
            "email": null,
            "resource_num": "CECT 1002",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo",
                "Agar",
                "DNA"
            ],
            "history": "CECT, 1987 < NCYC, 1960 < CBS < Mackinnon, J.E. No. 572",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        }
    ],
    "other_media": [
        {
            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a8/SEM_of_C_albicans.tif",
            "name": "SEM of C. albicans",
            "description": "C albicans visualised using scanning electron microscopy. Scanning electrom microscopy was performed at CenSE, IISc, Bangalore",
            "usage": "Vader1941 at English Wikipedia, CC BY-SA 4.0",
            "additional_type": null,
            "source": "/sources/0"
        }
    ],
    "sources": [
        {
            "name": "CBS",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/030a5r161",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "Westerdijk Fungal Biodiversity Institute",
            "address": null,
            "url": "https://wi.knaw.nl/page/fungal_display/309",
            "email": null,
            "resource_id": null
        }
    ]
}
```
