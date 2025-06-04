import onfido
import pytest
from os import environ
from time import sleep


@pytest.fixture(scope="session")
def onfido_api():
    configuration = onfido.Configuration(
        api_token=environ["ONFIDO_API_TOKEN"],
        region=onfido.configuration.Region.EU,
    )
    configuration.debug = True

    with onfido.ApiClient(configuration) as api_client:
        yield onfido.DefaultApi(api_client)


@pytest.fixture(scope="session", autouse=True)
def data_clean_up(onfido_api):
    sample_applicant_id = environ["ONFIDO_SAMPLE_APPLICANT_ID"]

    applicants = onfido_api.list_applicants(
        page=1, per_page=100, include_deleted=False
    ).applicants
    for applicant in applicants:
        if applicant.id != sample_applicant_id:
            try:
                onfido_api.delete_applicant(applicant.id)
            except onfido.ApiException:
                # Just ignore any failure during cleanup
                pass


@pytest.fixture(scope="session", autouse=True)
def webhook_clean_up(onfido_api):
    webhooks = onfido_api.list_webhooks().webhooks
    for webhook in webhooks:
        try:
            onfido_api.delete_webhook(webhook.id)
        except onfido.ApiException:
            # Just ignore any failure during cleanup
            pass


def create_applicant(onfido_api, applicant_builder=None):
    if applicant_builder is None:
        return onfido_api.create_applicant(
            onfido.ApplicantBuilder(
                first_name="First",
                last_name="Last",
                email="first.last@gmail.com",
                phone_number="351911111111",
            )
        )

    return onfido_api.create_applicant(applicant_builder)


def upload_document(onfido_api, applicant_id, file_path="tests/media/sample_driving_licence.png"):
    return onfido_api.upload_document(
        applicant_id=applicant_id,
        type=onfido.DocumentTypes.PASSPORT,
        side="front",
        file=file_path,
    )


def upload_live_photo(onfido_api, applicant_id):
    return onfido_api.upload_live_photo(
        applicant_id=applicant_id,
        file="tests/media/sample_photo.png",
    )


def upload_id_photo(onfido_api, applicant_id):
    return onfido_api.upload_id_photo(
        applicant_id=applicant_id,
        file="tests/media/sample_photo.png",
    )


def create_check(
    onfido_api,
    check_builder=None,
    applicant_id=None,
    document_ids=None,
    report_names=None,
    report_configuration=None
):
    if check_builder is None:
        return onfido_api.create_check(
            onfido.CheckBuilder(
                applicant_id=applicant_id,
                document_ids=document_ids,
                report_names=report_names,
                privacy_notices_read_consent_given=True,
                report_configuration=report_configuration,
            )
        )

    return onfido_api.create_check(check_builder)


def create_workflow_run(
    onfido_api, workflow_run_builder=None, applicant_id=None, workflow_id=None
):
    if workflow_run_builder is None:
        return onfido_api.create_workflow_run(
            onfido.WorkflowRunBuilder(
                applicant_id=applicant_id, workflow_id=workflow_id
            )
        )

    return onfido_api.create_workflow_run(workflow_run_builder)


def repeat_request_until_status_changes(
    function, params, status, max_retries=15, sleep_time=1
):
    instance = function(*params)

    is_instance_of_report = isinstance(instance, onfido.Report)
    if is_instance_of_report:
        instance = instance.actual_instance

    iteration = 0
    while instance.status != status:
        if iteration > max_retries:
            pytest.fail("Status did not change in time")

        iteration += 1
        sleep(sleep_time)
        if is_instance_of_report:
            instance = function(*params).actual_instance
        else:
            instance = function(*params)

    return instance


def repeat_request_until_task_output_changes(
    function, params, max_retries=15, sleep_time=1
):
    instance = function(*params)

    iteration = 0
    while instance.output is None:
        if iteration > max_retries:
            pytest.fail("Task output did not change in time")

        iteration += 1
        sleep(sleep_time)

        instance = function(*params)

    return instance


def repeat_request_until_http_code_changes(
    function, params, max_retries=15, sleep_time=1
):
    iteration = 0
    while iteration <= max_retries:
        try:
            instance = function(*params)
            break
        except onfido.ApiException:
            sleep(sleep_time)
            iteration += 1
    return instance
