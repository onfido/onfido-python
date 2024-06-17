import pytest

from onfido import (
    ApplicantBuilder,
    CountryCodes,
    DocumentReport,
    FacialSimilarityPhotoReport,
    LocationBuilder,
    ReportName,
    ReportStatus,
)
from tests.conftest import (
    create_applicant,
    create_check,
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


def test_schema_of_document_report_is_valid(onfido_api, applicant_id, document_id):
    document_report_id = create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT],
    ).report_ids[0]

    document_report = repeat_request_until_status_changes(
        onfido_api.find_report, [document_report_id], ReportStatus.COMPLETE
    )
    assert isinstance(document_report, DocumentReport)


def test_schema_of_facial_similarity_report_id_valid(
    onfido_api, applicant_id, document_id, live_photo_id
):
    facial_similarity_report_id = create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.FACIAL_SIMILARITY_PHOTO],
    ).report_ids[0]

    facial_similarity_report = repeat_request_until_status_changes(
        onfido_api.find_report, [facial_similarity_report_id], ReportStatus.COMPLETE
    )
    assert isinstance(facial_similarity_report, FacialSimilarityPhotoReport)
    assert facial_similarity_report.properties.score is None
