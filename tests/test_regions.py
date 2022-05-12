import onfido
from onfido.regions import Region

applicant_details = {
  "first_name": "Optimus",
  "last_name": "Prime"
}


def test_europe_region(requests_mock):
    api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)
    mock_create = requests_mock.post("https://api.eu.onfido.com/v3.4/applicants/", json=[])
    api.applicant.create(applicant_details)
    assert mock_create.called is True

def test_canada_region(requests_mock):
    api = onfido.Api("<AN_API_TOKEN>", region=Region.CA)
    mock_create = requests_mock.post("https://api.ca.onfido.com/v3.4/applicants/", json=[])
    api.applicant.create(applicant_details)
    assert mock_create.called is True

def test_us_region(requests_mock):
    api = onfido.Api("<AN_API_TOKEN>", region=Region.US)
    mock_create = requests_mock.post("https://api.us.onfido.com/v3.4/applicants/", json=[])
    api.applicant.create(applicant_details)
    assert mock_create.called is True

