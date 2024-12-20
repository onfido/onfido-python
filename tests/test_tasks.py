import pytest

from onfido import Task, TaskItem, CompleteTaskBuilder, CompleteTaskDataBuilder
from tests.conftest import create_applicant, create_workflow_run, upload_document


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function")
def workflow_id():
    return "5025d9fd-7842-4805-bce1-a7bfd7131b4e"

@pytest.fixture(scope="function")
def document_id(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id).id

@pytest.fixture(scope="function")
def workflow_run_id(onfido_api, applicant_id, workflow_id):
    return create_workflow_run(
        onfido_api, applicant_id=applicant_id, workflow_id=workflow_id
    ).id


def test_list_tasks(onfido_api, workflow_run_id):
    tasks = onfido_api.list_tasks(workflow_run_id)

    assert tasks is not None
    assert isinstance(tasks[0], TaskItem)
    assert len(tasks) == 2


def test_find_task(onfido_api, workflow_run_id):
    task = onfido_api.list_tasks(workflow_run_id)[0]
    get_task = onfido_api.find_task(workflow_run_id, task.id)

    assert get_task is not None
    assert isinstance(get_task, Task)
    assert get_task.id == task.id
    assert get_task.task_def_id == task.task_def_id


def test_complete_task(onfido_api, workflow_run_id, document_id):
    profile_data_task_id = next(
        filter(lambda task: "profile" in task.id,
               onfido_api.list_tasks(workflow_run_id))).id

    complete_task_builder = CompleteTaskBuilder(
        data=CompleteTaskDataBuilder({"first_name": "Jane", "last_name": "Doe"})
    )

    onfido_api.complete_task(
        workflow_run_id=workflow_run_id,
        task_id=profile_data_task_id,
        complete_task_builder=complete_task_builder,
    )

    profile_task_outputs = onfido_api.find_task(workflow_run_id,
                                                profile_data_task_id).output

    assert profile_task_outputs["first_name"] == "Jane"
    assert profile_task_outputs["last_name"] == "Doe"

    document_capture_task_id = next(
        filter(lambda task: "document_photo" in task.id,
               onfido_api.list_tasks(workflow_run_id))
    ).id

    complete_document_capture_task_builder = CompleteTaskBuilder(
        data=CompleteTaskDataBuilder([{"id": document_id}])
    )

    onfido_api.complete_task(
        workflow_run_id=workflow_run_id,
        task_id=document_capture_task_id,
        complete_task_builder=complete_document_capture_task_builder,
    )

    document_photo_task_id = next(
        filter(lambda task: "document_photo" in task.id,
               onfido_api.list_tasks(workflow_run_id))).id

    document_photo_task_outputs = onfido_api.find_task(
        workflow_run_id,
        document_photo_task_id).output

    assert document_photo_task_outputs == [{"id": document_id,
                                            "type": "document"}]
