import onfido

api = onfido.Api("My_API_Key")

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"

check_details = {
    "applicant_id": fake_uuid,
    "report_names": ["identity_enhanced"]
}


def test_create_check(requests_mock):
    mock_create = requests_mock.post("https://api.onfido.com/v3/checks/", json=[])
    api.check.create(check_details)
    assert mock_create.called is True
    assert mock_create.last_request.text is not None

def test_find_check(requests_mock):
    mock_find = requests_mock.get(f"https://api.onfido.com/v3/checks/{fake_uuid}", json=[])
    api.check.find(fake_uuid)
    assert mock_find.called is True

def test_list_checks(requests_mock):
    mock_list = requests_mock.get(f"https://api.onfido.com/v3/checks/?applicant_id={fake_uuid}", json=[])
    api.check.all(fake_uuid)
    assert mock_list.called is True

def test_resume_check(requests_mock):
    mock_resume = requests_mock.post(f"https://api.onfido.com/v3/checks/{fake_uuid}/resume", json=[])
    api.check.resume(fake_uuid)
    assert mock_resume.called is True
