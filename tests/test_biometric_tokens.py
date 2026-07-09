import json
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
from tests.conftest import create_applicant, repeat_request_until, upload_live_photo


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    unique_suffix = uuid4().hex[:8]
    applicant = create_applicant(
        onfido_api,
        ApplicantBuilder(
            first_name=f"First{unique_suffix}",
            last_name=f"Last{unique_suffix}",
            email=f"first.last.{unique_suffix}@example.com",
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

    biometric_tokens = repeat_request_until(
        onfido_api.list_biometric_tokens,
        [biometric_customer_user_id],
        lambda response: bool(response.biometric_tokens),
        "Biometric tokens were not created in time",
        max_retries=10,
        sleep_time=3,
    )

    return biometric_tokens


@pytest.fixture(scope="function")
def biometric_token_id(create_biometric_token):
    token_uuid = create_biometric_token.biometric_tokens[0].uuid
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
    approved_status = "approved"
    updated_biometric_token = onfido_api.update_biometric_token(
        biometric_customer_user_id,
        biometric_token_id,
        BiometricTokenUpdater(status=approved_status),
    )

    assert updated_biometric_token.biometric_token.uuid == biometric_token_id
    assert updated_biometric_token.biometric_token.data.status == approved_status


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
