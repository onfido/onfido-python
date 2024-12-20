from onfido.webhook_event_verifier import WebhookEventVerifier, OnfidoInvalidSignatureError
from onfido import (
    WebhookEvent, WebhookEventPayload, WebhookEventPayloadObject,
    WebhookEventResourceType, WebhookEventType, WebhookEventObjectStatus,
    WebhookEventPayloadResource
)

import pytest

raw_event = ("{\"payload\":{\"resource_type\":\"workflow_task\",\"action\":\"workflow_task.started\","
             "\"object\":{\"id\":\"profile_1eb92\",\"task_spec_id\":\"profile_1eb92\","
             "\"task_def_id\":\"profile_data\",\"workflow_run_id\":\"bc77c6e5-753a-4580-96a6-aaed3e5a8d19\""
             ",\"status\":\"started\",\"started_at_iso8601\":\"2024-07-10T12:49:09Z\","
             "\"href\":\"https://api.eu.onfido.com/v3.6/workflow_runs/"
             "bc77c6e5-753a-4580-96a6-aaed3e5a8d19/tasks/profile_1eb92\"},"
             "\"resource\":{\"created_at\":\"2024-07-10T12:49:09Z\",\"id\":""\"profile_1eb92\","
             "\"workflow_run_id\":\"bc77c6e5-753a-4580-96a6-aaed3e5a8d19\",\"updated_at\":\"2024-07-10T12:49:09Z\""
             ",\"input\":{},\"task_def_version\":null,\"task_def_id\":\"profile_data\",\"output\":null}}}")

secret_token = "YKOC6mkBxi6yK2zlUIrLMvsJMFEZObP5"

expected_event = WebhookEvent(
    payload=WebhookEventPayload(
        action=WebhookEventType.WORKFLOW_TASK_DOT_STARTED,
        resource_type=WebhookEventResourceType.WORKFLOW_TASK,
        object=WebhookEventPayloadObject(
            id='profile_1eb92',
            href='https://api.eu.onfido.com/v3.6/workflow_runs/bc77c6e5-753a-4580-96a6-aaed3e5a8d19/tasks/profile_1eb92',
            status=WebhookEventObjectStatus.STARTED,
            started_at_iso8601='2024-07-10T12:49:09Z',
            task_def_id='profile_data',
            task_spec_id='profile_1eb92',
            workflow_run_id='bc77c6e5-753a-4580-96a6-aaed3e5a8d19'
        ),
        resource=WebhookEventPayloadResource(
            created_at='2024-07-10T12:49:09Z',
            id='profile_1eb92',
            input={},
            output=None,
            task_def_id='profile_data',
            task_def_version=None,
            updated_at='2024-07-10T12:49:09Z',
            workflow_run_id='bc77c6e5-753a-4580-96a6-aaed3e5a8d19'
        )
    )
)

verifier = WebhookEventVerifier(secret_token)


def test_webhook_verification():
    signature = "c95a5b785484f6fa1bc25f381b5595d66bf85cb442eefb06aa007802ee6a4dfa"

    event = verifier.read_payload(raw_event, signature)
    event.payload.object.additional_properties = {}    # Suppress any additional property in object
    assert event == expected_event


def test_webhook_verification_invalid_signature():
    signature = "c95a5b785484f6fa1bc25f381b5595d66bf85cb442eefb06aa007802ee6a4dfb"

    with pytest.raises(OnfidoInvalidSignatureError):
        verifier.read_payload(raw_event, signature)


def test_webhook_verification_with_object_in_output():
    signature = "e3e5565647f5ccf07b2fd8ac22eab94a0a0619413d981fb768295c820523f7d7"

    with open('tests/media/studio_webhook_event_with_object_in_output.json', 'r') as file:
        event = verifier.read_payload(file.read(), signature)

    assert event.payload.resource.output['properties'] == {
        'date_of_birth': '1990-01-01',
        'date_of_expiry': '2031-05-28',
        'document_number': '999999999',
        'document_numbers': [
            {
                'type': 'document_number',
                'value': '999999999'
            }
        ],
       'document_type': 'passport',
       'first_name': 'Jane',
       'issuing_country': 'GBR',
       'last_name': 'Doe',
    }


def test_webhook_verification_with_list_in_output():
    signature = "f3a5170acfcecf8c1bf6d9cb9995c0d9dec941af83056a721530f8de7af2c293"

    with open('tests/media/studio_webhook_event_with_list_in_output.json', 'r') as file:
        event = verifier.read_payload(file.read(), signature)

    assert event.payload.resource.output == [
        {
          'checksum_sha256': 'hiwV2PLmeQZzeySPGGwVL48sxVXcyfpXy9LDl1u3lWU=',
          'id': '7af75a3a-ba34-4aa5-9e3e-096c9f56256b',
          'type': 'document_photo'
        }
    ]
