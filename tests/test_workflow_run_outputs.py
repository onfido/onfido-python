import pytest

from onfido import (
    ApplicantBuilder,
    CompleteTaskBuilder,
    CompleteTaskDataBuilder,
    CountryCodes,
    LocationBuilder,
    WorkflowRunBuilder,
)
from tests.conftest import (
    create_applicant,
    create_workflow_run,
    upload_document,
    upload_live_photo,
    repeat_request_until_status_changes,
)


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    applicant_builder = ApplicantBuilder(
        first_name="First",
        last_name="Last",
        location=LocationBuilder(
            ip_address="127.0.0.1", country_of_residence=CountryCodes.ITA
        ),
    )
    return create_applicant(onfido_api, applicant_builder=applicant_builder).id


@pytest.fixture(scope="function")
def document_id(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id).id


@pytest.fixture(scope="function")
def live_photo_id(onfido_api, applicant_id):
    return upload_live_photo(onfido_api, applicant_id).id


@pytest.fixture
def profile_data():
    return {
        "country_residence": "GBR",
        "first_name": "First",
        "last_name": "Last",
        "dob": "2000-01-01",
        "email": "first.last@gmail.com",
        "phone_number": "+351911111111",
        "nationality": "GBR",
        "phone_number_consent_granted": True,
        "address": {
            "country": "GBR",
            "line1": "123rd Street",
            "line2": "2nd Floor",
            "line3": "23",
            "town": "London",
            "postcode": "S2 2DF",
        },
    }


def test_profile_data_as_output(onfido_api, applicant_id, profile_data):
    workflow_id = "d27e510b-27a8-44c3-a3cc-bf4c0648a4ba"
    workflow_run_builder = WorkflowRunBuilder(
        applicant_id=applicant_id, workflow_id=workflow_id
    )
    workflow_run_id = create_workflow_run(
        onfido_api, workflow_run_builder=workflow_run_builder
    ).id

    tasks = onfido_api.list_tasks(workflow_run_id)
    profile_data_task_id = list(filter(lambda task: "profile" in task.id, tasks))[0].id

    complete_task_builder = CompleteTaskBuilder(
        data=CompleteTaskDataBuilder(profile_data)
    )

    onfido_api.complete_task(
        workflow_run_id=workflow_run_id,
        task_id=profile_data_task_id,
        complete_task_builder=complete_task_builder,
    )

    repeat_request_until_status_changes(
        onfido_api.find_workflow_run, [workflow_run_id], "approved"
    )
    workflow_run_outputs = onfido_api.find_workflow_run(workflow_run_id).output

    assert workflow_run_outputs["profile_capture_data"] == profile_data


def test_document_and_facial_similarity_report_as_output(
    onfido_api, applicant_id, document_id, live_photo_id
):
    workflow_id = "5025d9fd-7842-4805-bce1-a7bfd7131b4e"
    workflow_run_builder = WorkflowRunBuilder(
        applicant_id=applicant_id, workflow_id=workflow_id
    )
    workflow_run_id = create_workflow_run(
        onfido_api, workflow_run_builder=workflow_run_builder
    ).id

    tasks = onfido_api.list_tasks(workflow_run_id)
    profile_data_task_id = list(filter(lambda task: "profile" in task.id, tasks))[0].id

    complete_task_builder = CompleteTaskBuilder(
        data=CompleteTaskDataBuilder({"first_name": "Jane", "last_name": "Doe"})
    )
    onfido_api.complete_task(
        workflow_run_id=workflow_run_id,
        task_id=profile_data_task_id,
        complete_task_builder=complete_task_builder,
    )

    tasks = onfido_api.list_tasks(workflow_run_id)
    document_capture_task_id = list(
        filter(lambda task: "document_photo" in task.id, tasks)
    )[0].id

    complete_document_capture_task_builder = CompleteTaskBuilder(
        data=CompleteTaskDataBuilder([{"id": document_id}])
    )
    onfido_api.complete_task(
        workflow_run_id=workflow_run_id,
        task_id=document_capture_task_id,
        complete_task_builder=complete_document_capture_task_builder,
    )

    tasks = onfido_api.list_tasks(workflow_run_id)
    live_photo_capture_task_id = list(
        filter(lambda task: "face_photo" in task.id, tasks)
    )[0].id
    complete_live_photo_capture_task_request = CompleteTaskBuilder(
        data=CompleteTaskDataBuilder([{"id": live_photo_id}])
    )
    onfido_api.complete_task(
        workflow_run_id=workflow_run_id,
        task_id=live_photo_capture_task_id,
        complete_task_builder=complete_live_photo_capture_task_request,
    )

    repeat_request_until_status_changes(
        onfido_api.find_workflow_run, [workflow_run_id], "approved"
    )
    workflow_run_outputs = onfido_api.find_workflow_run(workflow_run_id).output
    document_report_output = workflow_run_outputs["doc"]
    facial_similarity_report_output = workflow_run_outputs["selfie"]

    assert document_report_output["breakdown"] is not None
    assert document_report_output["properties"] is not None
    assert document_report_output["repeat_attempts"] is not None
    assert document_report_output["result"] is not None
    assert document_report_output["status"] is not None
    assert document_report_output["sub_result"] is not None
    assert document_report_output["uuid"] is not None

    assert facial_similarity_report_output["breakdown"] is not None
    assert facial_similarity_report_output["properties"] is not None
    assert facial_similarity_report_output["result"] is not None
    assert facial_similarity_report_output["status"] is not None
    assert facial_similarity_report_output["uuid"] is not None
