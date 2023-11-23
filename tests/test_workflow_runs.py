import onfido
from onfido.regions import Region


api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"

def test_evidence_workflowrun(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.6/workflow_runs/{fake_uuid}/signed_evidence_file", text="FAKE PDF BINARY", headers={"Content-type": "application/pdf"})
    onfido_download = api.workflowrun.evidence(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "application/pdf"   
