``` mermaid
classDiagram
direction LR
class `OrganismType`{
<<enumeration>>
Algae
Archaea
Bacteria
Fungi
Protist
}

class `Morph`{
<<enumeration>>
yeast
filamentous
}

class `TypeStrain`{
typeStrain: boolean
source: string
}

class `Taxon`{
name: string
taxonRank: TaxonRank
taxonStatus: TaxonStatus
identifier: array[Identifier]
scientificName: ScientificName | null
alternateName: string
parentTaxon: Taxon | null
sameAs: string
}

class `TaxonRank`{
<<enumeration>>
subspecies
species
section
genus
family
order
class
phylum
domain
}

class `TaxonStatus`{
<<enumeration>>
proposed
validly published
validly published synonym
}

class `Identifier`{
name: string
value: string
propertyID: string | null
url: string | null
}

class `ScientificName`{
name: string
author: string
}

class `TaxonWithSource`{
name: string
taxonRank: TaxonRank
taxonStatus: TaxonStatus
identifier: array[Identifier]
scientificName: ScientificName | null
alternateName: string
parentTaxon: TaxonWithSource | null
sameAs: string
source: string
}

class `Sample`{
date: string | null
country: Country | null
description: string | null
locationCreated: Location | null
tags: array[IsolationTag]
source: string
}

class `Country`{
name: string | CountryHistoricalAlpha2 | CountryOtherCodes
identifier: array[Identifier]
conventionOfBiologicalDiversityParty: boolean | null
cartagenaProtocolParty: boolean | null
nagoyaProtocolParty: boolean | null
nagoyaKualaLumpurParty: boolean | null
}

class `CountryHistoricalAlpha2`{
<<enumeration>>
Czechoslovakia
German Democratic Republic (East Germany)
Dahomey
French Southern and Antarctic Territories
Gilbert and Ellice Islands
Upper Volta
Johnston Island
Midway Islands
New Hebrides
Southern Rhodesia
Soviet Union
East Timor
United Kingdom
North Vietnam
Yugoslavia
Zaire
Burma
Netherlands Antilles
}

class `CountryOtherCodes`{
<<enumeration>>
International Region
Other
}

class `Location`{
name: string | null
description: string | null
geo: GeoPoint | null
}

class `GeoPoint`{
latitude: number
longitude: number
elevation: number | null
precision: number | null
}

class `IsolationTag`{
level1: string
level2: string | null
level3: string | null
}

class `Isolation`{
date: string | null
isolatedAt: Organization | Person | null
source: string
}

class `Organization`{
name: string
identifier: array[Identifier]
legalName: string | null
address: Address | null
url: string | null
email: string | null
}

class `Address`{
addressCountry: string | null
addressLocality: string | null
addressRegion: string | null
postOfficeBoxNumber: string | null
postalCode: string | null
streetAddress: string | null
}

class `Person`{
name: string
identifier: array[Identifier]
}

class `Legal`{
dualUse: boolean | null
quarantineEU: boolean | null
nagoyaRestrictions: NagoyaRestrictions
qps: boolean | null
gras: boolean | null
gmo: boolean | null
gmoInformation: string | null
source: string
}

class `NagoyaRestrictions`{
<<enumeration>>
No known restrictions under the Nagoya protocol
Documents providing proof of legal access and terms of use available at the collection
Strain probably in scope, please contact the culture collection
}

class `CellShape`{
cellShape: string
source: string
}

class `OxygenRelation`{
oxygenRelation: string
source: string
}

class `MultiCell`{
multiCellComplexForming: boolean
source: string
}

class `Size`{
minimal: number
maximal: number
unit: SizeUnit
source: string
}

class `SizeUnit`{
<<enumeration>>
µm
mm
}

class `Motility`{
motile: boolean | null
flagellum: boolean | null
flagellumArrangement: FlagellumArrangement | null
gliding: boolean | null
source: string
}

class `FlagellumArrangement`{
<<enumeration>>
Polar
Peritrichous
Monotrichous polar
}

class `Colony`{
size: number | null
color: ColonyColor | null
source: string
}

class `ColonyColor`{
<<enumeration>>
white
cream
yellowish
orange
pink
red
buff
darkbrown
reyish
tannish
beige
brownish
}

class `Spore`{
sporeBuilding: boolean | null
typeOfSpore: SporeType
sporeEjection: string | null
source: string
}

class `SporeType`{
<<enumeration>>
spore
endospore
}

class `Growth[C]`{
optimal: number | null
minimal: number | null
maximal: number | null
unit: string
tested: array[GrowthRange[C]]
source: string
}

class `GrowthRange[C]`{
minimal: number | null
maximal: number | null
unit: string
growth: boolean
}

class `Growth[pH]`{
optimal: number | null
minimal: number | null
maximal: number | null
unit: string
tested: array[GrowthRange[pH]]
source: string
}

class `GrowthRange[pH]`{
minimal: number | null
maximal: number | null
unit: string
growth: boolean
}

class `IdentifierStrain`{
name: string
value: string
propertyID: string | null
url: string | null
source: string
}

class `ConnectedPerson`{
name: string
identifier: array[Identifier]
role: PersonRole | null
source: string
}

class `PersonRole`{
<<enumeration>>
sampler
isolator
other
}

class `Pathogen`{
host: Host
pathogen: PathogenLevel
classification: string | null
source: string
}

class `Host`{
<<enumeration>>
plant
animal
invertebrates
vertebrates
mammals
non-human primates
human
fungi
}

class `PathogenLevel`{
<<enumeration>>
no pathogen
opportunistic
obligate
}

class `BioSafety`{
riskgroup: string
classification: string | null
url: string | null
source: string
}

class `Sequence`{
type: SequenceType
level: SequenceLevel
accessionNumber: string
description: string | null
length: string | null
url: string
source: string
}

class `SequenceType`{
<<enumeration>>
nucleotide
protein
}

class `SequenceLevel`{
<<enumeration>>
genome
identifier sequence
gene
artificial
other
}

class `GCContent`{
method: string | null
value: number
source: string
}

class `Literature`{
name: string | null
url: string | null
datePublished: string | null
author: array[Person]
publisher: array[Organization]
source: string
}

class `CellWall`{
name: string | null
identifier: array[Identifier]
alternateName: string
percent: number | null
source: string
}

class `FattyAcidProfile`{
profile: array[FattyAcid]
temperature: integer | null
medium: string | null
library: string | null
software: string | null
source: string
}

class `FattyAcid`{
name: string | null
identifier: array[Identifier]
alternateName: string
percent: number | null
ecl: string | null
}

class `Staining`{
name: string
value: StainingValue
source: string
}

class `StainingValue`{
<<enumeration>>
positive
negative
variable
}

class `Hemolysis`{
blood: HemolysisBlood
hemolysisType: HemolysisType
source: string
}

class `HemolysisBlood`{
<<enumeration>>
sheep
horse
unknown
}

class `HemolysisType`{
<<enumeration>>
alpha
beta
gamma
}

class `CultivationMedia`{
name: string | null
url: string | null
reagentUsed: string
source: string
}

class `Halophil`{
name: string | null
identifier: array[Identifier]
alternateName: string
optimal: number | null
minimal: number | null
maximal: number | null
unit: ConcentrationUnit
tested: array[GrowthRange_ConcentrationUnit_]
source: string
}

class `ConcentrationUnit`{
<<enumeration>>
g/L
mol/L
g/g%
v/v%
unknown
}

class `GrowthRange_ConcentrationUnit_`{
minimal: number | null
maximal: number | null
unit: ConcentrationUnit
growth: boolean
}

class `Tolerance`{
name: string | null
identifier: array[Identifier]
alternateName: string
reaction: string | null
mic: string | null
unit: ConcentrationUnit | null
tests: array[ToleranceTest]
source: string
}

class `ToleranceTest`{
reaction: ToleranceReaction
concentration: string | null
unit: ConcentrationUnit
}

class `ToleranceReaction`{
<<enumeration>>
sensitive
resistant
intermediate
}

class `Enzyme`{
name: string | null
hasECNumber: string
url: string | null
alternateName: string
active: boolean | null
source: string
}

class `Metabolite`{
name: string | null
identifier: array[Identifier]
alternateName: string
tests: array[MetaboliteTest]
source: string
}

class `MetaboliteTest`{
type: MetaboliteTestType
active: boolean | null
protocol: string | null
kindOfUtilization: string | null
}

class `MetaboliteTestType`{
<<enumeration>>
utilization
production
}

class `Application`{
application: string
source: string
}

class `Collection`{
name: string
identifier: array[Identifier]
legalName: string | null
address: Address | null
url: string | null
email: string | null
resourceNumber: string
availability: boolean | null
catalogUrl: string | null
restrictionsOnUse: Restriction | null
axenicCulture: boolean | null
supplyForms: array | null
history: string | null
depositionDate: string | null
depositor: Person | null
source: string
}

class `Restriction`{
<<enumeration>>
No known restrictions apply
Only for non-commercial purposes
For commercial development a special agreement is requested
}

class `OtherMedia`{
url: string | null
name: string | null
description: string | null
usageInfo: string | null
additionalType: string | null
source: string
}

class `Microbe`{
organismType: OrganismType
morphType: Morph | null
unifiedTypeStrain: boolean
typeStrain: array[TypeStrain]
unifiedTaxon: Taxon
taxon: array[TaxonWithSource]
sample: array[Sample]
isolation: array[Isolation]
legal: array[Legal]
cellShape: array[CellShape]
oxygenRelation: array[OxygenRelation]
multiCellComplexForming: array[MultiCell]
cellLength: array[Size]
cellWidth: array[Size]
motility: array[Motility]
colony: array[Colony]
sporeFormation: array[Spore]
temperature: array[Growth[C]]
pH: array[Growth[pH]]
identifier: array[IdentifierStrain]
connectedPersons: array[ConnectedPerson]
pathogenicity: array[Pathogen]
bioSafety: array[BioSafety]
sequences: array[Sequence]
gcContent: array[GCContent]
literature: array[Literature]
wallConstituents: array[CellWall]
fattyAcidProfiles: array[FattyAcidProfile]
stainings: array[Staining]
hemolysis: array[Hemolysis]
cultivationMedia: array[CultivationMedia]
halophily: array[Halophil]
tolerances: array[Tolerance]
enzymes: array[Enzyme]
metabolites: array[Metabolite]
knownApplications: array[Application]
collections: array[Collection]
otherMedia: array[OtherMedia]
sources:
}

`Microbe` ..> `OrganismType`
`Microbe` ..> `Morph`
`Microbe` ..> `TypeStrain`
`Microbe` ..> `Taxon`
`Taxon` ..> `TaxonRank`
`Taxon` ..> `TaxonStatus`
`Taxon` ..> `Identifier`
`Taxon` ..> `ScientificName`
`Taxon` ..> `Taxon`
`Microbe` ..> `TaxonWithSource`
`TaxonWithSource` ..> `TaxonRank`
`TaxonWithSource` ..> `TaxonStatus`
`TaxonWithSource` ..> `Identifier`
`TaxonWithSource` ..> `ScientificName`
`TaxonWithSource` ..> `TaxonWithSource`
`Microbe` ..> `Sample`
`Sample` ..> `Country`
`Country` ..> `CountryHistoricalAlpha2`
`Country` ..> `CountryOtherCodes`
`Country` ..> `Identifier`
`Sample` ..> `Location`
`Location` ..> `GeoPoint`
`Sample` ..> `IsolationTag`
`Microbe` ..> `Isolation`
`Isolation` ..> `Organization`
`Organization` ..> `Identifier`
`Organization` ..> `Address`
`Isolation` ..> `Person`
`Person` ..> `Identifier`
`Microbe` ..> `Legal`
`Legal` ..> `NagoyaRestrictions`
`Microbe` ..> `CellShape`
`Microbe` ..> `OxygenRelation`
`Microbe` ..> `MultiCell`
`Microbe` ..> `Size`
`Size` ..> `SizeUnit`
`Microbe` ..> `Size`
`Microbe` ..> `Motility`
`Motility` ..> `FlagellumArrangement`
`Microbe` ..> `Colony`
`Colony` ..> `ColonyColor`
`Microbe` ..> `Spore`
`Spore` ..> `SporeType`
`Microbe` ..> `Growth[C]`
`Growth[C]` ..> `GrowthRange[C]`
`Microbe` ..> `Growth[pH]`
`Growth[pH]` ..> `GrowthRange[pH]`
`Microbe` ..> `IdentifierStrain`
`Microbe` ..> `ConnectedPerson`
`ConnectedPerson` ..> `Identifier`
`ConnectedPerson` ..> `PersonRole`
`Microbe` ..> `Pathogen`
`Pathogen` ..> `Host`
`Pathogen` ..> `PathogenLevel`
`Microbe` ..> `BioSafety`
`Microbe` ..> `Sequence`
`Sequence` ..> `SequenceType`
`Sequence` ..> `SequenceLevel`
`Microbe` ..> `GCContent`
`Microbe` ..> `Literature`
`Literature` ..> `Person`
`Literature` ..> `Organization`
`Microbe` ..> `CellWall`
`CellWall` ..> `Identifier`
`Microbe` ..> `FattyAcidProfile`
`FattyAcidProfile` ..> `FattyAcid`
`FattyAcid` ..> `Identifier`
`Microbe` ..> `Staining`
`Staining` ..> `StainingValue`
`Microbe` ..> `Hemolysis`
`Hemolysis` ..> `HemolysisBlood`
`Hemolysis` ..> `HemolysisType`
`Microbe` ..> `CultivationMedia`
`Microbe` ..> `Halophil`
`Halophil` ..> `Identifier`
`Halophil` ..> `ConcentrationUnit`
`Halophil` ..> `GrowthRange_ConcentrationUnit_`
`GrowthRange_ConcentrationUnit_` ..> `ConcentrationUnit`
`Microbe` ..> `Tolerance`
`Tolerance` ..> `Identifier`
`Tolerance` ..> `ConcentrationUnit`
`Tolerance` ..> `ToleranceTest`
`ToleranceTest` ..> `ToleranceReaction`
`ToleranceTest` ..> `ConcentrationUnit`
`Microbe` ..> `Enzyme`
`Microbe` ..> `Metabolite`
`Metabolite` ..> `Identifier`
`Metabolite` ..> `MetaboliteTest`
`MetaboliteTest` ..> `MetaboliteTestType`
`Microbe` ..> `Application`
`Microbe` ..> `Collection`
`Collection` ..> `Identifier`
`Collection` ..> `Address`
`Collection` ..> `Restriction`
`Collection` ..> `Person`
`Microbe` ..> `OtherMedia`
```
