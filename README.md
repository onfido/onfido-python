# Onfido Python Client Library

[onfido-python on PyPI](https://pypi.org/project/onfido-python/)

Version 1.2.0

The official wrapper for Onfido's API. Refer to the full [API documentation](https://documentation.onfido.com) for details of expected requests and responses.

This project supersedes the automatically generated [api-python-client](https://github.com/onfido/api-python-client) library (`onfido` in PyPI).

## Installation

`pip install onfido-python`

:warning: Having the old `onfido` package installed at the same time will cause errors.

## Usage

Make API calls by using an instance of the `Api` class and providing your API
token:

```python
import onfido

api = onfido.Api("<YOUR_API_TOKEN>")
```

### Regions

Set the region in the API instance using the `base_url` parameter.

The library will use the default base URL (api.onfido.com) for the EU region, if
no region is specified.

To specify the US region do:

```python
from onfido.regions import Region

api = onfido.Api("<YOUR_API_TOKEN>", base_url=Region.US)
```

To specify the CA region do:

```python
from onfido.regions import Region

api = onfido.Api("<YOUR_API_TOKEN>", base_url=Region.CA)
```

See https://documentation.onfido.com/#regions for supported regions.

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

### Response format

The Python library will return data directly from the API.

See https://documentation.onfido.com/#request,-response-format for more
information.

### Resources

All resources share the same interface when making API calls. For example, use
`.create` to create a resource, `.find` to find one, and `.all` to fetch all
resources.

#### Applicants

Applicants are the object upon which Onfido checks are performed.

```python
api.applicant.create(params)  # => Creates an applicant
api.applicant.update("<APPLICANT_ID>", params)  # => Updates an applicant
api.applicant.delete("<APPLICANT_ID>")  # => Schedule an applicant for deletion
api.applicant.restore("<APPLICANT_ID>") # => Restore an applicant scheduled for deletion
api.applicant.find("<APPLICANT_ID>")  # => Finds a single applicant
api.applicant.all()  # => Returns all applicants
```

`applicant.all()` takes the following optional arguments:

`include_deleted=true`: include applicants scheduled for deletion.
`per_page`: set the number of results per page. Defaults to 20.
`page`: return specific pages. Defaults to 1.

**Note:** Calling `api.applicant.delete` adds the applicant and all associated
documents, photos, videos, checks, reports and analytics data to our deletion
queue. Please read https://documentation.onfido.com/#delete-applicant for more
information.

#### Documents

Some report types require identity documents (passport, driving licence etc.) in order to be processed.

```python
request_body = {"applicant_id": "<APPLICANT_ID>", "type": "passport"}
sample_file = open("<FILE_NAME>", "rb")

api.document.upload(sample_file, request_body)   # => Uploads a document
api.document.find("<DOCUMENT_ID>")      # => Finds a document
api.document.download("<DOCUMENT_ID>")  # => Downloads a document as a binary data
api.document.all("<APPLICANT_ID>")      # => Returns all documents belonging to an applicant
```

See https://documentation.onfido.com/#document-types for example document types.

#### Live Photos

Live photos are images of the applicant’s face, typically taken at the same time as documents are provided. These photos are used to perform Facial Similarity Photo reports on the applicant.

```python
request_body = {"applicant_id": "<APPLICANT_ID>", "advanced_validation": "True"}
sample_file = open("<FILE_NAME>", "rb")

api.live_photo.upload(sample_file, request_body)   # => Uploads a live photo
api.live_photo.find("<LIVE_PHOTO_ID>")      # => Finds a live photo
api.live_photo.download("<LIVE_PHOTO_ID>")  # => Downloads a live photo as binary data
api.live_photo.all("<APPLICANT_ID>")        # => Returns all live photos belonging to an applicant
```

#### Checks

Checks are performed on an applicant. Depending on the type of check you wish to perform, different information will be required when you create an applicant. A check consists of one or more reports.

```python
request_body = {"applicant_id": "12345", "report_names": ["document", "facial_similarity_photo"]}

api.check.create(request_body) # => Creates a check
api.check.find("<CHECK_ID>")    # => Finds a check
api.check.resume("<CHECK_ID>")  # => Resumes a paused check
api.check.all("<APPLICANT_ID>") # => Returns all an applicant's checks
```

#### Reports

Reports provide details of the results of some part of a check. They are
created when a check is created, so the Onfido API only provides support for
finding and listing them. For paused reports specifically, additional support for resuming and
 cancelling reports is also available.

```python
api.report.find("<REPORT_ID>")    # => Finds a report
api.report.resume("<REPORT_ID>")  # => Resumes a paused report
api.report.all("<CHECK_ID>")      # => Returns all the reports in a check
api.report.cancel("<REPORT_ID>")  # => Cancels a paused report
```

#### Address Lookups

Onfido provides an address lookup service, to help ensure well-formatted
addresses are provided when creating applicants. To search for addresses
by postcode, use:

```python
api.address.pick("SW46EH") # => Returns all addresses in a given postcode
```

#### Webhook Endpoints

Onfido allows you to set up and view your webhook endpoints via the API, as well
as through the Dashboard.

```python
request_body = {
  "url": "https://<URL>",
  "events": [
    "report.completed",
    "check.completed"
  ]
}

api.webhook.create(request_body) # => Registers a webhook
api.webhook.find("<WEBHOOK_ID>")  # => Finds a single webhook
api.webhook.edit("<WEBHOOK_ID>", new_webhook_details) # => Edits a webhook
api.webhook.delete("<WEBHOOK_ID>") # => Deletes a webhook
api.webhook.all() # => Returns all webhooks
```

##### Webhook Verification

A webhook event is valid if the signature from the header is equal to the
expected signature you compute for it.

```python
event = verifier.read_payload(raw_event, signature)
```

See https://documentation.onfido.com/#verifying-webhook-signatures for more information.

#### SDK Tokens

Onfido allows you to generate JSON Web Tokens via the API in order to authenticate
with Onfido's SDKs.

```python
request_body = {"applicant_id": "<APPLICANT_ID>", "application_id": "<APPLICATION_ID>"}

api.sdk_token.generate(request_body) # => Creates an SDK token
```

#### Extraction (Autofill)

Extract data from documents. This endpoint only returns extracted data that can be used for automatic form filling.
You must provide the ID of a document that has already been uploaded.

```python
api.extraction.perform("<DOCUMENT_ID>") # => Returns data extracted from the document
```

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
