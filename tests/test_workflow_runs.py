import onfido
from onfido.regions import Region
from urllib.parse import urlparse, parse_qs

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

workflow_run_details = {
    "applicant_id": "12345",
    "completed_redirect_url": "https://<completed URL>",
    "expired_redirect_url": "https://<expired URL>",
    "expires_at": "2023-11-17T16:39:04Z",
    "language": "en_US"
}

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"

def test_create_workflow_run(requests_mock):
    mock_create = requests_mock.post("https://api.eu.onfido.com/v3.6/workflow_runs/", json=[])
    api.workflowrun.create(workflow_run_details)
    assert mock_create.called is True

def test_list_workflow_runs(requests_mock):
    mock_list = requests_mock.get("https://api.eu.onfido.com/v3.6/workflow_runs", json=[])
    api.workflowrun.all(
        page=2, 
        status="approved,declined", 
        tags="dummy_tag1,dummy_tag2", 
        created_at_gt="2023-11-17T16:39:04Z",
        created_at_lt="2008-02-29T02:56:37Z",
        sort='asc'
    )
    history = mock_list.request_history
    assert mock_list.called is True
    assert history[0].method == 'GET'
    query_params = urlparse(history[0].url).query
    assert history[0].url == "https://api.eu.onfido.com/v3.6/workflow_runs?" + query_params
    assert parse_qs(query_params) == { 
        "page": ['2'], 
        "status": ["approved,declined"], 
        "tags": ["dummy_tag1,dummy_tag2"],         
        "created_at_gt": ["2023-11-17T16:39:04Z"],
        "created_at_lt": ["2008-02-29T02:56:37Z"],
        "sort": ['asc']
    }

def test_find_workflow_run(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.6/workflow_runs/{fake_uuid}", json=[])
    api.workflowrun.find(fake_uuid)
    assert mock_find.called is True

def test_evidence_workflowrun(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.6/workflow_runs/{fake_uuid}/signed_evidence_file", text="FAKE PDF BINARY", headers={"Content-type": "application/pdf"})
    onfido_download = api.workflowrun.evidence(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "application/pdf"   
