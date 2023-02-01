import onfido
from onfido.regions import Region


api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"

check_details = {
    "applicant_id": fake_uuid,
    "report_names": ["identity_enhanced"]
}


def test_create_check(requests_mock):
    mock_create = requests_mock.post("https://api.eu.onfido.com/v3.6/checks/", json=[])
    api.check.create(check_details)
    assert mock_create.called is True
    assert mock_create.last_request.text is not None

def test_find_check(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.6/checks/{fake_uuid}", json=[])
    api.check.find(fake_uuid)
    assert mock_find.called is True

def test_list_checks(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.6/checks/?applicant_id={fake_uuid}", json=[])
    api.check.all(fake_uuid)
    assert mock_list.called is True

def test_resume_check(requests_mock):
    mock_resume = requests_mock.post(f"https://api.eu.onfido.com/v3.6/checks/{fake_uuid}/resume", json=[])
    api.check.resume(fake_uuid)
    assert mock_resume.called is True

def test_download_check(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.6/checks/{fake_uuid}/download", text="FAKE PDF BINARY", headers={"Content-type": "application/pdf"})
    onfido_download = api.check.download(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "application/pdf"    
