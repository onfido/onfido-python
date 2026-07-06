import json
from time import sleep
from uuid import uuid4

import pytest

from onfido import (
    ApiException,
    ApplicantBuilder,
    ApplicantConsentBuilder,
    ApplicantConsentName,
    BiometricTokenUpdater,
    WorkflowRunBuilder,
)
from tests.conftest import create_applicant, upload_live_photo


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    applicant = create_applicant(
        onfido_api,
        ApplicantBuilder(
            first_name="First",
            last_name="Last",
            email="first.last@gmail.com",
            consents=[
                ApplicantConsentBuilder(
                    name=ApplicantConsentName.PRIVACY_NOTICES_READ,
                    granted=True,
                )
            ],
        ),
    )
    return applicant.id


@pytest.fixture(scope="function")
def biometric_workflow_id():
    return "b79dcf69-41a0-412d-b803-d1a618730f72"


@pytest.fixture(scope="function")
def biometric_customer_user_id():
    return f"test-user-id-{uuid4()}"


@pytest.fixture(scope="function", autouse=True)
def live_photo(onfido_api, applicant_id):
    return upload_live_photo(onfido_api, applicant_id)


@pytest.fixture(scope="function")
def create_biometric_token(
    onfido_api,
    applicant_id,
    biometric_workflow_id,
    biometric_customer_user_id,
    live_photo,
):
    workflow_run = onfido_api.create_workflow_run(
        WorkflowRunBuilder(
            applicant_id=applicant_id,
            workflow_id=biometric_workflow_id,
            customer_user_id=biometric_customer_user_id,
            custom_data={
                "media_ids": [
                    {
                        "id": str(live_photo.id),
                    }
                ]
            },
        )
    )

    assert workflow_run.customer_user_id == biometric_customer_user_id

    max_retries = 3

    # Wait for the biometric token to be created
    for _ in range(max_retries + 1):
        biometric_tokens = onfido_api.list_biometric_tokens(
            biometric_customer_user_id
        )
        if biometric_tokens.biometric_tokens:
            return biometric_tokens
        sleep(2)

    pytest.fail("Biometric tokens were not created in time")


@pytest.fixture(scope="function")
def biometric_token(create_biometric_token):
    return create_biometric_token.biometric_tokens[0]


@pytest.fixture(scope="function")
def biometric_token_id(biometric_token):
    token_uuid = biometric_token.uuid
    if token_uuid is None:
        pytest.fail("Biometric token response did not include a uuid")

    return token_uuid


def test_list_biometric_tokens(create_biometric_token):
    assert len(create_biometric_token.biometric_tokens) > 0
    assert create_biometric_token.biometric_tokens[0].uuid is not None
    assert create_biometric_token.biometric_tokens[0].data.status is not None


def test_find_biometric_token(onfido_api, biometric_customer_user_id, biometric_token_id):
    biometric_token_response = onfido_api.find_biometric_token(
        biometric_customer_user_id,
        biometric_token_id,
    )

    assert biometric_token_response.biometric_token.uuid == biometric_token_id
    assert biometric_token_response.biometric_token.data.status is not None


def test_update_biometric_token_status(onfido_api, biometric_customer_user_id, biometric_token_id):
    updated_biometric_token = onfido_api.update_biometric_token(
        biometric_customer_user_id,
        biometric_token_id,
        BiometricTokenUpdater(status="approved"),
    )

    assert updated_biometric_token.biometric_token.uuid == biometric_token_id
    assert updated_biometric_token.biometric_token.data.status == "approved"


def test_invalidate_biometric_token_success(onfido_api, biometric_customer_user_id, biometric_token_id):
    response = onfido_api.invalidate_biometric_token_without_preload_content(
        biometric_customer_user_id,
        biometric_token_id,
    )

    assert response.status == 200


def test_invalidate_biometric_token_not_found_when_already_deleted(
    onfido_api,
    biometric_customer_user_id,
    biometric_token_id,
):
    onfido_api.invalidate_biometric_token_without_preload_content(
        biometric_customer_user_id,
        biometric_token_id,
    )

    with pytest.raises(ApiException) as exc_info:
        onfido_api.invalidate_biometric_token(
            biometric_customer_user_id,
            biometric_token_id,
        )

    error_response = json.loads(exc_info.value.body)

    assert exc_info.value.status == 404
    assert error_response["error"]["message"] == "Not found"
    assert error_response["error"]["type"] == "resource_not_found"


def test_invalidate_biometric_tokens_success(
    onfido_api,
    biometric_customer_user_id,
    create_biometric_token,
):
    response = onfido_api.invalidate_biometric_tokens_without_preload_content(
        biometric_customer_user_id
    )

    assert response.status == 200


def test_invalidate_biometric_tokens_not_found_when_already_deleted(
    onfido_api,
    biometric_customer_user_id,
    create_biometric_token,
):
    onfido_api.invalidate_biometric_tokens_without_preload_content(
        biometric_customer_user_id
    )

    with pytest.raises(ApiException) as exc_info:
        onfido_api.invalidate_biometric_tokens(
            biometric_customer_user_id
        )

    error_response = json.loads(exc_info.value.body)

    assert exc_info.value.status == 404
    assert error_response["error"]["message"] == "Not found"
    assert error_response["error"]["type"] == "resource_not_found"
