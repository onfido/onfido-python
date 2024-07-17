import pytest

from onfido import WorkflowRunBuilder

from tests.conftest import (
    create_applicant,
    create_workflow_run,
    repeat_request_until_task_output_changes,
)


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function")
def workflow_id():
    return "8b74614f-9e7f-42fd-852a-5f2bcc852587"


@pytest.fixture(scope="function")
def workflow_run(onfido_api, applicant_id, workflow_id):
    workflow_run_builder = WorkflowRunBuilder(
        applicant_id=applicant_id,
        workflow_id=workflow_id,
        custom_data={
            "country_of_operation": "GBR",
            "document_date_of_expiry": "2022-01-01",
            "document_issuing_country": "FRA",
            "document_issuing_date": "2022-01-01",
            "document_number": "Example string",
            "document_to_sign_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
            "document_type": "driving_licence",
        },
    )
    return create_workflow_run(
        onfido_api, workflow_run_builder=workflow_run_builder
    )


@pytest.fixture(scope="function")
def file_id(onfido_api, workflow_run):
    
    task = onfido_api.list_tasks(workflow_run.id)[0]

    output = repeat_request_until_task_output_changes(
        onfido_api.find_task, [workflow_run.id, task.id], max_retries=10, sleep_time=3
    ).output

    return output["properties"]["signed_documents"][0]["id"]


def test_documents(onfido_api, workflow_run, file_id):
    file = onfido_api.download_qes_document(workflow_run.id, file_id)

    assert len(file) > 0
    assert file[:4] == b"%PDF"
