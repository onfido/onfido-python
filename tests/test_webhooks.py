import pytest

from onfido import ApiException, Webhook, WebhookBuilder, WebhooksList, WebhookUpdater


@pytest.fixture
def webhook(onfido_api):
    webhook_builder = WebhookBuilder(
        url="https://example.com", events=["check.completed", "report.completed"]
    )
    return onfido_api.create_webhook(webhook_builder)


def test_create_webhook(webhook):
    assert isinstance(webhook, Webhook)
    assert webhook.id is not None
    assert webhook.url == "https://example.com"
    assert webhook.events == ["check.completed", "report.completed"]


def test_update_webhook(onfido_api, webhook):
    webhook_updater = WebhookUpdater(
        url="https://example.co.uk", events=["check.completed"]
    )
    updated_webhook = onfido_api.update_webhook(webhook.id, webhook_updater)

    assert updated_webhook.id == webhook.id
    assert updated_webhook.url == "https://example.co.uk"
    assert updated_webhook.events == ["check.completed"]


def test_list_webhooks(onfido_api):
    list_of_webhooks = onfido_api.list_webhooks()

    assert isinstance(list_of_webhooks, WebhooksList)
    assert len(list_of_webhooks.webhooks) > 0


def test_find_webhook(onfido_api, webhook):
    get_webhook = onfido_api.find_webhook(webhook.id)

    assert get_webhook.id == webhook.id


def test_delete_webhook(onfido_api, webhook):
    onfido_api.delete_webhook(webhook.id)

    with pytest.raises(ApiException):
        onfido_api.find_webhook(webhook.id)
