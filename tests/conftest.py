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
