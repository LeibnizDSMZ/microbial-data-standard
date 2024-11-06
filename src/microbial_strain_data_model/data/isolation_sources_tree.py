from anytree import Node

# Tree structure of Isolation Source Tags
# root node
root = Node("IsolationSources")


# Environmental
environmental = Node(
    "#Environmental",
    parent=root,
    children=[
        Node("#Air", children=[Node("#Indoor Air"), Node("#Outdoor Air")]),
        Node(
            "#Aquatic",
            children=[
                Node("#Brackish"),
                Node("#Cave water"),
                Node("#Coral reef"),
                Node("#Estuary"),
                Node("#Foam"),
                Node("#Freshwater"),
                Node("#Geologic"),
                Node("#Groundwater"),
                Node("#Hydrothermal vent"),
                Node("#Ice"),
                Node("#Lake (large)"),
                Node("#Mangrove"),
                Node("#Marine"),
                Node("#Non-marine Saline and Alkaline"),
                Node("#Pond (small)"),
                Node("#River (Creek)"),
                Node("#Sediment"),
                Node("#Spring"),
                Node("#Surface water"),
                Node("#Thermal spring"),
            ],
        ),
        Node("#Biofilm", children=[Node("#Iron mat")]),
        Node(
            "#Microbial community",
            children=[
                Node("#Bacteriome"),
                Node("#Co-culture"),
                Node("#Decomposing algae"),
                Node("#Decomposing fungi"),
                Node("#Microbial mat"),
            ],
        ),
        Node(
            "#Terrestrial",
            children=[
                Node("#Coast"),
                Node("#Core sample"),
                Node("#Desert"),
                Node("#Dust"),
                Node("#Forest"),
                Node("#Geologic"),
                Node("#Glacier"),
                Node("#Grassland"),
                Node("#Mud (Sludge)"),
                Node("#Permafrost"),
                Node("#Salt marsh"),
                Node("#Sandy"),
                Node("#Sediment"),
                Node("#Soil"),
                Node("#Tidal flat"),
                Node("#Tundra"),
                Node("#Volcanic"),
                Node("#Wetland (Swamp)"),
            ],
        ),
    ],
)

# Engineered
engineered = Node(
    "#Engineered",
    parent=root,
    children=[
        Node(
            "#Agriculture",
            children=[
                Node("#Field"),
                Node("#Garden"),
                Node("#Greenhouse"),
                Node("#Grove (Orchard)"),
                Node("#Livestock (Husbandry)"),
                Node("#Meadow"),
                Node("#Paddy (Ricefield)"),
                Node("#Park (City)"),
                Node("#Plantation"),
                Node("#Vineyard"),
            ],
        ),
        Node(
            "#Biodegradation",
            children=[
                Node("#Anaerobic digestor"),
                Node("#Composting"),
                Node("#Decomposing material"),
                Node("#Garden dump"),
            ],
        ),
        Node(
            "#Bioreactor",
        ),
        Node(
            "#Bioremediation",
            children=[Node("#Biofilter"), Node("#Ex situ"), Node("#In situ")],
        ),
        Node(
            "#Built environment",
            children=[
                Node("#Air conditioner"),
                Node("#Animal habitation (Nest,Burrow)"),
                Node("#City"),
                Node("#Clean room"),
                Node("#Container (Reservoir)"),
                Node("#House"),
                Node("#Indoor"),
                Node("#Surface swab"),
                Node("#Transportation ways (Roads)"),
                Node("#Water reservoir (Aquarium/pool)"),
            ],
        ),
        Node(
            "#Contamination",
            children=[Node("#Heavy metal"), Node("#Oil (Fuel)"), Node("#Pesticide")],
        ),
        Node(
            "#Food production",
            children=[
                Node("#Aquaculture"),
                Node("#Beverage"),
                Node("#Bottled, canned, packed food"),
                Node("#Dairy product"),
                Node("#Egg"),
                Node("#Fermented"),
                Node("#Food"),
                Node("#Meat"),
                Node("#Oil (Food)"),
                Node("#Seafood"),
                Node("#Spoiled"),
                Node("#Starter culture"),
                Node("#Sugary food"),
                Node("#Vegetable (incl. Grains)"),
            ],
        ),
        Node(
            "#Industrial",
            children=[
                Node("#Cooling tower"),
                Node("#Engineered product"),
                Node("#Industrial production"),
                Node("#Machines and devices"),
                Node("#Oil reservoir"),
                Node("#Plant (Factory)"),
            ],
        ),
        Node(
            "#Laboratory",
            children=[
                Node("#Contaminant"),
                Node("#Defined media"),
                Node("#Lab enrichment"),
                Node("#Lab synthesis"),
                Node("#Simulated communities"),
            ],
        ),
        Node(
            "#Other",
            children=[
                Node("#Currency"),
                Node("#Mine"),
                Node("#Painting"),
            ],
        ),
        Node(
            "#Treatment",
            children=[
                Node("#Frozen"),
                Node("#Heated (Burned)"),
                Node("#Preserved"),
                Node("#Sterilized (Desinfected)"),  # this is wrong - Disinfected
            ],
        ),
        Node(
            "#Waste",
            children=[
                Node("#Activated sludge"),
                Node("#Coalbed water"),
                Node("#Domestic waste"),
                Node("#Dust (Ash)"),
                Node("#Industrial waste"),
                Node("#Industrial wastewater"),
                Node("#Landfill"),
                Node("#Sewage sludge"),
                Node("#Solid animal waste"),
                Node("#Solid plant waste"),
                Node("#Solid waste"),
                Node("#Waste gas"),
                Node("#Wastewater"),
                Node("#Water treatment plant"),
            ],
        ),
    ],
)
host = Node(
    "#Host",
    parent=root,
    children=[
        Node(
            "#Algae",
            children=[
                Node("#Brown Algae"),
                Node("#Green algae"),
                Node("#Red algae"),
            ],
        ),
        Node("#Amphibia"),
        Node(
            "#Arthropoda",
            children=[
                Node("#Crustacea"),
                Node("#Insecta"),
                Node("#Tick"),
            ],
        ),
        Node("#Birds", children=[Node("#Chicken")]),
        Node("#Fishes", children=[Node("#Salmonidae"), Node("#Zebrafish")]),
        Node(
            "#Fungi",
            children=[
                Node("#Mushroom"),
                Node("#Mycelium"),
                Node("#Mycorrhiza"),
                Node("#Rot fungi"),
                Node("#Slime mold"),
                Node("#Symbiotic fungal garden and gallery"),
            ],
        ),
        Node(
            "#Human",
            children=[
                Node("#Child"),
                Node("#Female"),
                Node("#Male"),
            ],
        ),
        Node(
            "#Invertebrates (Other)",
            children=[
                Node("#Annelida"),
                Node("#Cnidaria (Corals)"),
                Node("#Echinodermata"),
                Node("#Mollusca"),
                Node("#Nematoda"),
                Node("#Porifera (Sponges)"),
                Node("#Tunicata"),
            ],
        ),
        Node("#Juvenile"),
        Node(
            "#Mammals",
            children=[
                Node("#Aquatic mammal"),
                Node("#Bovinae (Cow, Cattle)"),
                Node("#Canidae (Dog)"),
                Node("#Caprinae (Sheep/Goat)"),
                Node("#Equidae (Horse)"),
                Node("#Felidae (Cat)"),
                Node("#Leporidae (Rabbit/Hare)"),
                Node("#Muridae (Mouse/Rat)"),
                Node("#Primates"),
                Node("#Rodentia (Other)"),
                Node("#Suidae (Pig,Swine)"),
            ],
        ),
        Node(
            "#Microbial",
            children=[
                Node("#Bacteria"),
                Node("#Oomycota (Water moulds)"),
                Node("#Phytoplankton"),
                Node("#Viriome"),
                Node("#Zooplankton"),
            ],
        ),
        Node(
            "#Other",
            children=[
                Node("#Decomposing animal"),
                Node("#Ectosymbiont"),
                Node("#Endosymbiont"),
                Node("#Epibiont"),
                Node("#Extracellular"),
                Node("#Intracellular"),
                Node("#Lichen"),
                Node("#Parasite"),
            ],
        ),
        Node(
            "#Plants",
            children=[
                Node("#Aquatic plant"),
                Node("#Decomposing plant"),
                Node("#Herbaceous plants (Grass,Crops)"),
                Node("#Liana (Vine)"),
                Node("#Moss"),
                Node("#Peat moss"),
                Node("#Shrub (Scrub)"),
                Node("#Tree"),
                Node("#Xerophytic"),
            ],
        ),
        Node(
            "#Protozoa",
            children=[
                Node("#Dinoflagellate"),
                Node("#Protist"),
            ],
        ),
        Node("#Reptilia"),
        Node("#Yeast"),
    ],
)
host_body_site = Node(
    "#Host Body-Site",
    parent=root,
    children=[
        Node(
            "#Gastrointestinal tract",
            children=[
                Node("#Large intestine"),
                Node("#Rectum"),
                Node("#Small intestine"),
                Node("#Stomach"),
            ],
        ),
        Node(
            "#Limb",
            children=[
                Node("#Ankle"),
                Node("#Arm"),
                Node("#Foot"),
                Node("#Hand"),
                Node("#Joint"),
                Node("#Leg"),
            ],
        ),
        Node(
            "#Oral cavity and airways",
            children=[
                Node("#Airways"),
                Node("#Gingiva"),
                Node("#Lung"),
                Node("#Mouth"),
                Node("#Periodontal pocket"),
                Node("#Plaque"),
                Node("#Root (Tooth)"),
                Node("#Subgingival plaque"),
                Node("#Throat"),
                Node("#Tooth"),
                Node("#Trachea"),
            ],
        ),
        Node(
            "#Organ",
            children=[
                Node("#Brain"),
                Node("#Ear"),
                Node("#Eye"),
                Node("#Heart"),
                Node("#Liver"),
                Node("#Lymph node"),
                Node("#Mammary gland"),
                Node("#Nose"),
                Node("#Rumen"),
                Node("#Skin, Nail, Hair"),
                Node("#Spinal Cord"),
                Node("#Spleen"),
                Node("#Vascular system"),
            ],
        ),
        Node(
            "#Other",
            children=[
                Node("#Abdomen"),
                Node("#Abscess"),
                Node("#Bone"),
                Node("#Head"),
                Node("#Thoracic segment"),
                Node("#Torso"),
                Node("#Wound"),
            ],
        ),
        Node(
            "#Plant",
            children=[
                Node("#Bark"),
                Node("#Endosphere"),
                Node("#Flower"),
                Node("#Fruit (Seed)"),
                Node("#Leaf (Phyllosphere)"),
                Node("#Phylloplane"),
                Node("#Rhizoplane"),
                Node("#Rhizosphere"),
                Node("#Root (Rhizome)"),
                Node("#Root nodule"),
                Node("#Stem (Branch)"),
                Node("#Sterilized plant part"),
            ],
        ),
        Node(
            "#Urogenital tract",
            children=[
                Node("#Bladder"),
                Node("#Kidney"),
                Node("#Nephridium"),
                Node("#Ovary"),
                Node("#Urethra"),
                Node("#Vagina"),
            ],
        ),
    ],
)
host_body_product = Node(
    "#Host Body Product",
    parent=root,
    children=[
        Node(
            "#Fluids",
            children=[
                Node("#Aspirate"),
                Node("#Blood"),
                Node("#Cerebrospinal fluid"),
                Node("#Furuncle fluid"),
                Node("#Milk"),
                Node("#Rumen fluid"),
                Node("#Sputum"),
                Node("#Synovial fluid"),
                Node("#Urine"),
                Node("#Wound fluid"),
            ],
        ),
        Node(
            "#Gastrointestinal tract",
            children=[
                Node("#Caecal content"),
                Node("#Feces (Stool)"),
                Node("#Vomit"),
            ],
        ),
        Node(
            "#Oral cavity and Airways",
            children=[
                Node("#Bronchial wash"),
                Node("#Dental plaque"),
                Node("#Mucus"),
                Node("#Nasopharyngeal aspirate"),
                Node("#Phlegm"),
                Node("#Pleural fluid"),
                Node("#Saliva"),
                Node("#Tracheal aspirate"),
            ],
        ),
        Node("#Other", children=[Node("#Animal produced food (natural)")]),
        Node(
            "#Plant",
            children=[
                Node("#Cotton (other fibres)"),
                Node("#Digestive fluid"),
                Node("#Juice (natural)"),
                Node("#Nectar"),
                Node("#Plant exudate (Resin)"),
                Node("#Plant litter (Forest)"),
                Node("#Plant sap (Flux)"),
                Node("#Pollen"),
                Node("#Straw"),
                Node("#Timber"),
            ],
        ),
        Node(
            "#Urogenital tract",
            children=[
                Node("#Abort"),
                Node("#Amniotic fluid"),
                Node("#Bladder stone"),
                Node("#Egg"),
                Node("#Semen"),
                Node("#Vaginal secretion"),
            ],
        ),
    ],
)
infection = Node(
    "#Infection",
    parent=root,
    children=[
        Node(
            "#Disease",
            children=[
                Node("#Cystic fibrosis"),
                Node("#Meningitis"),
                Node("#Mycosis"),
                Node("#Post mortem"),
                Node("#Tuberculosis"),
            ],
        ),
        Node("#Inflammation"),
        Node(
            "#Medical device",
            children=[
                Node("#Catheter"),
                Node("#Heart valve"),
            ],
        ),
        Node(
            "#Medical environment",
            children=[
                Node("#Clinic"),
                Node("#Medical practice"),
            ],
        ),
        Node("#Medical product"),
        Node("#Outbreak"),
        Node(
            "#Patient",
            children=[
                Node("#Antibiotic treatment"),
                Node("#Biopsy"),
                Node("#Blood culture"),
                Node("#Immunocompromised"),
                Node("#Specimen"),
                Node("#Swab"),
            ],
        ),
        Node(
            "#Plant infections",
            children=[
                Node("#Canker"),
                Node("#Coloration/Discoloration"),
                Node("#Deformation (Broom)"),
                Node("#Gall"),
                Node("#Lesion (incl. Necrosis)"),
                Node("#Rot (Root,Stem)"),
                Node("#Spot (Leaf,Stem)"),
                Node("#Wilt"),
            ],
        ),
    ],
)
condition = Node(
    "#Condition",
    parent=root,
    children=[
        Node("#Acidic"),
        Node("#Alkaline"),
        Node("#Anoxic (anaerobic)"),
        Node("#Humid"),
        Node("#Psychrophilic (<10°C)"),
        Node("#Saline"),
        Node("#Sulfuric"),
        Node("#Thermophilic (>45°C)"),
        Node("#Xerophilic"),
    ],
)
climate = Node(
    "#Climate",
    parent=root,
    children=[
        Node(
            "#Cold",
            children=[
                Node("#Alpine"),
                Node("#Polar"),
                Node("#Subarctic"),
                Node("#Tundra"),
            ],
        ),
        Node("#Hot", children=[Node("#Arid"), Node("#Semiarid"), Node("#Tropical")]),
        Node(
            "#Temperate",
            children=[
                Node("#Boreal"),
                Node("#Continental"),
                Node("#Subtropical"),
            ],
        ),
    ],
)
