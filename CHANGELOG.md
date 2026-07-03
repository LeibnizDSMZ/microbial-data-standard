<!--
SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH

SPDX-License-Identifier: CC0-1.0
-->

## v0.12.3 (2026-07-03)

### Fix

- update image paths from stylesheets to images directory
- **licenses**: consolidate spdx headers using reuse.toml and update lint script

## v0.12.2 (2026-07-03)

### Fix

- restructure docs into dedicated pnpm package and update ci workflows

## v0.12.1 (2026-07-01)

### Fix

- **deps**: add griffe_pydantic to docs dependencies

## v0.12.0 (2026-07-01)

### Feat

- **strain**: add version field to strain model and update tests
- **strain**: add version field to strain model
- **strain**: add split functionality to partition strain data by source
- add licenses script

### Fix

- **classes**: correct inverted validation logic in data models

### Refactor

- **builder**: remove git add functionality from documentation scripts
- **schema**: alphabetize properties and sort json output in doc builder
- **address**: replace countryalpha2 type with str in index tuple
- **merge**: update strain join logic to handle bidirectional link mappings
- **schema**: update strain model properties and add deepdiff dependency
- **schema**: alphabetize schema properties and adjust doc generator separator

## v0.11.0 (2026-05-05)

### Feat

- change spore object requirements

### Fix

- correct sporeForming field

### Refactor

- rename sporeBuilding to sporeForming

## v0.10.0 (2026-04-23)

### Feat

- changed taxon and typestrain to not required and add min len for identifer = 1

### Fix

- **country**: fixed check for country name or iso

## v0.9.2 (2026-04-14)

### Fix

- **isolationtags**: fixed seperator problem in isolation tags

## v0.9.1 (2026-02-20)

### Fix

- move sample isolation to notes
- fixed historical iso codes to be 2 letter codes + updates (#26)
- **morph**: made cell data in morphology optional

### Refactor

- bump version

## v0.9.0 (2026-01-29)

### Feat

- **update**: new field primaryId and country data changes

## v0.8.0 (2025-08-29)

### Feat

- add OxygenRelation Enum
- add GCMethod enum
- add lastUpdate to source and logo to identifier
- add KindOfUtilization enum

### Fix

- change concentration of tolerance test to float value, was string
- changed enzyme url to identifier list

### Refactor

- **restructure**: restructure
- **restructure**: restructure data multicallcomplex and oxygenrelation into other classes
- **restructure**: restructure information of origin, morphology and growthcondtion into new classes

## v0.7.0 (2025-08-14)

### Feat

- **source**: new source class

### Fix

- fix typo in Source, make taxonRank and taxonStatus no longer required

## v0.6.0 (2025-07-31)

### Feat

- **source**: new source class
- add relatedData to fattyAcidProfile, Spore and Multicell
- add relationData to Enzyme and OxygenRelation
- add relatedData to CultivationMedia
- add relatedData to metabolitetest and tolerancetest
- add relatedData field to growthrange
- add new data structure "relatedData"
- add link to ABS files to collection
- new fields in Organization + small restructure
- URL field for pathogenicity documents
- new fields and descriptions

### Fix

- pattern of RelationLink and test data bacteria

### Refactor

- rename growrange to growthrange
- rename file sourcestring.py to links.py
- rename sourceString to SourceLink

## v0.5.0 (2025-06-24)

### Feat

- add relatedData to fattyAcidProfile, Spore and Multicell
- add relationData to Enzyme and OxygenRelation
- add relatedData to CultivationMedia
- add relatedData to metabolitetest and tolerancetest
- add relatedData field to growthrange
- add new data structure "relatedData"
- add link to ABS files to collection
- new fields in Organization + small restructure
- URL field for pathogenicity documents
- new fields and descriptions

### Fix

- pattern of RelationLink and test data bacteria

### Refactor

- rename growrange to growthrange
- rename file sourcestring.py to links.py
- rename sourceString to SourceLink

## v0.4.0 (2025-05-19)

### Feat

- add policyURL to Collection class
- replace url with identifier in sequence, fixed test data, fixed make buildSchema
- rename stainings to staining

### Fix

- fix lfs
- add docstring to "sequenceLevel" enum class
- **field-changes**: add new class restrictions and some field changes

### Refactor

- improve checks

## v0.3.0 (2025-02-17)

### Feat

- source now list of sourcestrings

### Fix

- solve "None" fields are not required

### Refactor

- remove aliases and rename variables for more consistency
- improve checks

## v0.2.1 (2025-02-05)

### Fix

- fix parent field in TaxonWithSource by overwriting

## v0.2.0 (2025-02-04)

### Feat

- source now list of sourcestrings

### Fix

- solve "None" fields are not required

## v0.1.1 (2025-01-15)

### Fix

- set model config for every class

## v0.1.0 (2025-01-13)

### Feat

- **update**: update data standard with new arrays, description and documentation

### Fix

- **required-fields**: switched required field unified_taxon/typeStrain with taxon and typeStrain
- **size**: move cell length and cell width in cellsize, fixed culture size and size class
- **id/lastUpdate**: delete id and last update from microbe
- remove mariadb dependency

### Refactor

- reset first release version to 0.0.0
- update dependencies
