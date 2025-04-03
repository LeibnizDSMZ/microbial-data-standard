# Technical Concept

### 1. One File - One Strain
We want the standard to hold all necessary information on a single strain in a single file.
This way data exchange is simplified and all data that belongs together stays together.

### 2. Full traceability
Every datapoint in the a file about a strain originates from a source. Sources can be
Persons or Organizations. The new standard will link every datapoint to the source of
information.

Example:
```json
{
    "colony": [
        {
            "color": "red",
            "source": [
                "/sources/0",
                "/sources/2"
            ]
        },
        {
            "color": "green",
            "source": [
                "/sources/1"
            ]
        }
    ],
    "sources": [
        {
            "firstName": "Peter",
            "lastName":"Parker"
        },
        {
            "firstName": "Bruce",
            "lastName": "Banner"
        },
        {
            "firstName": "Tony",
            "lastName": "Stark"
        }
    ]
}
```

The example above shows two data points in "colony".
There are two sources that say the colony is of color "red"
and one source that states the color of the colony is "green".
The source pointers in each datapoint indicate which source in the
"sources" list is responsible for the datapoint.


By tracking the source of information for each datapoint, we want to achieve that
every data provider gets credit for their provided data. Furthermore by comparing the data
from different sources with each other data quality will improve drastically.
Incorrect data can easier be spotted and corrected or mutations in strains
can be found.

### 3. Aligning with schema.org and bioschemas
This new data standard tries to improve the interoperability with other use cases
and systems by implementing fields and structures like they are found in
[schema.org](https://schema.org) and
[bioschemas](https://bioschemas.org/).
Data fields that are not defined in those schemas are added to the standard wherever
needed, but with similar structure to schemas.
