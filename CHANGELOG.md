# Changelog

## v5.6.0 15th January 2026

- Release based on Onfido OpenAPI spec version [v5.6.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v5.6.0):
  - [SIG-3270] Update document_type supported by PoA
  - [DEXTV2-9337] Update list of document subtypes for extraction
  - [STUDIO-5634] Add timeline_file_download_url to the webhook event resource

## v5.5.0 22nd September 2025

- Release based on Onfido OpenAPI spec version [v5.5.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v5.5.0):
  - [SIG-3128] Add ssn breakdowns to IDR enhanced report

## v5.4.0 28th July 2025

- Release based on Onfido OpenAPI spec version [v5.4.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v5.4.0):
  - [ENT-26] Add AES document download endpoint
- Fix dependabot error, add support for python 3.13 (and drop 3.8)
- [ENT-26] Add AES documents test

## v5.3.0 11th July 2025

- Release based on Onfido OpenAPI spec version [v5.3.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v5.3.0):
  - [DEXTV2-9494] Add manual_transmission_restriction to document with driver verification report

## v5.2.0 5th June 2025

- Release based on Onfido OpenAPI spec version [v5.2.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v5.2.0):
  - [BIO-7260] Add report configuration (including use_case) to checks

## v5.1.0 14th May 2025

- Release based on Onfido OpenAPI spec version [v5.1.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v5.1.0):
  - CAT-1760: create get applicant consents endpoint
  - [CAT-1911] Fix document_with_driving_licence_information to be a list of objects
  - [AF-1390] Fix: Device Intelligence Report Schema
  - [CAT-1944] Add OAuth fields for Webhook authentication
  - Fix storage of device_fingerprint_reuse breakdown and properties as float
  - Add .markdownlint.json to templates

## v5.0.0 21st February 2025

- Release based on Onfido OpenAPI spec version [v5.0.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v5.0.0):
  - Add missing type annotations to webhook verifier
  - Denote webhook event payload.object.href as a not required property
  - [CAT-1593] Drop invalid enum value from webhook event type
  - Add applicant_id in GET /workflow_runs
  - [CAT-1694] Define document file type as free text
  - [DOCCAP-2513] Add download-nfc-face endpoint
  - [CAT-1719] Don't impose a type on deprecated records property in watchlist reports
  - Remove documents property for reports where it's not applicable
  - Update openapi generator version to v7.10.0 (was v7.9.0)
  - Update openapi generator version to v7.11.0 (was v7.10.0)
- Add tests for Download NFC Face endpoint
- [Migration Guide](MIGRATION.md#upgrading-from-4x-to-5x)

## v4.6.0 24th January 2025

- Release based on Onfido OpenAPI spec version [v4.6.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v4.6.0):
  - (Python) Use Poetry only for dependency management
  - [STUDIO-4308] Add driving_license to id_number enum
  - [CAT-1634] Add proxy configuration support to Java client library
  - Update README files (including templated ones)
  - Add customer_user_id in the webhook event resource
- test: wait for evidence folder to be available

## v4.5.0 8th January 2025

- Release based on Onfido OpenAPI spec version [v4.5.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v4.5.0):
  - [STUDIO-4305] Add download evidence folder path

## v4.4.0 20th December 2024

- Release based on Onfido OpenAPI spec version [v4.4.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v4.4.0):
  - [CAT-1593] Fix missing webhook type and evidence folder webhook
  - [CAT-1590] Allow any type for the workflow task output

## v4.3.0 27th November 2024

- Release based on Onfido OpenAPI spec version [v4.3.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v4.3.0):
  - [CAT-1581] Revert "[CAT-1528] Fix barcode field in document properties object"

## v4.2.0 19th November 2024

- Release based on Onfido OpenAPI spec version [v4.2.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v4.2.0):
  - feat: add new fields to facial similarity report objects
  - [CAT-1552] Add missing document types

## v4.1.0 8th November 2024

- Release based on Onfido OpenAPI spec version [v4.1.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v4.1.0):
  - [CAT-1528] Fix barcode field in document properties object

## v4.0.0 24th October 2024

- Release based on Onfido OpenAPI spec version [v4.0.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v4.0.0):
  - [CAT-1379] Add a few missing properties
  - [CAT-1447] Fix applicant consents
  - [CAT-1379] Fix check creation, remove some deprecated properties and deprecate others
  - Use document-type enum for document upload
  - [CAT-1306] Add webhooks event resource
  - Upgrade OpenAPI generator to v7.9.0 (was v7.6.0)
  - [Migration Guide](MIGRATION.md#upgrading-from-3x-to-4x)

## v3.5.0 20th September 2024

- Release based on Onfido OpenAPI spec version [v3.5.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v3.5.0):
  - [CAT-1376] Add record item object definition for watchlist enhanced properties field

## v3.4.0 24th July 2024

- Release based on Onfido OpenAPI spec version [v3.3.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v3.3.0):
  - Expose `customer_user_id` in `workflow_runs`
  - Add `sdk_token` to workflow run schema

## v3.3.0 17th July 2024

- Release based on Onfido OpenAPI spec version [v3.2.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v3.2.0):
  - [CAT-1289] Document report's properties: Add middle name
  - chore(qes): add documents endpoint
  - [CAT-1297] Webhook Event: remove uuid format from object.id
  - fix(qes): fix download document http method
  - Add started_at_iso8601 field in webhook event
  - add jpeg file type for documents

## v3.2.0 2nd July 2024

- Release based on Onfido OpenAPI spec version [v3.1.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v3.1.0):
  - Add missing fields in document report's properties

## v3.1.0 24th June 2024

- Library has been rebuilt from scratch and automatically generated on [Onfido OpenAPI Spec](https://github.com/onfido/onfido-openapi-spec) (release [v3.0.0](https://github.com/onfido/onfido-openapi-spec/releases/tag/v3.0.0))
- Integration tests have also been implemented

## v3.0.0 13th June 2024 (pre-release)

- Make library auto-generated and based on [Onfido OpenAPI spec](https://github.com/onfido/onfido-openapi-spec)

## v2.10.0 24th November 2023

- Added core methods for [WorkflowRuns](https://documentation.onfido.com/#workflow-runs)

## v2.9.0 24th November 2023

- Added `signed_evidence_file` method for WorkflowRuns

## v2.8.0, 15th November 2023

- Support asyncio API
- Handle filenames with a uppercase file extension
- Replace pkg_resources

## v2.7.0, 24th January 2023

- Update to use API v3.6, for more details please see our [release notes](https://developers.onfido.com/release-notes#api-v36)
- Added Watchlist monitors
- Handle filenames with a uppercase file extension
- Bump certifi from 2020.6.20 to 2022.12.7
- Add support for python 3.10

## v2.6.0, 22nd November 2022

- Add Motion support

## v2.5.0, 11th November 2022

- Update to use API v3.5, for more details please see our [release notes](https://developers.onfido.com/release-notes#api-v35)

## v2.4.1, 2nd Jun 2022

- Fix boolean serialization in upload request ([issue #25](https://github.com/onfido/onfido-python/issues/25))

## v2.4.0, 12th May 2022

- Update to use API v3.4, for more details please see our [release notes](https://developers.onfido.com/release-notes#api-v34)

## v2.3.0, 11 April 2022

- Improve error handling for 422 errors

## v2.2.0, 2nd March 2022

- Update to use API v3.3

## v2.1.0, 24th June 2021

- Update to use API v3.2

## v2.0.0, 12 April 2021

- `base_url` parameter has become `region`, which takes one of `Region.EU`, `Region.US` or `Region.CA` and no longer has a default value
- Added support for 'Download check' endpoint

## v1.3.1, 09 March 2021

- Updates README.

## v1.3.0, 04 February 2021

- Updates README with live video functionality.
- Marks Resource methods private.

## v1.2.0, 25 November 2020

- Adds option to set global configuration for timeouts.

## v1.1.1, 22 October 2020

- Fixed arguments for extraction.

## v1.1.0, 20 October 2020

- Added support for Extraction (a.k.a. Autofill).

## v1.0.0, 12 August 2020

- Full release

## v0.5.0, 6 August 2020

- Added User-Agent header

## v0.4.0, 30 June 2020

- Beta version released
