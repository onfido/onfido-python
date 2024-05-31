import pytest

from onfido import ApiException, Document, DocumentsList
from tests.conftest import create_applicant, upload_document


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function", autouse=True)
def document(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id)


def test_create_document(applicant_id, document):
    assert document is not None
    assert document.applicant_id == applicant_id
    assert document.type == "passport"
    assert document.side == "front"
    assert isinstance(document, Document)


def test_list_documents(onfido_api, applicant_id):
    documents = onfido_api.list_documents(applicant_id)

    assert documents is not None
    assert isinstance(documents, DocumentsList)
    assert len(documents.documents) > 0


def test_retrieve_document(onfido_api, document):
    get_document = onfido_api.find_document(document.id)

    assert get_document.id == document.id
    assert isinstance(get_document, Document)


def test_download_document(onfido_api, document):
    file = onfido_api.download_document(document.id)

    assert len(file) > 0


def test_download_inexistent_document(onfido_api):
    inexistent_document_id = "00000000-0000-0000-0000-000000000000"

    with pytest.raises(ApiException):
        onfido_api.download_document(inexistent_document_id)
