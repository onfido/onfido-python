# Migration Guide

This guide provides detailed instructions on how to upgrade between different
major versions of the client library.

It covers changes in core resources, other endpoints, and the OpenAPI generator,
ensuring a smooth transition between versions.

## Upgrading from 5.x to 6.x

### Core Resources

- Documents
  - Driving licence information properties removed from general `DocumentProperties`
    and moved to new `DocumentPropertiesWithDrivingLicenceInformation` class
- Workflow Runs
  - `created_at_gt` and `created_at_lt` parameters in `list_workflow_runs` changed from
    date-time format to date format (YYYY-MM-DD)

### Other Endpoints

- Reports
  - Device Intelligence: Removed deprecated `breakdown` property and related
    breakdown classes:
    - `DeviceIntelligenceBreakdownBreakdown` removed
    - `DeviceIntelligenceBreakdownProperties` → `DeviceIntelligenceProperties`
    - `DeviceIntelligenceBreakdownPropertiesDevice` → `DeviceIntelligencePropertiesDevice`
    - `DeviceIntelligenceBreakdownPropertiesGeolocation` → `DeviceIntelligencePropertiesGeolocation`
    - `DeviceIntelligenceBreakdownPropertiesIp` → `DeviceIntelligencePropertiesIp`
  - Identity Enhanced: Changed `total_number_of_sources` and `number_of_matches` from
    number to string type

### OpenAPI generator

- Version upgraded from `7.11.0` to `7.16.0`

## Upgrading from 4.x to 5.x

### Core Resources

- Documents
  - Allow any string as `file_type`

### Other Endpoints

- Webhooks
  - Drop `WORKFLOW_SIGNED_EVIDENCE_FILE_DOT_CREATED` enum value from
    `WebhookEventType` enum
  - Make `href` property in `WebhookEventPayloadObject` optional
- Reports
  - Allow the deprecated `records` property in `WatchlistAml` and
    `WatchlistStandard` reports to be any object, and not just a string
  - Remove `documents` property from all reports except Document and
    Facial Similarity reports

### OpenAPI generator

- Version upgraded from `7.9.0` to `7.11.0`

## Upgrading from 3.x to 4.x

### Core Resources

- Applicants
  - Replace broken `ConsentsBuilder` object with a list of `ApplicantConsentBuilder` ones
- Workflow Runs
  - Rename `WorkflowRunSharedLink` object into `WorkflowRunLink`
  - Define `WorkflowRunStatus` enum for storing status information
  - Rename `WorkflowRunResponseError` object into `WorkflowRunError`
- Documents
  - Reuse already existent `DocumentTypes` enum when uploading documents

### Other Endpoints

- Webhooks
  - Define `WebhookEventObjectStatus` enum to collect webhook event object's status
  - Define `WebhookEventResourceType` enum to collect webhhok event resource's type
  - Define `WebhookEventPayloadResource` object to store webhook payload's contents
- Checks
  - Define `CheckStatus` enum for accessing checks status
- Reports
  - Remove properties from `DeviceIntelligenceBreakdownPropertiesDevice` object: `true_os`, `os_anomaly`, `rooted` and `remote_software`
  - Remove properties from `DeviceIntelligenceBreakdownPropertiesIp` object: `vpn_detection`, `proxy_detection` and `type`

### OpenAPI generator

- Version upgraded from `7.6.0` to `7.9.0`
  - Remove support for python 3.7
