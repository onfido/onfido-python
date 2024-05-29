import pytest

from onfido import TimelineFileReference, WorkflowRun, WorkflowRunBuilder
from tests.conftest import (
    create_applicant,
    create_workflow_run,
    repeat_request_until_http_code_changes,
    repeat_request_until_status_changes,
)


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
        custom_data={"age": 18, "is_employed": False},
    )
    workflow_run = create_workflow_run(
        onfido_api, workflow_run_builder=workflow_run_builder
    )
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


def test_generate_timeline_file(onfido_api, applicant_id):
    workflow_id = "221f9d24-cf72-4762-ac4a-01bf3ccc09dd"
    workflow_run_id = create_workflow_run(
        onfido_api, applicant_id=applicant_id, workflow_id=workflow_id
    ).id
    repeat_request_until_status_changes(
        onfido_api.find_workflow_run, [workflow_run_id], "approved"
    )

    workflow_timeline_file_data = onfido_api.create_timeline_file(workflow_run_id)

    assert isinstance(workflow_timeline_file_data, TimelineFileReference)
    assert workflow_timeline_file_data.workflow_timeline_file_id is not None
    assert workflow_timeline_file_data.href is not None


def test_find_timeline_file(onfido_api, applicant_id):
    workflow_id = "221f9d24-cf72-4762-ac4a-01bf3ccc09dd"
    workflow_run_id = create_workflow_run(
        onfido_api, applicant_id=applicant_id, workflow_id=workflow_id
    ).id
    repeat_request_until_status_changes(
        onfido_api.find_workflow_run, [workflow_run_id], "approved"
    )

    timeline_file_id = onfido_api.create_timeline_file(
        workflow_run_id
    ).workflow_timeline_file_id
    file = repeat_request_until_http_code_changes(
        onfido_api.find_timeline_file, [workflow_run_id, timeline_file_id]
    )

    assert len(file) > 0
