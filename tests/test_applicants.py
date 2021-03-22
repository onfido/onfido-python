import onfido

api = onfido.Api("<AN_API_TOKEN>")

applicant_details = {
  "first_name": "Jane",
  "last_name": "Doe",
  "dob": "1984-01-01",
  "address": {
    "street": "Second Street",
    "town": "London",
    "postcode": "S2 2DF",
    "country": "GBR"
  }
}

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_create_applicant(requests_mock):
    mock_create = requests_mock.post("https://api.eu.onfido.com/v3.1/applicants/", json=[])
    api.applicant.create(applicant_details)
    assert mock_create.called is True

def test_find_applicant(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.1/applicants/{fake_uuid}", json=[])
    api.applicant.find(fake_uuid)
    assert mock_find.called is True

def test_update_applicant(requests_mock):
    mock_update = requests_mock.put(f"https://api.eu.onfido.com/v3.1/applicants/{fake_uuid}", json=[])
    api.applicant.update(fake_uuid, applicant_details)
    assert mock_update.called is True

def test_delete_applicant(requests_mock):
    mock_delete = requests_mock.delete(f"https://api.eu.onfido.com/v3.1/applicants/{fake_uuid}", json=[])
    api.applicant.delete(fake_uuid)
    assert mock_delete.called is True

def test_restore_applicant(requests_mock):
    mock_restore = requests_mock.post(f"https://api.eu.onfido.com/v3.1/applicants/{fake_uuid}/restore", json=[])
    api.applicant.restore(fake_uuid)
    assert mock_restore.called is True

def test_list_applicants(requests_mock):
    mock_list = requests_mock.get("https://api.eu.onfido.com/v3.1/applicants", json=[])
    api.applicant.all(include_deleted=True, per_page=5, page=2)
    history = mock_list.request_history
    assert mock_list.called is True
    assert history[0].method == 'GET'
    assert history[0].url == "https://api.eu.onfido.com/v3.1/applicants?include_deleted=True&per_page=5&page=2"
