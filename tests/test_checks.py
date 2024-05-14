import pytest
from onfido import Check, ChecksList, ReportName, CheckBuilder, UsDrivingLicenceBuilder
from tests.conftest import create_applicant, create_check, upload_document


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function")
def document_id(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id).id


@pytest.fixture(scope="function", autouse=True)
def check(onfido_api, applicant_id, document_id):
    return create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT, ReportName.IDENTITY_ENHANCED],
    )


def test_create_check(check, applicant_id):
    assert check is not None
    assert isinstance(check, Check)
    assert check.applicant_id == applicant_id
    assert len(check.report_ids) == 2
    assert check.status == "in_progress"


def test_create_consider_check(onfido_api, applicant_id, document_id):
    check_builder = CheckBuilder(
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT],
        consider=[ReportName.DOCUMENT],
    )
    check = create_check(onfido_api, check_builder=check_builder)

    assert check is not None
    assert isinstance(check, Check)
    assert check.applicant_id == applicant_id


def test_create_driving_licence_check(onfido_api, applicant_id, document_id):
    us_driving_licence_builder = UsDrivingLicenceBuilder(id_number="12345", issue_state="GA")

    check_builder = CheckBuilder(
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT],
        us_driving_licence=us_driving_licence_builder,
    )
    check = create_check(onfido_api, check_builder=check_builder)

    assert check is not None
    assert isinstance(check, Check)
    assert check.applicant_id == applicant_id


def test_list_checks(onfido_api, applicant_id):
    checks = onfido_api.list_checks(applicant_id)

    assert checks is not None
    assert isinstance(checks, ChecksList)
    assert len(checks.checks) > 0


def test_retrieve_check(onfido_api, check):
    get_check = onfido_api.find_check(check.id)

    assert get_check.id == check.id
    assert isinstance(get_check, Check)


def test_restart_check(onfido_api, check):
    onfido_api.resume_check(check.id)


def test_download_check(onfido_api, check):
    file = onfido_api.download_check(check.id)

    assert len(file) > 0
