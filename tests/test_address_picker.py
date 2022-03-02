import onfido
from onfido.regions import Region


api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)


def test_address_picker(requests_mock):
    mock_create = requests_mock.get("https://api.eu.onfido.com/v3.3/addresses/pick?postcode=SW46EH", json=[])
    api.address.pick("SW46EH")
    assert mock_create.called is True

