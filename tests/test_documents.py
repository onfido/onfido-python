import pytest

from onfido import ApiException, Document, DocumentsList, DocumentTypes
from tests.conftest import create_applicant, upload_document

INEXISTENT_DOCUMENT_ID = "00000000-0000-0000-0000-000000000000"

@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function", autouse=True)
def document(onfido_api, applicant_id):
    return upload_document(onfido_api, applicant_id)


def test_create_document(applicant_id, document):
    assert document is not None
    assert document.applicant_id == applicant_id
    assert document.type == DocumentTypes.PASSPORT
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
    with pytest.raises(ApiException):
        onfido_api.download_document(INEXISTENT_DOCUMENT_ID)

def test_download_nfc_face(onfido_api, document, applicant_id):
    nfc_face = upload_document(onfido_api, applicant_id, "tests/media/nfc_data.json")

    file = onfido_api.download_nfc_face(nfc_face.id)

    assert len(file) > 0


def test_download_nfc_face_not_found(onfido_api):
    with pytest.raises(ApiException):
        onfido_api.download_nfc_face(INEXISTENT_DOCUMENT_ID)
