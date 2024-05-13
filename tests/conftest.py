import onfido
from os import environ
import pytest


@pytest.fixture
def onfido_api():
    configuration = onfido.Configuration(
      api_token=environ['ONFIDO_API_TOKEN'],
      region=onfido.configuration.Region.EU,
    )
    configuration.debug = True

    with onfido.ApiClient(configuration) as api_client:
        yield onfido.DefaultApi(api_client)


def create_applicant(onfido_api, applicant_builder=None):
    if applicant_builder is None:
        return onfido_api.create_applicant(
            onfido.ApplicantBuilder(first_name="First", last_name="Last")
        )

    return onfido_api.create_applicant(applicant_builder)
