import onfido
from onfido.regions import Region

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

webhook_details = {
  "url": "https://<URL>",
  "events": [
    "report.completed",
    "check.completed"
  ]
}

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_create_webhook(requests_mock):
    mock_create = requests_mock.post("https://api.eu.onfido.com/v3.5/webhooks", json=[])
    api.webhook.create(webhook_details)
    assert mock_create.called is True

def test_list_webhooks(requests_mock):
    mock_list = requests_mock.get("https://api.eu.onfido.com/v3.5/webhooks", json=[])
    api.webhook.all()
    assert mock_list.called is True

def test_find_webhook(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.5/webhooks/{fake_uuid}", json=[])
    api.webhook.find(fake_uuid)
    assert mock_find.called is True

def test_edit_webhook(requests_mock):
    mock_edit = requests_mock.put(f"https://api.eu.onfido.com/v3.5/webhooks/{fake_uuid}", json=[])
    api.webhook.edit(fake_uuid, webhook_details)
    assert mock_edit.called is True

def test_delete_webhook(requests_mock):
    mock_delete = requests_mock.delete(f"https://api.eu.onfido.com/v3.5/webhooks/{fake_uuid}", json=[])
    api.webhook.delete(fake_uuid)
    assert mock_delete.called is True
