[![Documentation Status](https://img.shields.io/badge/docs-GitHub-blue.svg?style=flat-square)](https://LeibnizDSMZ.github.io/microbial-data-standard/)

# Microbial Data Standard

This project defines a new microbial data standard for culture collection strain data.


## Technical information

The data model presented here is implemented with the use of
[pydantic](https://pydantic.dev).

Also included in the project is the JSON-schema file of the new data standard.

This project is initiated by Work Package 6 of the Bioindustry 4.0 (funded by the EU).

If you want to report a bug, contribute to the project or suggest new features, please open a issue or contact the project owner.

## How to use

Import:
```python
from microbial_strain_data_model.microbe import Microbe
```

Generate JSON schema:
```python
import json
from microbial_strain_data_model.microbe import Microbe

mi = Microbe.model_json_schema()
print(json.dumps(mi, indent=2))
```

Validate a JSON against the pydantic model:
```python
from microbial_strain_data_model.microbe import Microbe

with open("PATH_TO_FILE", "r") as f_in:
        file_content = f_in.read()

Microbe.model_validate_json(file_content)
```

Validate a JSON against the JSON schema:
```python
import jsonschema
import json

with open("PATH_TO_SCHEMA", "r") as schema_file:
        schema = json.load(schema_file)

with open("PATH_TO_FILE", "r") as f_in:
        json_content = json.loads(f_in)

jsonschema.validate(json_content, schema)
```
