import pytest

import onfido
import datetime
from tests.conftest import create_applicant


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


def test_create_applicant(onfido_api):
    applicant_builder = onfido.ApplicantBuilder(
        first_name="Test",
        last_name="Applicant",
        dob=datetime.date(1980, 1, 22),
        location=onfido.LocationBuilder(
            ip_address="127.0.0.1", country_of_residence=onfido.CountryCodes.ITA
        ),
        address=onfido.AddressBuilder(
            building_number="100",
            street="Main Street",
            town="London",
            postcode="SW4 6EH",
            country=onfido.CountryCodes.FRA,
            line1="My wonderful address",
        ),
    )

    applicant = create_applicant(onfido_api, applicant_builder)

    assert isinstance(applicant, onfido.Applicant)
    assert applicant.first_name == "Test"
    assert applicant.last_name == "Applicant"
    assert applicant.dob == datetime.date(1980, 1, 22)

    assert applicant.location.ip_address == "127.0.0.1"
    assert applicant.location.country_of_residence == "ITA"

    assert applicant.address.to_dict() == {
        "building_number": "100",
        "street": "Main Street",
        "town": "London",
        "postcode": "SW4 6EH",
        "country": onfido.CountryCodes.FRA,
        "line1": "My wonderful address",
        "line2": None,
        "line3": None,
    }


def test_list_applicants(onfido_api):
    list_of_applicants = onfido_api.list_applicants()
    assert isinstance(list_of_applicants, onfido.ApplicantsList)
    assert len(list_of_applicants.applicants) > 0


def test_retrieve_applicant(onfido_api, applicant_id):
    applicant = onfido_api.find_applicant(applicant_id)

    assert applicant.id == applicant_id
    assert applicant.first_name == "First"
    assert applicant.last_name == "Last"
    assert isinstance(applicant, onfido.Applicant)


def test_update_applicant(onfido_api, applicant_id):
    new_applicant_data = onfido.ApplicantUpdater(
        first_name="Jane", last_name="Doe", dob=datetime.date(1990, 1, 22)
    )
    onfido_api.update_applicant(applicant_id, new_applicant_data)

    updated_applicant = onfido_api.find_applicant(applicant_id)
    assert isinstance(updated_applicant, onfido.Applicant)
    assert updated_applicant.first_name == "Jane"
    assert updated_applicant.last_name == "Doe"
    assert updated_applicant.dob == datetime.date(1990, 1, 22)


def test_delete_applicant(onfido_api, applicant_id):
    onfido_api.delete_applicant(applicant_id)

    with pytest.raises(onfido.exceptions.ApiException):
        onfido_api.find_applicant(applicant_id)


def test_restore_deleted_applicant(onfido_api, applicant_id):
    onfido_api.delete_applicant(applicant_id)
    onfido_api.restore_applicant(applicant_id)
