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
