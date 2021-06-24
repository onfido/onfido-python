import onfido
from onfido.regions import Region
import pytest
import io

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_upload_document(requests_mock):
    mock_upload = requests_mock.post("https://api.eu.onfido.com/v3.2/documents/", json=[])

    request_body = {"applicant_id": fake_uuid,
                    "document_type": "driving_licence"}

    sample_file = open("sample_driving_licence.png", "rb")

    api.document.upload(sample_file, request_body)

    assert mock_upload.called is True

def test_upload_document_missing_params():
    string_io = io.StringIO("Data to be uploaded")

    with pytest.raises(TypeError):
        api.document.upload(sample_file=string_io)

def test_find_document(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.2/documents/{fake_uuid}", json=[])
    api.document.find(fake_uuid)
    assert mock_find.called is True

def test_list_documents(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.2/documents?applicant_id={fake_uuid}", json=[])
    api.document.all(fake_uuid)
    assert mock_list.called is True

def test_download_document(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.2/documents/{fake_uuid}/download", text="FAKE IMAGE BINARY", headers={"Content-type": "image/png"})
    onfido_download = api.document.download(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "image/png"
