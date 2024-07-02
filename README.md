# Onfido Python Library

The official Python library for integrating with the Onfido API.

Documentation can be found at <https://documentation.onfido.com>.

This version uses Onfido API v3.6. Refer to our [API versioning guide](https://developers.onfido.com/guide/api-versioning-policy#client-libraries) for details of which client library versions use which versions of the API.

[![PyPI version](https://badge.fury.io/py/onfido-python.svg)](https://badge.fury.io/py/onfido-python)
![Build Status](https://github.com/onfido/onfido-python/actions/workflows/python.yml/badge.svg)

## Installation & Usage

### Requirements

Python 3.7+

### Installation

#### Pip

If the python package is hosted on a repository, you can install directly using:

```sh
pip install onfido-python
```

Then import the package:

```python
import onfido
```

#### Poetry

```sh
poetry add onfido-python
```

Then import the package:

```python
import onfido
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Import the `DefaultApi` object, this is the main object used for interfacing with the API:

```python
import onfido

import urllib3
from os import environ

configuration = onfido.Configuration(
    api_token=environ['ONFIDO_API_TOKEN'],
    region=onfido.configuration.Region.EU,     # Supports `EU`, `US` and `CA`
    timeout=urllib3.util.Timeout(connect=60.0, read=60.0)
  )

with onfido.ApiClient(configuration) as api_client:
  onfido_api = onfido.DefaultApi(api_client)
  ...
```

NB: by default, timeout values are set to 30 seconds.

### Making a call to the API

```python
  try:
    applicant = onfido_api.create_applicant(
        onfido.ApplicantBuilder(
          first_name= 'First',
          last_name= 'Last')
      )

    # To access the information access the desired property on the object, for example:
    applicant.first_name

    # ...

  except OpenApiException:
    # ...
    pass
  except Exception:
    # ...
    pass
```

Specific exception types are defined into [exceptions.py](onfido/exceptions.py).

### Webhook event verification

Webhook events payload needs to be verified before it can be accessed. Library allows to easily decode the payload and verify its signature before returning it as an object for user convenience:

```python
  try:
    verifier = onfido.WebhookEventVerifier(os.environ["ONFIDO_WEBHOOK_SECRET_TOKEN"])

    signature = "a0...760e"

    event = verifier.read_payload('{"payload":{"r...3"}}', signature)
  except onfido.OnfidoInvalidSignatureError:
    # Invalid webhook signature
    pass
```

### Recommendations

#### Do not use additional properties

Retain from using `additional_properties` dictionary to access not defined properties to avoid breaking changes when these fields will appear.

## Contributing

This library is automatically generated using [OpenAPI Generator](https://openapi-generator.tech) (version: 7.6.0); therefore all the contributions, except tests files, should target [Onfido OpenAPI specification repository](https://github.com/onfido/onfido-openapi-spec/tree/master) instead of this repository.

For contributions to the tests instead, please follow the steps below:

1. [Fork](https://github.com/onfido/onfido-python/fork) repository
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request

## Versioning policy

[Semantic Versioning](https://semver.org) policy is used for library versioning, following guidelines and limitations below:

- MAJOR versions (x.0.0) might:
  - target a new API version
  - include non-backward compatible change
- MINOR versions (0.x.0) might:
  - add a new functionality, non-mandatory parameter or property
  - deprecate an old functionality
  - include non-backward compatible change to a functionality which is:
    - labelled as alpha or beta
    - completely broken and not usable
- PATCH version (0.0.x) might:
  - fix a bug
  - include backward compatible changes only

## More documentation

More documentation and code examples can be found at <https://documentation.onfido.com>.

## Support

Should you encounter any technical issues during integration, please contact Onfido's Customer Support team via the [Customer Experience Portal](https://public.support.onfido.com/) which also includes support documentation.
