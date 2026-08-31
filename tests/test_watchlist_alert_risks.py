from datetime import date
from uuid import UUID

import pytest

from onfido import (
    AddressBuilder,
    ApplicantBuilder,
    WatchlistAlertRisk,
    WorkflowRunBuilder,
)
from tests.conftest import (
    create_applicant,
    repeat_request_until_task_output_changes,
)


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    applicant = create_applicant(
        onfido_api,
        ApplicantBuilder(
            first_name="Donald",
            last_name="Consider",
            dob=date(1990, 1, 1),
            address=AddressBuilder(
                country="PRT",
                town="Town",
                street="Street",
                building_number="12",
                postcode="12345",
            ),
        ),
    )
    return applicant.id


@pytest.fixture(scope="function")
def workflow_id():
    return UUID("18effbfe-73c3-4680-ae43-e1c474767ff4")


@pytest.fixture(scope="function")
def workflow_run(onfido_api, applicant_id, workflow_id):
    return onfido_api.create_workflow_run(
        WorkflowRunBuilder(
            applicant_id=applicant_id,
            workflow_id=workflow_id,
            custom_data={
                "national_id": {
                    "type": "passport",
                    "value": "P1234567",
                },
                "nationality": "PRT",
            },
        )
    )


@pytest.fixture(scope="function")
def watchlist_task(onfido_api, workflow_run):
    task = next(
        (
            workflow_task
            for workflow_task in onfido_api.list_tasks(workflow_run.id)
            if workflow_task.task_def_id == "query_watchlists_complyadvantage_mesh"
        ),
        None,
    )

    assert task is not None

    return repeat_request_until_task_output_changes(
        onfido_api.find_task,
        [workflow_run.id, task.id],
        max_retries=30,
        sleep_time=2,
    )


@pytest.fixture(scope="function")
def alert_id(watchlist_task):
    alert_identifier = watchlist_task.output["properties"]["alert_identifier"]

    assert alert_identifier is not None
    return UUID(alert_identifier)


def test_list_watchlist_alert_risks(onfido_api, alert_id):
    risks = onfido_api.list_watchlist_alert_risks(alert_id, page=1, per_page=1)

    assert len(risks) > 0
    assert len(risks) <= 1
    assert isinstance(risks[0], WatchlistAlertRisk)
    assert risks[0].identifier is not None
    assert risks[0].decision is not None
    assert risks[0].detail is not None
