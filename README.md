# Onfido Python Client Library

[onfido-python on PyPI](https://pypi.org/project/onfido-python/)

The official wrapper for Onfido's API. Refer to the full [API documentation](https://documentation.onfido.com) for details of expected requests and responses for all resources.

[![PyPI version](https://badge.fury.io/py/onfido-python.svg)](https://badge.fury.io/py/onfido-python)

This version uses Onfido API v3.6. Refer to our [API versioning guide](https://developers.onfido.com/guide/api-versioning-policy#client-libraries) for details of which client library versions use which versions of the API.

This project supersedes the automatically generated [api-python-client](https://github.com/onfido/api-python-client) library (`onfido` in PyPI).

## Installation

`pip install onfido-python`

:warning: Having the old `onfido` package installed at the same time will cause errors.

## Getting started

Make API calls by using an instance of the `Api` class and providing your API
token:

```python
import onfido

api = onfido.Api("<YOUR_API_TOKEN>")
```

### Regions

Set the region in the API instance using the `region` parameter, which takes a value from the `Region` enum (currently `Region.EU`, `Region.US` or `Region.CA`).

For example, to specify the EU region:

```python
import onfido
from onfido.regions import Region

api = onfido.Api("<YOUR_API_TOKEN>", region=Region.EU)
```

`region` does not take a default parameter. Failure to pass a correct region will raise an `OnfidoRegionError`.

See https://documentation.onfido.com/#regions for more information about our supported regions at a given time.

### Timeouts

You can optionally set a global timeout for all requests in the API
constructor. This takes a floating number input and each whole integer
increment corresponds to a second. 

For example, to set a timeout of 1 second:

```python
api = onfido.Api("<YOUR_API_TOKEN>", timeout=1)
```

The default value for `timeout` is `None`, meaning no timeout will be set on
the client side.

## Response format

The Python library will return JSON requests directly from the API. Each request corresponds to a resource. 

All resources share the same interface when making API calls. For example, use `.create` to create a resource, `.find` to find one, and `.all` to fetch all resources. 

For example, to create an applicant:

```python
applicant_details = {
  'first_name': 'Jane',
  'last_name': 'Doe',
  'dob': '1984-01-01',
  'address': {
    'street': 'Second Street',
    'town': 'London',
    'postcode': 'S2 2DF',
    'country': 'GBR'
  },
  'location': {
    'ip_address': '127.0.0.1',
    'country_of_residence': 'GBR'
  }
}

api.applicant.create(applicant_details)
```

```python
{
  'id': '<APPLICANT_ID>',
  'created_at': '2019-10-09T16:52:42Z',
  'sandbox': True,
  'first_name': 'Jane',
  'last_name': 'Doe',
  'email': None,
  'dob': '1990-01-01',
  'delete_at': None,
  'href': '/v3.1/applicants/<APPLICANT_ID>',
  'id_numbers': [],
  'address': {
    'flat_number': None,
    'building_number': None,
    'building_name': None,
    'street': 'Second Street',
    'sub_street': None,
    'town': 'London',
    'state': None,
    'postcode': 'S2 2DF',
    'country': 'GBR',
    'line1': None,
    'line2': None,
    'line3': None
  },
  'phone_number': None,
  'location': {
    'ip_address': '127.0.0.1',
    'country_of_residence': 'GBR'
  }
}
```

See https://documentation.onfido.com/#request,-response-format for more
information.

### Resources

Resource information and code examples can be found at https://documentation.onfido.com/.

### Error Handling

- `OnfidoServerError` is raised whenever Onfido returns a `5xx` response
- `OnfidoRequestError` is raised whenever Onfido returns a `4xx` response
- `OnfidoInvalidSignatureError` is raised whenever a signature from the header is not equal to the expected signature you compute for it
- `OnfidoTimeoutError` is raised if a timeout occurs
- `OnfidoConnectionError` is raised whenever any other network error occurs
- `OnfidoUnknownError` is raised whenever something unexpected happens

## Contributing

1. Fork it ( https://github.com/onfido/onfido-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Run the tests (`poetry run pytest tests/test_my_new_feature.py`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request
