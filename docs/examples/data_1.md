# Bacteria

This is a example data for a bacterium. The data is artificial and should only demonstrate
what the data in this schema look like.

```JSON
{
    "id": 1,
    "last_update": "2024-07-15T00:00:00Z",
    "organism_type": "Bacteria",
    "morph_type": null,
    "type_strain": true,
    "taxon": {
        "name": "Eubacterium limosum",
        "rank": "species",
        "status": "validly published",
        "identifier": [
            {
                "name": "LPSN",
                "value": "https://lpsn.dsmz.de/species/eubacterium-limosum",
                "property": "https://www.wikidata.org/wiki/Property:P1991",
                "url": "https://lpsn.dsmz.de/species/eubacterium-limosum"
            },
            {
                "name": "NCBI:txid",
                "value": "1736",
                "property": "https://www.wikidata.org/wiki/Property:P685",
                "url": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1736"
            }
        ],
        "scientific": {
            "name": "Eubacterium limosum",
            "author": "(Eggerth 1935) Prévot 1938 (Approved Lists 1980)"
        },
        "alternate_name": [
            "Butyribacterium limosum",
            "Bacteroides limosus"
        ],
        "parent": {
            "name": "Eubacterium",
            "rank": "genus",
            "status": "validly published",
            "identifier": [
                {
                    "name": "LPSN",
                    "value": "https://lpsn.dsmz.de/genus/eubacterium",
                    "property": "https://www.wikidata.org/wiki/Property:P1991",
                    "url": "https://lpsn.dsmz.de/genus/eubacterium"
                }
            ],
            "scientific": {
                "name": "Eubacterium",
                "author": "Prévot 1938 (Approved Lists 1980)"
            },
            "alternate_name": [],
            "parent": null,
            "same_as": []
        },
        "same_as": [
            "https://www.gbif.org/species/3226415/metrics"
        ]
    },
    "sample": [
        {
            "date": "/2011-09-12",
            "country": null,
            "description": "soil of landfill site",
            "location": {
                "name": "Pohang",
                "description": null,
                "geo": {
                    "latitude": 36.03901723905223,
                    "longitude": 129.365704500591,
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
            "isolator": {
                "name": "Korea Research Institute of Bioscience and Biotechnology",
                "identifier": [
                    {
                        "name": "ROR",
                        "value": "https://ror.org/03ep23f07",
                        "property": "https://www.wikidata.org/wiki/Property:P6782",
                        "url": null
                    }
                ],
                "legal_name": null,
                "address": null,
                "url": null,
                "email": null
            },
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
            "cell_shape": "coccus",
            "source": "/sources/0"
        }
    ],
    "oxygen": [
        {
            "relation": "anerobe",
            "source": "/sources/0"
        }
    ],
    "multi_cell": [
        {
            "multi_cell": true,
            "source": "/sources/0"
        }
    ],
    "cell_length": [
        {
            "min": 1.3,
            "max": 2.2,
            "unit": "µm",
            "source": "/sources/0"
        }
    ],
    "cell_width": [
        {
            "min": 0.5,
            "max": 0.8,
            "unit": "µm",
            "source": "/sources/0"
        }
    ],
    "cell_motility": [
        {
            "motile": true,
            "flagellum": true,
            "flag_arr": null,
            "gliding": false,
            "source": "/sources/0"
        }
    ],
    "colony": [],
    "spore": [
        {
            "building": true,
            "type": "endospore",
            "ejection": null,
            "source": "/sources/0"
        }
    ],
    "temperature": [
        {
            "optimal": 37.0,
            "minimal": null,
            "maximal": null,
            "unit": "C",
            "tests": [
                {
                    "minimal": 30.0,
                    "maximal": 39.0,
                    "unit": "C",
                    "growth": true
                },
                {
                    "minimal": 45.0,
                    "maximal": 43.0,
                    "unit": "C",
                    "growth": false
                }
            ],
            "source": "/sources/0"
        }
    ],
    "ph": [
        {
            "optimal": 7.0,
            "minimal": null,
            "maximal": null,
            "unit": "pH",
            "tests": [
                {
                    "minimal": 6.0,
                    "maximal": 9.0,
                    "unit": "pH",
                    "growth": true
                }
            ],
            "source": "/sources/0"
        }
    ],
    "identifier": [
        {
            "name": "CCNO",
            "value": "DSM 20543",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "ATCC 8486",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "NCIB 9763",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "CCUG 16793",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "JCM 6421",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "BCRC 14401",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "CIP 104169",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "JCM 9978",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "KCTC 3266",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "CCNO",
            "value": "NCIMB 9763",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "Designation",
            "value": "STAFF 1027",
            "property": null,
            "url": null,
            "source": "/sources/0"
        },
        {
            "name": "BacDiveID",
            "value": "5432",
            "property": "https://www.wikidata.org/wiki/Property:P2946",
            "url": "https://bacdive.dsmz.de/strain/5432",
            "source": "/sources/0"
        },
        {
            "name": "SI-ID",
            "value": "34969",
            "property": null,
            "url": "https://straininfo.dsmz.de/strain/34969",
            "source": "/sources/0"
        }
    ],
    "connected_persons": [
        {
            "name": "J.-W. Bae",
            "identifier": [
                {
                    "name": "ORCiD",
                    "value": "https://orcid.org/0000-0001-6433-5270",
                    "property": "https://www.wikidata.org/wiki/Property:P496",
                    "url": null
                }
            ],
            "role": "isolator",
            "source": "/sources/0"
        }
    ],
    "pathogenicity": [
        {
            "host": "human",
            "pathogen": "opportunistic",
            "classification": "German classification",
            "source": "/sources/0"
        },
        {
            "host": "animal",
            "pathogen": "no pathogen",
            "classification": "German classification",
            "source": "/sources/0"
        },
        {
            "host": "plant",
            "pathogen": "no pathogen",
            "classification": "German classification",
            "source": "/sources/0"
        }
    ],
    "bio_safety": [
        {
            "group": "1",
            "classification": "German classification",
            "url": "https://www.baua.de/EN/Service/Legislative-texts-and-technical-rules/Rules/TRBA/TRBA-466.html",
            "source": "/sources/0"
        },
        {
            "group": "1",
            "classification": "Japan classification",
            "url": null,
            "source": "/sources/0"
        }
    ],
    "sequences": [
        {
            "type": "nucleotide",
            "level": "identifier sequence",
            "accession": "LC019782",
            "description": "Eubacterium limosum gene for 16S ribosomal RNA, partial sequence, strain: JCM 9978",
            "length": "1425",
            "url": [
                "https://www.ncbi.nlm.nih.gov/nuccore/LC019782",
                "https://www.ebi.ac.uk/ena/browser/view/LC019782"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "identifier sequence",
            "accession": "M59120",
            "description": "Eubacterium limosum strain ATCC 8486 16S ribosomal RNA gene, partial sequence",
            "length": "1525",
            "url": [
                "https://www.ncbi.nlm.nih.gov/nuccore/M59120",
                "https://www.ebi.ac.uk/ena/browser/view/M59120",
                "https://www.arb-silva.de/browser/ssu/M59120"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "identifier sequence",
            "accession": "AB595134",
            "description": "Eubacterium limosum gene for 16S ribosomal RNA, partial sequence, strain: JCM 6421",
            "length": "1484",
            "url": [
                "https://www.ncbi.nlm.nih.gov/nuccore/AB595134",
                "https://www.ebi.ac.uk/ena/browser/view/AB595134",
                "https://www.arb-silva.de/browser/ssu/AB595134"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "genome",
            "accession": "GCA_000807675",
            "description": "Eubacterium limosum ATCC 8486",
            "length": null,
            "url": [
                "https://www.ncbi.nlm.nih.gov/assembly/GCA_000807675",
                "https://www.ebi.ac.uk/ena/browser/view/GCA_000807675"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "gene",
            "accession": "1736.3",
            "description": "Eubacterium limosum ATCC 8480",
            "length": null,
            "url": [
                "https://www.patricbrc.org/view/Genome/1736.3"
            ],
            "source": "/sources/0"
        },
        {
            "type": "nucleotide",
            "level": "genome",
            "accession": "2814123220",
            "description": "Eubacterium limosum ATCC 8486",
            "length": null,
            "url": [
                "https://img.jgi.doe.gov/cgi-bin/m/main.cgi?section=TaxonDetail&page=taxonDetail&taxon_oid=2814123220"
            ],
            "source": "/sources/0"
        }
    ],
    "gc": [
        {
            "method": "thermal denaturion, midpoint method (Tm)",
            "value": 47.8,
            "source": "/sources/0"
        }
    ],
    "literature": [
        {
            "name": "Something",
            "url": "https://doi.org/10.1128/JB.30.3.277-299.1935",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": "Something different",
            "url": "https://doi.org/10.1128/AEM.62.4.1242-1247.1996",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        },
        {
            "name": "Something completely different",
            "url": "https://doi.org/10.1099/00207713-44-4-787",
            "date": null,
            "author": [],
            "publisher": [],
            "source": "/sources/0"
        }
    ],
    "cell_wall": [
        {
            "name": "B04",
            "identifier": [],
            "alternate_name": [
                "B2alpha {L-Ser} [L-Orn] D-Glu-D-Lys(D-Orn)"
            ],
            "percent": null,
            "source": "/sources/0"
        }
    ],
    "fatty_acid_profiles": [
        {
            "profile": [
                {
                    "name": "C15:0 ISO",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 31.9,
                    "ecl": "14.621"
                },
                {
                    "name": "C16:0",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 14.0,
                    "ecl": "16"
                },
                {
                    "name": "C17:1 ISO I/C16:0 DMA",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 9.7,
                    "ecl": "16.481"
                },
                {
                    "name": "C15:0 ANTEISO",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 6.7,
                    "ecl": "14.711"
                },
                {
                    "name": "C18:2 ω6,9c/C18:0 ANTE",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 5.4,
                    "ecl": "17.724"
                },
                {
                    "name": "C14:0 ISO 3OH",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 5.3,
                    "ecl": "15.117"
                },
                {
                    "name": "C14:0",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 4.2,
                    "ecl": "14"
                },
                {
                    "name": "unknown 14.966",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 3.9,
                    "ecl": "14.966"
                },
                {
                    "name": "unknown 18.177",
                    "identifier": [],
                    "alternate_name": [],
                    "percent": 3.3,
                    "ecl": "18.177"
                }
            ],
            "temperature": 37,
            "medium": "blood Agar",
            "library": "BHIBLA",
            "software": "Sherlock 6.1",
            "source": "/sources/0"
        }
    ],
    "stainings": [
        {
            "name": "Gram stain",
            "value": "negative",
            "source": "/sources/0"
        }
    ],
    "hemolysis": [
        {
            "blood": "sheep",
            "hemolysis": "alpha",
            "source": "/sources/0"
        },
        {
            "blood": "horse",
            "hemolysis": "beta",
            "source": "/sources/0"
        }
    ],
    "cultivation_media": [
        {
            "name": "PYG MEDIUM (MODIFIED) (DSMZ Medium 104)",
            "url": "https://mediadive.dsmz.de/medium/104?bacdive=5432",
            "reagents": [
                "Yeast extract",
                "Peptone",
                "Glucose",
                "Trypticase peptone",
                "Beef extract",
                "L-Cysteine HCl x H2O",
                "NaHCO3",
                "NaCl",
                "KH2PO4",
                "K2HPO4",
                "MgSO4 x 7 H2O",
                "CaCl2 x 2 H2O",
                "Hemin",
                "Ethanol",
                "Resazurin",
                "Tween 80",
                "Vitamin K1",
                "NaOH",
                "Distilled water"
            ],
            "source": "/sources/0"
        },
        {
            "name": "CIP Medium 187",
            "url": "https://catalogue-crbip.pasteur.fr/fiche_milieu.xhtml?crbip=187",
            "reagents": [],
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
            "optimal": 0.0,
            "minimal": null,
            "maximal": null,
            "unit": "g/g%",
            "tests": [
                {
                    "minimal": 0.0,
                    "maximal": 1.0,
                    "unit": "g/g%",
                    "growth": true
                }
            ],
            "source": "/sources/0"
        }
    ],
    "tolerances": [
        {
            "name": "amikacin",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": "CHEBI:2637",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:2637"
                }
            ],
            "alternate_name": [
                "1-N-(L(−)-γ-amino-α-hydroxybutyryl)kanamycin A",
                "Amikacin",
                "O-3-amino-3-deoxy-α-D-glucopyranosyl-(1→4)-O-(6-amino-6-deoxy-α-D-glucopyranosyl-(1→6))-N3-(4-amino-L-2-hydroxybutyryl)-2-deoxy-L-streptamine"
            ],
            "reaction": null,
            "mic": null,
            "unit": null,
            "tests": [
                {
                    "reaction": "sensitive",
                    "concentration": "30",
                    "unit": "g/L"
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "ampicillin",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": "CHEBI:28971",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:28971"
                }
            ],
            "alternate_name": [
                "AP",
                "AMP",
                "ABPC",
                "Ampicillin",
                "ampicillin acid",
                "ampicillin anhydrous"
            ],
            "reaction": null,
            "mic": null,
            "unit": null,
            "tests": [
                {
                    "reaction": "resistant",
                    "concentration": "10",
                    "unit": "g/L"
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "cefuroxime",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": "CHEBI:3515",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:3515"
                }
            ],
            "alternate_name": [
                "Sharox",
                "Zinacef Danmark",
                "Cefuroxim",
                "Cefuroxime",
                "Cephuroxime"
            ],
            "reaction": null,
            "mic": null,
            "unit": null,
            "tests": [
                {
                    "reaction": "intermediate",
                    "concentration": "30",
                    "unit": "g/L"
                }
            ],
            "source": "/sources/0"
        }
    ],
    "enzymes": [
        {
            "name": "acid phosphatase",
            "ec_num": "3.1.3.2",
            "url": "https://www.brenda-enzymes.org/enzyme.php?ecno=3.1.3.2",
            "alternate_name": [
                "acid phosphatase",
                "tartrate-resistant acid phosphatase",
                "prostatic acid phosphatase",
                "tracp",
                "acpase",
                "uteroferrin",
                "tracp 5b",
                "phosphatidic acid phosphatase",
                "tracp5b"
            ],
            "active": true,
            "source": "/sources/0"
        },
        {
            "name": "alkaline phosphatase",
            "ec_num": "3.1.3.1",
            "url": "https://www.brenda-enzymes.org/enzyme.php?ecno=3.1.3.1",
            "alternate_name": [
                "ap",
                "alkaline phosphatase",
                "bone alkaline phosphatase",
                "placental alkaline phosphatase",
                "alpase",
                "apase",
                "intestinal alkaline phosphatase",
                "tnsalp",
                "phosphomonoesterase",
                "secreted alkaline phosphatase"
            ],
            "active": true,
            "source": "/sources/0"
        },
        {
            "name": "alpha-chymotrypsin",
            "ec_num": "3.4.21.1",
            "url": "https://www.brenda-enzymes.org/enzyme.php?ecno=3.4.21.1",
            "alternate_name": [
                "chymotrypsin",
                "alpha-chymotrypsin",
                "bovine alpha-chymotrypsin",
                "chymotrypsin a",
                "alpha-ct",
                "chymotrypsin b",
                "chtp",
                "alpha chymotrypsin",
                "alpha-chymotrypsin a",
                "chymotrypsin ii"
            ],
            "active": false,
            "source": "/sources/0"
        },
        {
            "name": "alpha-fucosidase",
            "ec_num": "3.2.1.51",
            "url": "https://www.brenda-enzymes.org/enzyme.php?ecno=3.2.1.51",
            "alternate_name": [
                "alpha-l-fucosidase",
                "acid hydrolase",
                "fuca1",
                "serum alpha-l-fucosidase",
                "serum afu",
                "alpha-fuc",
                "fuca2",
                "alf1_wf",
                "alpha-l-fucosidase i",
                "alphafuc"
            ],
            "active": false,
            "source": "/sources/0"
        },
        {
            "name": "arginine dihydrolase",
            "ec_num": "3.5.3.6",
            "url": "https://www.brenda-enzymes.org/enzyme.php?ecno=3.5.3.6",
            "alternate_name": [
                "arginine deiminase",
                "arginine dihydrolase",
                "ppadi",
                "arginine-degrading enzyme",
                "l-arginine deiminase",
                "arca-1",
                "lymphocyte blastogenesis inhibitory factor",
                "paadi",
                "streptococcal acid glycoprotein"
            ],
            "active": false,
            "source": "/sources/0"
        },
        {
            "name": "beta-galactosidase",
            "ec_num": "3.2.1.23",
            "url": "https://www.brenda-enzymes.org/enzyme.php?ecno=3.2.1.23",
            "alternate_name": [
                "beta-galactosidase",
                "beta-gal",
                "beta-d-galactosidase",
                "senescence-associated beta-galactosidase",
                "endo-beta-galactosidase",
                "bglap",
                "sa-beta-gal",
                "acid beta-galactosidase",
                "beta galactosidase",
                "betagal"
            ],
            "active": true,
            "source": "/sources/0"
        }
    ],
    "metabolites": [
        {
            "name": "alanine",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:16449",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:16449"
                },
                {
                    "name": "PubChem",
                    "value": "5950",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/5950"
                }
            ],
            "alternate_name": [
                "L-alanine",
                "Alinine",
                "2-Aminopropanoic acid",
                "2-aminopropanoic acid",
                "Alanine"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "asparagine",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:22653",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:22653"
                },
                {
                    "name": "PubChem",
                    "value": "6267",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/6267"
                }
            ],
            "alternate_name": [
                "L-asparagine",
                "asparagine"
            ],
            "tests": [
                {
                    "type": "production",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                },
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "aspartate",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:35391",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:35391"
                },
                {
                    "name": "PubChem",
                    "value": "5460542",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/5460542"
                }
            ],
            "alternate_name": [
                "aspartate(1-)",
                "hydrogen aspartate",
                "2-ammoniosuccinate",
                "2-ammoniobutanedioate",
                "aspartic acid monoanion",
                "CHEBI:35391",
                "FT-0653860",
                "FT-0657391"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "formate",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:15740",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:15740"
                }
            ],
            "alternate_name": [
                "aminate",
                "formate",
                "formiate",
                "formic acid, ion(1−)",
                "formylate",
                "HCO2 anion",
                "hydrogen carboxylate",
                "methanoate"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "glucose",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:17234",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17234"
                }
            ],
            "alternate_name": [
                "DL-glucose",
                "Glc",
                "Glucose",
                "Glukose"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "glutamate(2-)",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:29987",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:29987"
                }
            ],
            "alternate_name": [
                "glutamate(2−)",
                "glutamic acid dianion"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "nitrate",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:17632",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17632"
                },
                {
                    "name": "PubChem",
                    "value": "943",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/943"
                }
            ],
            "alternate_name": [
                "[NO3]−",
                "nitrate",
                "NITRATE ION",
                "NO3−",
                "nitrate(1−)",
                "NO3",
                "CHEMBL186200",
                "NITRATO",
                "trioxonitrate(1-)"
            ],
            "tests": [
                {
                    "type": "utilization",
                    "active": true,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        },
        {
            "name": "indole",
            "identifier": [
                {
                    "name": "ChEBI",
                    "value": " CHEBI:17632",
                    "property": "https://wikidata.org/wiki/Property:P683",
                    "url": "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17632"
                },
                {
                    "name": "PubChem",
                    "value": "943",
                    "property": "https://wikidata.org/wiki/Property:P662",
                    "url": "https://pubchem.ncbi.nlm.nih.gov/compound/943"
                }
            ],
            "alternate_name": [
                "[NO3]−",
                "nitrate",
                "NITRATE ION",
                "NO3−",
                "nitrate(1−)",
                "NO3",
                "CHEMBL186200",
                "NITRATO",
                "trioxonitrate(1-)"
            ],
            "tests": [
                {
                    "type": "production",
                    "active": false,
                    "protocol": null,
                    "utilization": null
                }
            ],
            "source": "/sources/0"
        }
    ],
    "applications": [
        {
            "application": "Production of substance x",
            "source": "/sources/0"
        },
        {
            "application": "Degradation of substance y",
            "source": "/sources/0"
        }
    ],
    "collections": [
        {
            "name": "DSMZ",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/02tyer376",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "Leibniz-Institut DSMZ-Deutsche Sammlung von Mikroorganismen und Zellkulturen GmbH",
            "address": null,
            "url": "https://www.dsmz.de/",
            "email": null,
            "resource_num": "DSMZ 20543",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo",
                "Agar",
                "DNA"
            ],
            "history": "<- KCTC <- J.-W. Bae, KRIBB",
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
            "url": "https://www.atcc.org/",
            "email": null,
            "resource_num": "ATCC 8486",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo"
            ],
            "history": "<- AH Eggerth",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        },
        {
            "name": "JCM",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/00s05em53",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "RIKEN BioResource Research Center",
            "address": null,
            "url": "https://jcm.brc.riken.jp/en/",
            "email": null,
            "resource_num": "JCM 9978",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo",
                "Agar"
            ],
            "history": "<-- STAFF 1027 <-- ATCC 8486 <-- A. H. Eggerth",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        },
        {
            "name": "JCM",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/00s05em53",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "RIKEN BioResource Research Center",
            "address": null,
            "url": "https://jcm.brc.riken.jp/en/",
            "email": null,
            "resource_num": "JCM 6421",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo",
                "Agar"
            ],
            "history": "<-- T. Mitsuoka <-- ATCC 8486 <-- A. H. Eggerth",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        },
        {
            "name": "Korean Collection for Type Cultures",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/03ep23f07",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "Korea Research Institute of Bioscience and Biotechnology",
            "address": null,
            "url": "http://www.kribb.re.kr/eng/",
            "email": null,
            "resource_num": "KCTC 3266",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [
                "Lyo",
                "Agar"
            ],
            "history": "<- JH Kim <- ATCC <- AH Eggerth, `Bacteroides limosus`",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        },
        {
            "name": "Culture Collection University Of Gothenburg",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/01tm6cn81",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "University Of Gothenburg",
            "address": null,
            "url": "https://www.ccug.se/",
            "email": null,
            "resource_num": "CCUG 16793",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [],
            "history": "<- DSM <- ATCC <- A.H.Eggerth",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        },
        {
            "name": "Collection of Institut Pasteur",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/0495fxg12",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "Biological Resource Center of Institut Pasteur (CRBIP)",
            "address": null,
            "url": "https://catalogue-crbip.pasteur.fr/",
            "email": null,
            "resource_num": "CIP 104169",
            "available": true,
            "catalog_link": null,
            "restrictions": null,
            "axenic": true,
            "supply_forms": [],
            "history": "1994, ATCC <- A.H. Eggerth, Bacteroides limosus",
            "date": null,
            "depositor": null,
            "source": "/sources/0"
        }
    ],
    "other_media": [
        {
            "url": "https://cdn.dsmz.de/images/strain/2979/EM_DSM_14619_1.jpg",
            "name": "EM_DSM_14619_1.jpg",
            "description": "Electron microscopic image",
            "usage": null,
            "additional_type": "image",
            "source": "/sources/0"
        }
    ],
    "sources": [
        {
            "name": "BacDive",
            "identifier": [
                {
                    "name": "ROR",
                    "value": "https://ror.org/02tyer376",
                    "property": "https://www.wikidata.org/wiki/Property:P6782",
                    "url": null
                }
            ],
            "legal_name": "Leibniz-Institut DSMZ-Deutsche Sammlung von Mikroorganismen und Zellkulturen GmbH",
            "address": null,
            "url": "https://bacdive.dsmz.de/strain/2904",
            "email": null,
            "resource_id": null
        }
    ]
}
```
