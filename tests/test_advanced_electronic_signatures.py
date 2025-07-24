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
    return "9554c27e-9886-4052-992d-816467d97d24"


@pytest.fixture(scope="function")
def workflow_run(onfido_api, applicant_id, workflow_id):
    workflow_run_builder = WorkflowRunBuilder(
        applicant_id=applicant_id,
        workflow_id=workflow_id,
        custom_data={
            "doc_result": "clear",
            "face_result": "clear",
            "transaction_id": "995bf84c-d708-4977-8b88-d4b66bebdaf6",
        },
    )
    return create_workflow_run(
        onfido_api, workflow_run_builder=workflow_run_builder
    )


@pytest.fixture(scope="function")
def task_output(onfido_api, workflow_run):
    task = onfido_api.list_tasks(workflow_run.id)[1]

    output = repeat_request_until_task_output_changes(
        onfido_api.find_task, [workflow_run.id, task.id], max_retries=10, sleep_time=3
    ).output

    return output


def get_signed_document_id(task_output):
    return task_output["properties"]["signed_documents"][0]["id"]


def get_transaction_receipt_id(task_output):
    return task_output["properties"]["receipt_document"]["id"]


def test_aes_documents(onfido_api, workflow_run, task_output):
    """Test Advanced Electronic Signature (AES) document download"""
    signed_document_id = get_signed_document_id(task_output)
    transaction_receipt_id = get_transaction_receipt_id(task_output)

    # Test signed document download
    signed_document = onfido_api.download_aes_document(workflow_run.id, signed_document_id)
    assert len(signed_document) > 0
    assert signed_document[:4] == b"%PDF"

    # Test transaction receipt download
    receipt_document = onfido_api.download_aes_document(workflow_run.id, transaction_receipt_id)
    assert len(receipt_document) > 0
    assert receipt_document[:4] == b"%PDF"
