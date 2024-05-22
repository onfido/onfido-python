import pytest

from datetime import date
from onfido import Extraction, ExtractRequest, DocumentTypes, CountryCodes
from tests.conftest import create_applicant, upload_document


@pytest.fixture
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture
def document_id(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id).id


def test_perform_extraction(onfido_api, document_id):
    extraction = onfido_api.extract(ExtractRequest(document_id=document_id))

    assert extraction is not None
    assert isinstance(extraction, Extraction)
    assert extraction.document_id == document_id

    document_classification = extraction.document_classification
    extracted_data = extraction.extracted_data

    # Check response body: document classification
    assert document_classification is not None
    assert document_classification.document_type == DocumentTypes.DRIVING_LICENCE
    assert document_classification.issuing_country == CountryCodes.GBR

    # Check response body: extracted data
    assert extracted_data is not None
    assert extracted_data.date_of_birth == date(1976, 3, 11)
    assert extracted_data.date_of_expiry == date(2031, 5, 28)
    assert extracted_data.document_number == "200407512345"
    assert extracted_data.first_name == "SARAH"
    assert extracted_data.last_name == "MORGAN"
    assert extracted_data.gender == "Female"
