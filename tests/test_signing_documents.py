import pytest
from pydantic import ValidationError

from onfido import ApiException, SigningDocument, SigningDocumentsList
from tests.conftest import create_applicant, upload_signing_document

INEXISTENT_SIGNING_DOCUMENT_ID = "00000000-0000-0000-0000-000000000000"


@pytest.fixture(scope="function")
def applicant(onfido_api):
    return create_applicant(onfido_api)


@pytest.fixture(scope="function")
def signing_document(onfido_api, applicant):
    return upload_signing_document(onfido_api, applicant.id)


def test_upload_signing_document(signing_document, applicant):
    assert isinstance(signing_document, SigningDocument)
    assert signing_document.file_name == "sample_signing_document.pdf"
    assert signing_document.file_type == "pdf"
    assert signing_document.applicant_id == applicant.id
    assert signing_document.href is not None
    assert signing_document.download_href is not None
    assert signing_document.file_size is not None and signing_document.file_size > 0
    assert signing_document.model_dump_json(by_alias=True, exclude_none=True) is not None


def test_download_signing_document(onfido_api, signing_document):
    file_contents = onfido_api.download_signing_document(signing_document.id)

    assert len(file_contents) > 0
    assert bytes(file_contents[:4]) == b"%PDF"


def test_find_signing_document(onfido_api, signing_document, applicant):
    found = onfido_api.find_signing_document(signing_document.id)

    assert isinstance(found, SigningDocument)
    assert found.id == signing_document.id
    assert found.file_name == "sample_signing_document.pdf"
    assert found.file_type == "pdf"
    assert found.applicant_id == applicant.id
    assert found.download_href is not None
    assert found.model_dump_json(by_alias=True, exclude_none=True) is not None


def test_list_signing_documents(onfido_api, applicant, signing_document):
    documents = onfido_api.list_signing_documents(applicant.id)

    assert documents is not None
    assert isinstance(documents, SigningDocumentsList)
    assert any(doc.id == signing_document.id for doc in documents.signing_documents)


def test_upload_signing_document_with_null_params(onfido_api):
    with pytest.raises(ValidationError):
        onfido_api.upload_signing_document(None, None)


def test_download_inexistent_signing_document(onfido_api):
    with pytest.raises(ApiException):
        onfido_api.download_signing_document(INEXISTENT_SIGNING_DOCUMENT_ID)
