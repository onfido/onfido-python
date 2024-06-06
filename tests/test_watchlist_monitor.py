from datetime import datetime

import pytest

from onfido import ApplicantBuilder, ReportName, WatchlistMonitorBuilder
from tests.conftest import create_applicant


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    applicant_builder = ApplicantBuilder(
        first_name="John",
        last_name="Smith",
        dob=datetime(year=1990, month=1, day=1),
    )
    return create_applicant(onfido_api, applicant_builder=applicant_builder).id


@pytest.fixture(scope="function")
def watchlist_monitor(onfido_api, applicant_id):
    return onfido_api.create_watchlist_monitor(
        WatchlistMonitorBuilder(
            applicant_id=applicant_id, report_name=ReportName.WATCHLIST_STANDARD
        )
    )


def test_create_watchlist_standard_monitor(onfido_api, applicant_id, watchlist_monitor):
    assert watchlist_monitor.applicant_id == applicant_id
    assert watchlist_monitor.report_name == ReportName.WATCHLIST_STANDARD


def test_create_watchlist_aml_monitor(onfido_api, applicant_id):
    watchlist_monitor = onfido_api.create_watchlist_monitor(
        WatchlistMonitorBuilder(
            applicant_id=applicant_id, report_name=ReportName.WATCHLIST_AML
        )
    )

    assert watchlist_monitor.applicant_id == applicant_id
    assert watchlist_monitor.report_name == ReportName.WATCHLIST_AML


def test_list_watchlist_monitors(onfido_api, applicant_id, watchlist_monitor):
    list_of_monitors = onfido_api.list_watchlist_monitors(
        applicant_id, include_deleted=False
    ).monitors

    assert len(list_of_monitors) > 0


def test_find_watchlist_monitor(onfido_api, watchlist_monitor):
    get_watchlist_monitor = onfido_api.find_watchlist_monitor(watchlist_monitor.id)

    assert get_watchlist_monitor.id == watchlist_monitor.id


def test_delete_watchlist_monitor(onfido_api, watchlist_monitor):
    onfido_api.delete_watchlist_monitor(watchlist_monitor.id)


def test_list_watchlist_monitor_matches(onfido_api, watchlist_monitor):
    matches_list = onfido_api.list_watchlist_monitor_matches(
        watchlist_monitor.id
    ).matches

    assert len(matches_list) == 0


def test_force_report_creation(onfido_api, applicant_id, watchlist_monitor):
    onfido_api.force_report_creation_from_watchlist_monitor(watchlist_monitor.id)

    checks = onfido_api.list_checks(applicant_id=applicant_id).checks
    assert len(checks) == 2
