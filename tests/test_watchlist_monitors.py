
import onfido
from onfido.regions import Region


api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

watchlist_details = {
    "applicant_id": "12345",
    "report_name": "watchlist_standard",
    "tags": [
        "dummy_tag",
    ],
}

fake_uuid = "96264b11-f734-4074-8be0-641c0099114c"


def test_create_monitor(requests_mock):
    mock_create = requests_mock.post("https://api.eu.onfido.com/v3.5/watchlist_monitors/", json=[])
    api.watchlist_monitor.create(watchlist_details)
    assert mock_create.called is True

def test_find_monitor(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.5/watchlist_monitors/{fake_uuid}", json=[])
    api.watchlist_monitor.find(fake_uuid)
    assert mock_find.called is True

def test_delete_monitor(requests_mock):
    mock_delete = requests_mock.delete(f"https://api.eu.onfido.com/v3.5/watchlist_monitors/{fake_uuid}", json=[])
    api.watchlist_monitor.delete(fake_uuid)
    assert mock_delete.called is True

def test_list_monitors(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.5/watchlist_monitors?applicant_id={fake_uuid}", json=[])
    api.watchlist_monitor.all(fake_uuid)
    assert mock_list.called is True
    
