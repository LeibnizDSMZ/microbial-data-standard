# Technical Concept

## 1. One Strain - One File
As this new data standard is primarily intended for data exchange, the concept of
‘One Strain, One File’ is being pursued.
The focus here is on recording all relevant data of a microbial strain at once.
This form of a data exchange format is intended to provide a low-friction solution for
highly complex data, as all relevant information that belongs together always stays together.

## 2. Full traceability
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

## 3. Aligning with schema.org and bioschemas
This new data standard tries to improve the interoperability with other use cases
and systems by implementing fields and structures similar to
[schema.org](https://schema.org) and
[bioschemas](https://bioschemas.org/).

## 4. Related data points
Other microbial data standards have no solution to define that data points are
related to each other.

This data standard offers a solution to this, by providing the option to define *relatedData*
objects which can describe the type of relation. Other data objects, which have a *relatedData*
list can point at those *relatedData* objects to define that they belong to this relation.


When a test is performed on a strain, the environment conditions are fully controlled in
most cases, as a change in the conditions can change the result of the test.
The relation between the environment conditions and the test can be captured
with the *relatedData* links and object.
![image](stylesheets/growth_condition.png)
In the example above all data points that are related to the growth condition are linked to the
*relatedDate* object **Growth Condition**. Even the test result, which was measured under
the given condition, points to this *relatedData* object.

But a connection can be used in many different ways.
For example if a test series like an API test is performed on a strain,
the results of each single test in the series will be put into the
according category of this data standard. But to capture the information that a result
is from this API test series, all the results will link via *relatedData* to the relation
object.

![image](stylesheets/API_results.png)

As one data point can link to multiple *relatedData* objects, even complex combinations of
relations can be captured.

Join now! See [Call To Action](call.md) for further details.
