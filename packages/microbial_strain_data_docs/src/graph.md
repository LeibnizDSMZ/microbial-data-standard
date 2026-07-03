---
# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: CC0-1.0

hide:
  - navigation
  - toc
search:
  exclude: true
---

``` mermaid
classDiagram
direction LR
class `BioSafety`{
classification: string | null
riskgroup: string
source: string
url: string | null
}

class `Collection`{
absFile: string | null
address: Address | null
available: boolean | null
axenicCulture: boolean | null
catalogUrl: string | null
depositedAs: string | null
depositionDate: string | null
depositor: Person | null
email: string | null
history: string | null
identifier: array[Identifier]
legalName: string | null
logo: string | null
mtaFile: string | null
name: string
policyUrl: string | null
registeredCollection: boolean | null
resourceNumber: string
restrictionsOnUse: microbial_strain_data_model__classes__enums__Restriction | null
source: string
supplyForms: array[SupplyForm]
url: string | null
}

class `Address`{
addressCountry: string | null
addressCountryIso: string | null
addressLocality: string | null
addressRegion: string | null
postOfficeBoxNumber: string | null
postalCode: string | null
streetAddress: string | null
}

class `Person`{
identifier: array[Identifier]
name: string
}

class `Identifier`{
logo: string | null
name: string
propertyID: string | null
url: string | null
value: string
}

class `microbial_strain_data_model__classes__enums__Restriction`{
<<enumeration>>
no known restrictions apply
only for non-commercial purposes
for commercial development a special agreement is requested
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

class `CultivationMedia`{
name: string
reagentUsed: string
relatedData: string
source: string
url: string | null
}

class `Enzyme`{
active: boolean | null
alternateName: string
hasECNumber: string
identifier: array[Identifier]
name: string | null
relatedData: string
source: string
}

class `FattyAcidProfile`{
library: string | null
profile: array[FattyAcid]
relatedData: string
software: string | null
source: string
}

class `FattyAcid`{
alternateName: string
ecl: string | null
identifier: array[Identifier]
name: string | null
percent: number | null
}

class `GCContent`{
method: GCMethod | null
noteMethod: string | null
source: string
value: number
}

class `GCMethod`{
<<enumeration>>
experimental
genome sequence
}

class `GrowthCondition`{
maximalPh: number | null
maximalTemperature: number | null
minimalPh: number | null
minimalTemperature: number | null
optimalPh: number | null
optimalTemperature: number | null
oxygenRelation: OxygenTolerance | null
source: string
testsPh: array[GrowthRange]
testsTemperature: array[GrowthRange]
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

class `GrowthRange`{
growth: boolean
maximal: number | null
minimal: number | null
relatedData: string
}

class `Halophil`{
alternateName: string
identifier: array[Identifier]
maximal: number | null
minimal: number | null
name: string | null
optimal: number | null
source: string
tests: array[GrowthRange]
unit: ConcentrationUnit
}

class `ConcentrationUnit`{
<<enumeration>>
g/L
mol/L
g/g%
v/v%
unknown
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

class `IdentifierStrain`{
logo: string | null
name: string
propertyID: string | null
source: string
url: string | null
value: string
}

class `Application`{
application: string
source: string
}

class `Legal`{
dualUse: boolean | null
gmo: boolean | null
gmoInformation: string | null
gras: boolean | null
nagoyaRestrictions: NagoyaRestrictions
otherRestrictions: array[microbial_strain_data_model__classes__legal__Restriction]
qps: boolean | null
quarantineEU: boolean | null
source: string
}

class `NagoyaRestrictions`{
<<enumeration>>
No known restrictions under the Nagoya protocol
Documents providing proof of legal access and terms of use available at the collection
Strain probably in scope, please contact the culture collection
}

class `microbial_strain_data_model__classes__legal__Restriction`{
authority: string | null
country: Country | null
name: string
url: string | null
value: string
}

class `Country`{
cartagenaProtocolParty: boolean | null
conventionOfBiologicalDiversityParty: boolean | null
identifier: array[Identifier]
iso_3166_2: string | CountryHistoricalAlpha2 | CountryOtherCodes | null
nagoyaKualaLumpurParty: boolean | null
nagoyaProtocolParty: boolean | null
name: string | null
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

class `Literature`{
author: array[Person]
datePublished: string | null
name: string | null
publisher: array[Organization]
source: string
url: string | null
}

class `Organization`{
address: Address | null
email: string | null
identifier: array[Identifier]
legalName: string | null
logo: string | null
name: string
url: string | null
}

class `Metabolite`{
alternateName: string
identifier: array[Identifier]
name: string | null
source: string
tests: array[MetaboliteTest]
}

class `MetaboliteTest`{
active: boolean | null
kindOfUtilization: KindOfUtilization | null
protocol: string | null
relatedData: string
type: MetaboliteTestType
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

class `MetaboliteTestType`{
<<enumeration>>
utilization
production
}

class `Morph`{
<<enumeration>>
yeast
filamentous
}

class `Morphology`{
cellLength: Size | null
cellShape: string | null
cellWidth: Size | null
colonyColor: ColonyColor | null
colonySize: Size | null
flagellum: boolean | null
flagellumArrangement: FlagellumArrangement | null
gliding: boolean | null
motile: boolean | null
multiCellComplexForming: boolean | null
source: string
}

class `Size`{
maximal: number
minimal: number
unit: SizeUnit
}

class `SizeUnit`{
<<enumeration>>
µm
mm
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

class `FlagellumArrangement`{
<<enumeration>>
Polar
Peritrichous
Monotrichous polar
}

class `OrganismType`{
<<enumeration>>
Algae
Archaea
Bacteria
Fungi
Protist
}

class `Origin`{
country: Country | null
description: string | null
isolatedAt: Organization | null
isolationDate: string | null
isolator: Person | null
locationCreated: Location | null
sampleDate: string | null
sampler: Person | null
source: string
tags: array[IsolationTag]
}

class `Location`{
description: string | null
geo: GeoPoint | null
name: string | null
}

class `GeoPoint`{
elevation: number | null
latitude: number | string
longitude: number | string
precision: number | null
}

class `IsolationTag`{
level1: string
level2: string | null
level3: string | null
}

class `OtherMedia`{
additionalType: string | null
description: string | null
name: string | null
source: string
url: string | null
usageInfo: string | null
}

class `Pathogen`{
classification: string | null
host: Host
pathogen: PathogenLevel
source: string
url: string | null
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

class `RelatedData`{
relation: string
source: string
}

class `Sequence`{
accessionNumber: string
description: string | null
identifier: array[Identifier]
length: string | null
level: SequenceLevel
source: string
type: SequenceType
}

class `SequenceLevel`{
<<enumeration>>
genome
identifier sequence
gene
artificial
other
}

class `SequenceType`{
<<enumeration>>
nucleotide
protein
}

class `Source`{
author: array[Person]
datePublished: string | null
dateRecorded: string
identifier: array[Identifier]
lastUpdate: string | null
mode: CurationMode
name: string | null
publisher: array[Organization]
sourceType: SourceType
url: string | null
}

class `CurationMode`{
<<enumeration>>
manual
automated
unknown
}

class `SourceType`{
<<enumeration>>
literature
website
dataset
}

class `Spore`{
relatedData: string
source: string
sporeEjection: string | null
sporeForming: boolean
typeOfSpore: SporeType | null
}

class `SporeType`{
<<enumeration>>
spore
endospore
}

class `Staining`{
name: string
source: string
value: StainingValue
}

class `StainingValue`{
<<enumeration>>
positive
negative
variable
}

class `TaxonWithSource`{
alternateName: string
identifier: array[Identifier]
name: string
parentTaxon: Taxon | null
sameAs: string
scientificName: ScientificName | null
source: string
taxonRank: TaxonRank | null
taxonStatus: TaxonStatus | null
}

class `Taxon`{
alternateName: string
identifier: array[Identifier]
name: string
parentTaxon: Taxon | null
sameAs: string
scientificName: ScientificName | null
taxonRank: TaxonRank | null
taxonStatus: TaxonStatus | null
}

class `ScientificName`{
author: string
name: string
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

class `Tolerance`{
alternateName: string
identifier: array[Identifier]
mic: string | null
name: string | null
reaction: ToleranceReaction | null
source: string
tests: array[ToleranceTest]
unit: ConcentrationUnit | null
}

class `ToleranceReaction`{
<<enumeration>>
sensitive
resistant
intermediate
}

class `ToleranceTest`{
concentration: number | null
reaction: ToleranceReaction
relatedData: string
unit: ConcentrationUnit
}

class `TypeStrain`{
source: string
typeStrain: boolean
}

class `CellWall`{
alternateName: string
identifier: array[Identifier]
name: string | null
percent: number | null
source: string
}

class `Strain`{
bioSafety: array[BioSafety]
collections: array[Collection]
cultivationMedia: array[CultivationMedia]
enzymes: array[Enzyme]
fattyAcidProfiles: array[FattyAcidProfile]
gcContent: array[GCContent]
growthConditions: array[GrowthCondition]
halophily: array[Halophil]
hemolysis: array[Hemolysis]
identifier: array[IdentifierStrain]
knownApplications: array[Application]
legal: array[Legal]
literature: array[Literature]
metabolites: array[Metabolite]
morphType: Morph | null
morphology: array[Morphology]
organismType: OrganismType
origin: array[Origin]
otherMedia: array[OtherMedia]
pathogenicity: array[Pathogen]
primaryId: string
relatedData: array[RelatedData]
sequences: array[Sequence]
sources: array[Source]
sporeFormation: array[Spore]
staining: array[Staining]
taxon: array[TaxonWithSource]
tolerances: array[Tolerance]
typeStrain: array[TypeStrain]
version: integer
wallConstituents: array[CellWall]
}

`Strain` ..> `BioSafety`
`Strain` ..> `Collection`
`Collection` ..> `Address`
`Collection` ..> `Person`
`Person` ..> `Identifier`
`Collection` ..> `Identifier`
`Collection` ..> `microbial_strain_data_model__classes__enums__Restriction`
`Collection` ..> `SupplyForm`
`Strain` ..> `CultivationMedia`
`Strain` ..> `Enzyme`
`Enzyme` ..> `Identifier`
`Strain` ..> `FattyAcidProfile`
`FattyAcidProfile` ..> `FattyAcid`
`FattyAcid` ..> `Identifier`
`Strain` ..> `GCContent`
`GCContent` ..> `GCMethod`
`Strain` ..> `GrowthCondition`
`GrowthCondition` ..> `OxygenTolerance`
`GrowthCondition` ..> `GrowthRange`
`GrowthCondition` ..> `GrowthRange`
`Strain` ..> `Halophil`
`Halophil` ..> `Identifier`
`Halophil` ..> `GrowthRange`
`Halophil` ..> `ConcentrationUnit`
`Strain` ..> `Hemolysis`
`Hemolysis` ..> `HemolysisBlood`
`Hemolysis` ..> `HemolysisType`
`Strain` ..> `IdentifierStrain`
`Strain` ..> `Application`
`Strain` ..> `Legal`
`Legal` ..> `NagoyaRestrictions`
`Legal` ..> `microbial_strain_data_model__classes__legal__Restriction`
`microbial_strain_data_model__classes__legal__Restriction` ..> `Country`
`Country` ..> `Identifier`
`Country` ..> `CountryHistoricalAlpha2`
`Country` ..> `CountryOtherCodes`
`Strain` ..> `Literature`
`Literature` ..> `Person`
`Literature` ..> `Organization`
`Organization` ..> `Address`
`Organization` ..> `Identifier`
`Strain` ..> `Metabolite`
`Metabolite` ..> `Identifier`
`Metabolite` ..> `MetaboliteTest`
`MetaboliteTest` ..> `KindOfUtilization`
`MetaboliteTest` ..> `MetaboliteTestType`
`Strain` ..> `Morph`
`Strain` ..> `Morphology`
`Morphology` ..> `Size`
`Size` ..> `SizeUnit`
`Morphology` ..> `Size`
`Morphology` ..> `ColonyColor`
`Morphology` ..> `Size`
`Morphology` ..> `FlagellumArrangement`
`Strain` ..> `OrganismType`
`Strain` ..> `Origin`
`Origin` ..> `Country`
`Origin` ..> `Organization`
`Origin` ..> `Person`
`Origin` ..> `Location`
`Location` ..> `GeoPoint`
`Origin` ..> `Person`
`Origin` ..> `IsolationTag`
`Strain` ..> `OtherMedia`
`Strain` ..> `Pathogen`
`Pathogen` ..> `Host`
`Pathogen` ..> `PathogenLevel`
`Strain` ..> `RelatedData`
`Strain` ..> `Sequence`
`Sequence` ..> `Identifier`
`Sequence` ..> `SequenceLevel`
`Sequence` ..> `SequenceType`
`Strain` ..> `Source`
`Source` ..> `Person`
`Source` ..> `Identifier`
`Source` ..> `CurationMode`
`Source` ..> `Organization`
`Source` ..> `SourceType`
`Strain` ..> `Spore`
`Spore` ..> `SporeType`
`Strain` ..> `Staining`
`Staining` ..> `StainingValue`
`Strain` ..> `TaxonWithSource`
`TaxonWithSource` ..> `Identifier`
`TaxonWithSource` ..> `Taxon`
`Taxon` ..> `Identifier`
`Taxon` ..> `Taxon`
`Taxon` ..> `ScientificName`
`Taxon` ..> `TaxonRank`
`Taxon` ..> `TaxonStatus`
`TaxonWithSource` ..> `ScientificName`
`TaxonWithSource` ..> `TaxonRank`
`TaxonWithSource` ..> `TaxonStatus`
`Strain` ..> `Tolerance`
`Tolerance` ..> `Identifier`
`Tolerance` ..> `ToleranceReaction`
`Tolerance` ..> `ToleranceTest`
`ToleranceTest` ..> `ToleranceReaction`
`ToleranceTest` ..> `ConcentrationUnit`
`Tolerance` ..> `ConcentrationUnit`
`Strain` ..> `TypeStrain`
`Strain` ..> `CellWall`
`CellWall` ..> `Identifier`
```
