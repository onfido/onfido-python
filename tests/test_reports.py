import onfido

api = onfido.Api("<AN_API_TOKEN>")

check_details = {
    "applicant_id": "12345",
    "report_names": ["identity_enhanced"]
}

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_find_report(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.1/reports/{fake_uuid}", json=[])
    api.report.find(fake_uuid)
    assert mock_find.called is True

def test_list_reports(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.1/reports/?check_id={fake_uuid}", json=[])
    api.report.all(fake_uuid)
    assert mock_list.called is True

def test_resume_report(requests_mock):
    mock_resume = requests_mock.post(f"https://api.eu.onfido.com/v3.1/reports/{fake_uuid}/resume", json=[])
    api.report.resume(fake_uuid)
    assert mock_resume.called is True

def test_cancel_report(requests_mock):
    mock_cancel = requests_mock.post(f"https://api.eu.onfido.com/v3.1/reports/{fake_uuid}/cancel", json=[])
    api.report.cancel(fake_uuid)
    assert mock_cancel.called is True
