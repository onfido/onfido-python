import pytest

from onfido import Report, ReportName, ReportStatus
from tests.conftest import create_applicant, create_check, upload_document
from typing import List


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function")
def document_id(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id).id


@pytest.fixture(scope="function")
def check(onfido_api, applicant_id, document_id):
    return create_check(
        onfido_api,
        applicant_id=applicant_id,
        document_ids=[document_id],
        report_names=[ReportName.DOCUMENT, ReportName.IDENTITY_ENHANCED],
    )


@pytest.fixture(scope="function")
def sorted_reports(onfido_api, check):
    return sort_reports(onfido_api.list_reports(check.id).reports)


@pytest.fixture(scope="function")
def document_report_id(sorted_reports):
    return sorted_reports[0].actual_instance.id


@pytest.fixture(scope="function")
def identity_report_id(sorted_reports):
    return sorted_reports[1].actual_instance.id


def sort_reports(report_list: List[Report]):
    return sorted(report_list, key=lambda report: report.actual_instance.name)


def test_list_reports(sorted_reports):
    assert isinstance(sorted_reports[0], Report)
    assert sorted_reports[0].actual_instance.name == ReportName.DOCUMENT
    assert sorted_reports[1].actual_instance.name == ReportName.IDENTITY_ENHANCED


def test_find_report(onfido_api, document_report_id, identity_report_id):
    get_document_report = onfido_api.find_report(document_report_id)
    get_identity_report = onfido_api.find_report(identity_report_id)

    assert isinstance(get_document_report, Report)
    assert get_document_report.actual_instance.id == document_report_id
    assert get_document_report.actual_instance.name == ReportName.DOCUMENT
    assert get_document_report.actual_instance.status == ReportStatus.AWAITING_DATA

    assert isinstance(get_identity_report, Report)
    assert get_identity_report.actual_instance.id == identity_report_id
    assert get_identity_report.actual_instance.name == ReportName.IDENTITY_ENHANCED
    assert get_identity_report.actual_instance.status == ReportStatus.COMPLETE
    assert get_identity_report.actual_instance.breakdown.date_of_birth is None
    assert get_identity_report.actual_instance.breakdown.address is None


def test_resume_report(onfido_api, document_report_id):
    onfido_api.resume_report(document_report_id)


def test_cancel_report(onfido_api, document_report_id):
    onfido_api.cancel_report(document_report_id)
