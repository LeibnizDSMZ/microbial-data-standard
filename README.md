[![release: 0.3.0](https://img.shields.io/badge/rel-0.3.0-blue.svg?style=flat-square)](https://github.com/LeibnizDSMZ/microbial-data-standard)
[![MIT LICENSE](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![Documentation Status](https://img.shields.io/badge/docs-GitHub-blue.svg?style=flat-square)](https://LeibnizDSMZ.github.io/microbial-data-standard/)

*Please note that this project is still in development*


# Microbial Data Standard

This project defines a new microbial data standard for all data describing a microbial strain.
The new microbial data standard is part of the work of WP6 of the [Bioindustry 4.0](https://www.bioindustry4.eu/) project.

### Basic information

The new microbial data standard is defined as a data model written in [pydantic](https://pydantic.dev).
The model is used for data validation and to generate a JSON schema file, describing the microbial data standard.

The JSON-schema file is prebuilt and included in this project. You find the JSON schema in
`schema/microbe_schema.json`. The JSON schema will be used for data validation.

If you want to report a bug, contribute to the project or suggest new features, please contact the project owner.


### How to use

The provided data model and schema are for data validation.


Examples for using the pydantic data model:

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
