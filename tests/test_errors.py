import pytest
from onfido.exceptions import OnfidoRequestError, OnfidoServerError, OnfidoConnectionError, OnfidoTimeoutError, OnfidoUnknownError, error_decorator
import requests
import onfido

api = onfido.Api("<AN_API_TOKEN>")

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


@error_decorator
def raise_status_code(status_code):
    response = requests.Response()
    response.status_code = status_code

    raise requests.HTTPError(response=response)

@error_decorator
def timeout_test():
    raise requests.Timeout

@error_decorator
def connection_error_test():
    raise requests.ConnectionError

@error_decorator
def request_error_test():
    raise requests.RequestException

def test_mocked_status_code(requests_mock):
    response = requests.Response()
    response.status_code = 422

    requests_mock.get(f"https://api.eu.onfido.com/v3.1/applicants/{fake_uuid}", exc=requests.HTTPError(response=response))
    with pytest.raises(OnfidoRequestError):
        api.applicant.find(fake_uuid)

def test_onfido_unknown_error(requests_mock):
    requests_mock.get(f"https://api.eu.onfido.com/v3.1/applicants/{fake_uuid}", text="NOT VALID JSON")

    with pytest.raises(OnfidoUnknownError):
        api.applicant.find(fake_uuid)

def test_errors():
    with pytest.raises(OnfidoTimeoutError):
        timeout_test()

    with pytest.raises(OnfidoConnectionError):
        connection_error_test()

    with pytest.raises(OnfidoUnknownError):
        request_error_test()

    with pytest.raises(OnfidoServerError):
        raise_status_code(500)

    with pytest.raises(OnfidoRequestError):
        raise_status_code(499)

