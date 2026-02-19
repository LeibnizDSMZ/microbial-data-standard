---
hide:
  - navigation
  - toc
---

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

class `TaxonWithSource`{
name: string
taxonRank: TaxonRank | null
taxonStatus: TaxonStatus | null
identifier: array[Identifier]
scientificName: ScientificName | null
alternateName: string
parentTaxon: Taxon | null
sameAs: string
source: string
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
logo: string | null
}

class `ScientificName`{
name: string
author: string
}

class `Taxon`{
name: string
taxonRank: TaxonRank | null
taxonStatus: TaxonStatus | null
identifier: array[Identifier]
scientificName: ScientificName | null
alternateName: string
parentTaxon: Taxon | null
sameAs: string
}

class `IdentifierStrain`{
name: string
value: string
propertyID: string | null
url: string | null
logo: string | null
source: string
}

class `Origin`{
sampleDate: string | null
country: Country | null
description: string | null
locationCreated: Location | null
tags: array[IsolationTag]
sampler: Person | null
isolationDate: string | null
isolatedAt: Organization | null
isolator: Person | null
source: string
}

class `Country`{
name: string | null
iso_3166_2: string | CountryHistoricalAlpha2 | CountryOtherCodes
identifier: array[Identifier]
conventionOfBiologicalDiversityParty: boolean | null
cartagenaProtocolParty: boolean | null
nagoyaProtocolParty: boolean | null
nagoyaKualaLumpurParty: boolean | null
}

class `CountryHistoricalAlpha2`{
<<enumeration>>
CS
DD
DY
FQ
GE
HV
JT
MI
NH
RH
SU
ET
UK
VD
YU
ZR
BU
AN
}

class `CountryOtherCodes`{
<<enumeration>>
International Waters
Other
}

class `Location`{
name: string | null
description: string | null
geo: GeoPoint | null
}

class `GeoPoint`{
latitude: number | string
longitude: number | string
elevation: number | null
precision: number | null
}

class `IsolationTag`{
level1: string
level2: string | null
level3: string | null
}

class `Person`{
name: string
identifier: array[Identifier]
}

class `Organization`{
name: string
identifier: array[Identifier]
legalName: string | null
address: Address | null
url: string | null
email: string | null
logo: string | null
}

class `Address`{
addressCountry: string | null
addressCountryIso: string | null
addressRegion: string | null
addressLocality: string | null
postOfficeBoxNumber: string | null
postalCode: string | null
streetAddress: string | null
}

class `Legal`{
dualUse: boolean | null
quarantineEU: boolean | null
nagoyaRestrictions: NagoyaRestrictions
qps: boolean | null
gras: boolean | null
gmo: boolean | null
gmoInformation: string | null
otherRestrictions: array[microbial_strain_data_model__classes__legal__Restriction]
source: string
}

class `NagoyaRestrictions`{
<<enumeration>>
No known restrictions under the Nagoya protocol
Documents providing proof of legal access and terms of use available at the collection
Strain probably in scope, please contact the culture collection
}

class `microbial_strain_data_model__classes__legal__Restriction`{
name: string
country: Country | null
authority: string | null
value: string
url: string | null
}

class `Pathogen`{
host: Host
pathogen: PathogenLevel
classification: string | null
url: string | null
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

class `Morphology`{
cellShape: string | null
cellLength: Size | null
cellWidth: Size | null
motile: boolean | null
flagellum: boolean | null
flagellumArrangement: FlagellumArrangement | null
gliding: boolean | null
colonySize: Size | null
colonyColor: ColonyColor | null
multiCellComplexForming: boolean | null
source: string
}

class `Size`{
minimal: number
maximal: number
unit: SizeUnit
}

class `SizeUnit`{
<<enumeration>>
µm
mm
}

class `FlagellumArrangement`{
<<enumeration>>
Polar
Peritrichous
Monotrichous polar
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

class `CellWall`{
name: string | null
identifier: array[Identifier]
alternateName: string
percent: number | null
source: string
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

class `Spore`{
sporeBuilding: boolean | null
typeOfSpore: SporeType
sporeEjection: string | null
relatedData: string
source: string
}

class `SporeType`{
<<enumeration>>
spore
endospore
}

class `GrowthCondition`{
optimalTemperature: number | null
minimalTemperature: number | null
maximalTemperature: number | null
testsTemperature: array[GrowthRange]
optimalPh: number | null
minimalPh: number | null
maximalPh: number | null
testsPh: array[GrowthRange]
oxygenRelation: OxygenTolerance | null
source: string
}

class `GrowthRange`{
minimal: number | null
maximal: number | null
growth: boolean
relatedData: string
}

class `OxygenTolerance`{
<<enumeration>>
aerobe
aerotolerant
anaerobe
facultative aerobe
facultative anaerobe
microaerophile
microaerotolerant
obligate aerobe
obligate anaerobe
}

class `CultivationMedia`{
name: string
url: string | null
reagentUsed: string
source: string
relatedData: string
}

class `Sequence`{
type: SequenceType
level: SequenceLevel
accessionNumber: string
description: string | null
length: string | null
identifier: array[Identifier]
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
method: GCMethod | null
noteMethod: string | null
value: number
source: string
}

class `GCMethod`{
<<enumeration>>
experimental
genome sequence
}

class `FattyAcidProfile`{
profile: array[FattyAcid]
library: string | null
software: string | null
relatedData: string
source: string
}

class `FattyAcid`{
name: string | null
identifier: array[Identifier]
alternateName: string
percent: number | null
ecl: string | null
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

class `Halophil`{
name: string | null
identifier: array[Identifier]
alternateName: string
minimal: number | null
maximal: number | null
optimal: number | null
unit: ConcentrationUnit
tests: array[GrowthRange]
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

class `Tolerance`{
name: string | null
identifier: array[Identifier]
alternateName: string
reaction: ToleranceReaction | null
mic: string | null
unit: ConcentrationUnit | null
tests: array[ToleranceTest]
source: string
}

class `ToleranceReaction`{
<<enumeration>>
sensitive
resistant
intermediate
}

class `ToleranceTest`{
reaction: ToleranceReaction
concentration: number | null
unit: ConcentrationUnit
relatedData: string
}

class `Enzyme`{
name: string | null
hasECNumber: string
identifier: array[Identifier]
alternateName: string
active: boolean | null
relatedData: string
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
kindOfUtilization: KindOfUtilization | null
relatedData: string
}

class `MetaboliteTestType`{
<<enumeration>>
utilization
production
}

class `KindOfUtilization`{
<<enumeration>>
assimilation
builds acid from
degradation
energy source
fermentation
hydrolysis
reduction
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
logo: string | null
resourceNumber: string
available: boolean | null
catalogUrl: string | null
restrictionsOnUse: microbial_strain_data_model__classes__enums__Restriction | null
policyUrl: string | null
axenicCulture: boolean | null
supplyForms: array[SupplyForm]
history: string | null
depositionDate: string | null
depositor: Person | null
depositedAs: string | null
registeredCollection: boolean | null
mtaFile: string | null
absFile: string | null
source: string
}

class `microbial_strain_data_model__classes__enums__Restriction`{
<<enumeration>>
No known restrictions apply
Only for non-commercial purposes
For commercial development a special agreement is requested
}

class `SupplyForm`{
<<enumeration>>
Agar
Cryo
Dry ice
Liquid medium
Lyo
Oil
Water
DNA
}

class `Literature`{
name: string | null
url: string | null
datePublished: string | null
author: array[Person]
publisher: array[Organization]
source: string
}

class `OtherMedia`{
url: string | null
name: string | null
description: string | null
usageInfo: string | null
additionalType: string | null
source: string
}

class `RelatedData`{
relation: string
source: string
}

class `Source`{
sourceType: SourceType
mode: CurationMode
name: string | null
url: string | null
identifier: array[Identifier]
datePublished: string | null
dateRecorded: string
lastUpdate: string | null
author: array[Person]
publisher: array[Organization]
}

class `SourceType`{
<<enumeration>>
literature
website
dataset
}

class `CurationMode`{
<<enumeration>>
manual
automated
unknown
}

class `Strain`{
primaryId: string
organismType: OrganismType
morphType: Morph | null
typeStrain: array[TypeStrain]
taxon: array[TaxonWithSource]
identifier: array[IdentifierStrain]
origin: array[Origin]
legal: array[Legal]
pathogenicity: array[Pathogen]
bioSafety: array[BioSafety]
morphology: array[Morphology]
wallConstituents: array[CellWall]
staining: array[Staining]
sporeFormation: array[Spore]
growthConditions: array[GrowthCondition]
cultivationMedia: array[CultivationMedia]
sequences: array[Sequence]
gcContent: array[GCContent]
fattyAcidProfiles: array[FattyAcidProfile]
hemolysis: array[Hemolysis]
halophily: array[Halophil]
tolerances: array[Tolerance]
enzymes: array[Enzyme]
metabolites: array[Metabolite]
knownApplications: array[Application]
collections: array[Collection]
literature: array[Literature]
otherMedia: array[OtherMedia]
relatedData: array[RelatedData]
sources: array[Source]
}

`Strain` ..> `OrganismType`
`Strain` ..> `Morph`
`Strain` ..> `TypeStrain`
`Strain` ..> `TaxonWithSource`
`TaxonWithSource` ..> `TaxonRank`
`TaxonWithSource` ..> `TaxonStatus`
`TaxonWithSource` ..> `Identifier`
`TaxonWithSource` ..> `ScientificName`
`TaxonWithSource` ..> `Taxon`
`Taxon` ..> `TaxonRank`
`Taxon` ..> `TaxonStatus`
`Taxon` ..> `Identifier`
`Taxon` ..> `ScientificName`
`Taxon` ..> `Taxon`
`Strain` ..> `IdentifierStrain`
`Strain` ..> `Origin`
`Origin` ..> `Country`
`Country` ..> `CountryHistoricalAlpha2`
`Country` ..> `CountryOtherCodes`
`Country` ..> `Identifier`
`Origin` ..> `Location`
`Location` ..> `GeoPoint`
`Origin` ..> `IsolationTag`
`Origin` ..> `Person`
`Person` ..> `Identifier`
`Origin` ..> `Organization`
`Organization` ..> `Identifier`
`Organization` ..> `Address`
`Origin` ..> `Person`
`Strain` ..> `Legal`
`Legal` ..> `NagoyaRestrictions`
`Legal` ..> `microbial_strain_data_model__classes__legal__Restriction`
`microbial_strain_data_model__classes__legal__Restriction` ..> `Country`
`Strain` ..> `Pathogen`
`Pathogen` ..> `Host`
`Pathogen` ..> `PathogenLevel`
`Strain` ..> `BioSafety`
`Strain` ..> `Morphology`
`Morphology` ..> `Size`
`Size` ..> `SizeUnit`
`Morphology` ..> `Size`
`Morphology` ..> `FlagellumArrangement`
`Morphology` ..> `Size`
`Morphology` ..> `ColonyColor`
`Strain` ..> `CellWall`
`CellWall` ..> `Identifier`
`Strain` ..> `Staining`
`Staining` ..> `StainingValue`
`Strain` ..> `Spore`
`Spore` ..> `SporeType`
`Strain` ..> `GrowthCondition`
`GrowthCondition` ..> `GrowthRange`
`GrowthCondition` ..> `GrowthRange`
`GrowthCondition` ..> `OxygenTolerance`
`Strain` ..> `CultivationMedia`
`Strain` ..> `Sequence`
`Sequence` ..> `SequenceType`
`Sequence` ..> `SequenceLevel`
`Sequence` ..> `Identifier`
`Strain` ..> `GCContent`
`GCContent` ..> `GCMethod`
`Strain` ..> `FattyAcidProfile`
`FattyAcidProfile` ..> `FattyAcid`
`FattyAcid` ..> `Identifier`
`Strain` ..> `Hemolysis`
`Hemolysis` ..> `HemolysisBlood`
`Hemolysis` ..> `HemolysisType`
`Strain` ..> `Halophil`
`Halophil` ..> `Identifier`
`Halophil` ..> `ConcentrationUnit`
`Halophil` ..> `GrowthRange`
`Strain` ..> `Tolerance`
`Tolerance` ..> `Identifier`
`Tolerance` ..> `ToleranceReaction`
`Tolerance` ..> `ConcentrationUnit`
`Tolerance` ..> `ToleranceTest`
`ToleranceTest` ..> `ToleranceReaction`
`ToleranceTest` ..> `ConcentrationUnit`
`Strain` ..> `Enzyme`
`Enzyme` ..> `Identifier`
`Strain` ..> `Metabolite`
`Metabolite` ..> `Identifier`
`Metabolite` ..> `MetaboliteTest`
`MetaboliteTest` ..> `MetaboliteTestType`
`MetaboliteTest` ..> `KindOfUtilization`
`Strain` ..> `Application`
`Strain` ..> `Collection`
`Collection` ..> `Identifier`
`Collection` ..> `Address`
`Collection` ..> `microbial_strain_data_model__classes__enums__Restriction`
`Collection` ..> `SupplyForm`
`Collection` ..> `Person`
`Strain` ..> `Literature`
`Literature` ..> `Person`
`Literature` ..> `Organization`
`Strain` ..> `OtherMedia`
`Strain` ..> `RelatedData`
`Strain` ..> `Source`
`Source` ..> `SourceType`
`Source` ..> `CurationMode`
`Source` ..> `Identifier`
`Source` ..> `Person`
`Source` ..> `Organization`
```
