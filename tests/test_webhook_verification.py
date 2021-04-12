import onfido
from onfido.regions import Region
from onfido.webhook_event_verifier import WebhookEventVerifier
from onfido.exceptions import OnfidoInvalidSignatureError
import pytest

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

raw_event = (
    '{"payload":'
    '{"resource_type":"check","action":"check.completed","object":'
    '{"id":"check-123",'
    '"status":"complete","completed_at_iso8601":"2020-01-01T00:00:00Z",'
    '"href":"https://api.onfido.com/v3/checks/check-123"}}}'
)

secret_token = "_ABC123abc123ABC123abc123ABC123_"

expected_event = {
    "action": "check.completed",
    "resource_type": "check",
    "object": {
        "id": "check-123",
        "href": "https://api.onfido.com/v3/checks/check-123",
        "status": "complete",
        "completed_at_iso8601": "2020-01-01T00:00:00Z"
    }
}

verifier = WebhookEventVerifier(secret_token)


def test_webhook_verification():
    signature = "a0082d7481f9f0a2907583dbe1f344d6d4c0d9989df2fd804f98479f60cd760e"

    event = verifier.read_payload(raw_event, signature)
    assert event == expected_event


def test_webhook_verification_invalid_signature():
    signature = "b0082d7481f9f0a2907583dbe1f344d6d4c0d9989df2fd804f98479f60cd760e"

    with pytest.raises(OnfidoInvalidSignatureError):
        verifier.read_payload(raw_event, signature)
