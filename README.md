# MaLo Ident Python Models

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python Versions (officially) supported](https://img.shields.io/pypi/pyversions/maloident.svg)
![Pypi status badge](https://img.shields.io/pypi/v/maloident)
![Unittests status badge](https://github.com/Hochfrequenz/malo-ident-python-models/workflows/Unittests/badge.svg)
![Coverage status badge](https://github.com/Hochfrequenz/malo-ident-python-models/workflows/Coverage/badge.svg)
![Linting status badge](https://github.com/Hochfrequenz/malo-ident-python-models/workflows/Linting/badge.svg)
![Black status badge](https://github.com/Hochfrequenz/malo-ident-python-models/workflows/Formatting/badge.svg)

This package provides mostly autogenerated [pydantic](https://docs.pydantic.dev/latest/)-based model classes for the MaLo ident API.

It does not provide you with an HTTP client.

## Installation
Install it from [PyPI](https://pypi.org/projects/maloident)
```bash
pip install maloident
```

Then use it:

```python
from maloident.models import ResultNegative
my_json = {
    "decisionTree": "E_0594",
    "responseCode": "A10",
    "reason": "Ich bin ein Freitext.",
    "networkOperator": 9900987654321,
}
result = ResultNegative.model_validate(my_json)
```

The request payload type for the Lieferant➡️Netzbetreiber identification request is `maloident.models.IdentificationParameter`.

See the [tests](unittests/test_models.py) for more examples.

## Project Structure
This project is based on [`datamodel-code-generator`](https://github.com/koxudaxi/datamodel-code-generator/).
Most of the classes are autogenerated from the [`openapi.yml`](openapi/openapi.yml) which can be found on [SwaggerHub](https://app.swaggerhub.com/apis/edi-energy/MaLoIdent_2024-07-03/v1.0.0).

Note that we fixed some errors in the official OpenAPI spec.
Our changes are mentioned at the beginning of the [`openapi.yml`](openapi/openapi.yml) file.

After updating the `openapi.yml` file, use
```bash
tox -e codegen
```
to re-generate the model classes.

## Contribute

You are very welcome to contribute to this template repository by opening a pull request against the main branch.