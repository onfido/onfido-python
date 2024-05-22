import pytest

from onfido import WorkflowRun, WorkflowRunBuilder
from tests.conftest import create_applicant, create_workflow_run


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function")
def workflow_id():
    return "e8c921eb-0495-44fe-b655-bcdcaffdafe5"


@pytest.fixture(scope="function")
def workflow_run(onfido_api, applicant_id, workflow_id):
    return create_workflow_run(
        onfido_api, applicant_id=applicant_id, workflow_id=workflow_id
    )


def test_create_workflow_run(workflow_run, workflow_id):
    assert workflow_run is not None
    assert isinstance(workflow_run, WorkflowRun)
    assert workflow_run.workflow_id == workflow_id
    assert workflow_run.status == "awaiting_input"


def test_create_workflow_run_with_custom_inputs(onfido_api, applicant_id):
    workflow_id = "45092b29-f220-479e-aa6f-a6f989baac4c"

    workflow_run_builder = WorkflowRunBuilder(
        applicant_id=applicant_id,
        workflow_id=workflow_id,
        custom_data={"age": 18, "is_employed": False}
    )
    workflow_run = create_workflow_run(onfido_api, workflow_run_builder=workflow_run_builder)
    assert isinstance(workflow_run, WorkflowRun)
    assert workflow_run.workflow_id == workflow_id
    assert workflow_run.status == "approved"


def test_list_workflow_runs(onfido_api):
    workflow_runs = onfido_api.list_workflow_runs()

    assert isinstance(workflow_runs[0], WorkflowRun)
    assert len(workflow_runs) > 0


def test_find_workflow_run(onfido_api, workflow_run):
    get_workflow_run = onfido_api.find_workflow_run(workflow_run.id)

    assert get_workflow_run.id == workflow_run.id
    assert isinstance(get_workflow_run, WorkflowRun)


def test_download_evidence_file(onfido_api, workflow_run):
    file = onfido_api.download_signed_evidence_file(workflow_run.id)

    assert len(file) > 0
    assert file[:4] == b"%PDF"
