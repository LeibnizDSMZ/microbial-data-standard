# Technical Concept

### 1. One Strain - One File
We want the standard to hold all necessary information on a single strain in a single file.
In this way data exchange is simplified and all data that belongs together stays together.

### 2. Full traceability
Every datapoint in a file originates from a source. Sources can be
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
There are two sources that state the colony is of color "red"
and one source that states the color of the colony is "green".
The source pointers in each datapoint indicate which source in the
"sources" list is responsible for the datapoint.


By tracking the source of information for each datapoint, full transparency is achieved and
every data provider gets credit for their provided data. Furthermore by comparing the data
from different sources, quality will improve drastically.
Incorrect data can easily be spotted and corrected or mutations in strains
can be found and the respective dataset can be demerged.

### 3. Aligning with schema.org and bioschemas
This new data standard tries to improve the interoperability with other use cases
and systems by implementing fields and structures similar to
[schema.org](https://schema.org) and
[bioschemas](https://bioschemas.org/).

### 4. Related data points
Other microbial data standards have no possibility to define conditions which are e.g. related to a test result.

For example:
A strain that grows on Medium Y, which has a pH of 7, at 25°C, in a aerobic environment needs time X to double.
This results in the most data standards in 5 different singular results like: grows on Y, grows at pH 7 and so on.
But if we change the conditions the strain may grows faster or slower at a different temperature or pH or medium. Maybe the strain produces different compounds in a different aerobic environment.

As this data is very specific and small changes can have massive impacts at results this
data standard aim to solve the issue by providing a way to capture the conditions under which a test was performed.
The solution is **related data points**.


Join now! See [Call To Action](call.md) for further details.
