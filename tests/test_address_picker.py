import onfido

api = onfido.Api("<AN_API_TOKEN>")


def test_address_picker(requests_mock):
    mock_create = requests_mock.get("https://api.eu.onfido.com/v3.1/addresses/pick?postcode=SW46EH", json=[])
    api.address.pick("SW46EH")
    assert mock_create.called is True

