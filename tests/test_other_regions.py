import onfido
from onfido.regions import Region


applicant_details = {
  "first_name": "Optimus",
  "last_name": "Prime"
}


def test_canada_region(requests_mock):
    api = onfido.Api("<AN_API_TOKEN>", base_url=Region.CA)
    mock_create = requests_mock.post("https://api.ca.onfido.com/v3.1/applicants/", json=[])
    api.applicant.create(applicant_details)
    assert mock_create.called is True

def test_us_region(requests_mock):
    api = onfido.Api("<AN_API_TOKEN>", base_url=Region.US)
    mock_create = requests_mock.post("https://api.us.onfido.com/v3.1/applicants/", json=[])
    api.applicant.create(applicant_details)
    assert mock_create.called is True

