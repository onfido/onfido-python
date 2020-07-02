import onfido
import pytest

api = onfido.Api("<AN_API_TOKEN>")

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"
fake_uuid2 = "a63c28a2-5e58-4f7d-bfe8-4b5fe5214c55"


def test_generate_sdk_token(requests_mock):
    mock_generate = requests_mock.post("https://api.onfido.com/v3/sdk_token", json=[])

    request_body = {"applicant_id": fake_uuid,
                    "application_id": fake_uuid2}

    api.sdk_token.generate(request_body)
    assert mock_generate.called is True

