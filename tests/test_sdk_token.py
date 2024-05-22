import pytest

from onfido import SdkToken, SdkTokenBuilder
from tests.conftest import create_applicant


@pytest.fixture
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


def test_generate_sdk_token(onfido_api, applicant_id):
    token = onfido_api.generate_sdk_token(
        SdkTokenBuilder(
            applicant_id=applicant_id,
            referrer="https://*.example.com/example_page/*",
        )
    )

    assert isinstance(token, SdkToken)
    assert len(token.token) > 0
