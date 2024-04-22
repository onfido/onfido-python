from onfido.webhook_event_verifier import WebhookEventVerifier, OnfidoInvalidSignatureError
from onfido import WebhookEvent, WebhookEventPayload, WebhookEventPayloadObject

import pytest

raw_event = ("{\"payload\":{\"resource_type\":\"check\",\"action\":\"check.completed\","
             "\"object\":{\"id\":\"f2302f45-227d-413d-ad61-09ec077a086a\",\"status\":\"complete\","
             "\"completed_at_iso8601\":\"2024-04-04T09:21:21Z\","
             "\"href\":\"https://api.onfido.com/v3.6/checks/f2302f45-227d-413d-ad61-09ec077a086a\"}}}")

secret_token = "wU99mE6jJ7nXOLFwZ0tJymM1lpI15pZh"

expected_event = WebhookEvent(
    payload=WebhookEventPayload(
        action="check.completed",
        resource_type="check",
        object=WebhookEventPayloadObject(
            id='f2302f45-227d-413d-ad61-09ec077a086a',
            href='https://api.onfido.com/v3.6/checks/f2302f45-227d-413d-ad61-09ec077a086a',
            status="complete",
            completed_at_iso8601='2024-04-04T09:21:21Z'
        )
    )
)

verifier = WebhookEventVerifier(secret_token)


def test_webhook_verification():
    signature = "77ebc3e418f26be6eebb47f7ebe551321de26734fc273961e075fc9ab163d9c7"

    event = verifier.read_payload(raw_event, signature)
    assert event == expected_event


def test_webhook_verification_invalid_signature():
    signature = "77ebc3e418f26be6eebb47f7ebe551321de26734fc273961e075fc9ab163d9c8"

    with pytest.raises(OnfidoInvalidSignatureError):
        verifier.read_payload(raw_event, signature)
