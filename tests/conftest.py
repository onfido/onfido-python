import onfido
from os import environ
import pytest


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
            except onfido.ApiException as e:
                # Just ignore any failure during cleanup
                pass


def create_applicant(onfido_api, applicant_builder=None):
    if applicant_builder is None:
        return onfido_api.create_applicant(
            onfido.ApplicantBuilder(first_name="First", last_name="Last")
        )

    return onfido_api.create_applicant(applicant_builder)


def upload_document(onfido_api, applicant_id):
    return onfido_api.upload_document(
        applicant_id=applicant_id,
        type="passport",
        side="front",
        file="tests/media/sample_driving_licence.png",
    )


def upload_live_photo(onfido_api, applicant_id):
    return onfido_api.upload_live_photo(
        applicant_id=applicant_id,
        file="tests/media/sample_photo.png",
    )


def create_check(
    onfido_api,
    check_builder=None,
    applicant_id=None,
    document_ids=None,
    report_names=None,
):
    if check_builder is None:
        return onfido_api.create_check(
            onfido.CheckBuilder(
                applicant_id=applicant_id,
                document_ids=document_ids,
                report_names=report_names,
            )
        )

    return onfido_api.create_check(check_builder)
