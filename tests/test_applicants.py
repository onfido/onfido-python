import onfido
import datetime


def test_create_applicant(onfido_api):
    applicant = onfido_api.create_applicant(
        onfido.ApplicantBuilder(
            first_name='Test',
            last_name='Applicant',
            dob=datetime.date(1980, 1, 22),
            location=onfido.LocationBuilder(
                ip_address='127.0.0.1',
                country_of_residence=onfido.CountryCodes.ITA
            ),
            address=onfido.AddressBuilder(
                building_number='100',
                street='Main Street',
                town='London',
                postcode='SW4 6EH',
                country=onfido.CountryCodes.FRA,
                line1='My wonderful address')
            )
        )

    assert applicant.first_name == 'Test'
    assert applicant.last_name == 'Applicant'
    assert applicant.dob == datetime.date(1980, 1, 22)

    assert applicant.location.ip_address == '127.0.0.1'
    assert applicant.location.country_of_residence == 'ITA'

    assert applicant.address.to_dict() == {
      'building_number': '100',
      'street': 'Main Street',
      'town': 'London',
      'postcode': 'SW4 6EH',
      'country': onfido.CountryCodes.FRA,
      'line1': 'My wonderful address',
      'line2': None,
      'line3': None
    }
