from onfido.models.address import Address
from copy import deepcopy

exampleAddress = Address.from_dict({
  'postcode': "S2 2DF",
  'country': "GBR",
  'flat_number': "",
  'building_number': "2",
  'building_name': "",
  'street': "RAWSON CLOSE",
  'sub_street': "",
  'town': "SHEFFIELD"
})

exampleAddress2 = deepcopy(exampleAddress)
exampleAddress2.building_number = "18"


def test_address_picker(onfido_api):
    addresses = onfido_api.find_addresses("S2 2DF").addresses

    assert exampleAddress in addresses
    assert exampleAddress2 in addresses
