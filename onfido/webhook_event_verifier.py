import hmac
import hashlib

from .models import WebhookEvent


class OnfidoInvalidSignatureError(Exception):
    pass


class WebhookEventVerifier:
    def __init__(self, webhook_token):
        self.webhook_token = webhook_token

    def read_payload(self, raw_event, signature):
        # Compute the the actual HMAC signature from the raw request body.
        event_signature = hmac.new(
            key=self.webhook_token.encode("utf-8"),
            msg=raw_event.encode("utf-8"),
            digestmod=hashlib.sha256,
        ).hexdigest()

        # Compare the signatures (prevent against timing attacks).
        if not hmac.compare_digest(signature, event_signature):
            raise OnfidoInvalidSignatureError("Invalid signature for webhook event")

        return WebhookEvent.from_json(raw_event)
