import pytest

from tests.conftest import (
    create_applicant,
    create_workflow_run,
)


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function")
def workflow_id():
    return "e8c921eb-0495-44fe-b655-bcdcaffdafe5"


@pytest.fixture(scope="function")
def workflow_run(onfido_api, applicant_id, workflow_id):
    return create_workflow_run(
        onfido_api, applicant_id=applicant_id, workflow_id=workflow_id
    )


@pytest.fixture(scope="function")
def file_id():
    return "58813a17-904c-408f-8105-127dc8144b3e"


def test_documents(onfido_api, workflow_run, file_id):
    file = onfido_api.download_qes_document(workflow_run.id, file_id)

    assert len(file) > 0
    assert file[:4] == b"%PDF"
