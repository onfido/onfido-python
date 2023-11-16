import aiofiles
import onfido
from onfido.exceptions import OnfidoRequestError
from onfido.regions import Region
import pytest
import io
import asyncio
import aiohttp
from aioresponses import aioresponses

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_upload_document(requests_mock):
    mock_upload = requests_mock.post("https://api.eu.onfido.com/v3.6/documents/", json=[])

    request_body = {"applicant_id": fake_uuid,
                    "type": "driving_licence",
                    "location": {
                      "ip_address": "127.0.0.1",
                      "country_of_residence": "GBR"
                      },
                    "validate_image_quality": True
                    }

    sample_file = open("sample_driving_licence.png", "rb")

    api.document.upload(sample_file, request_body)

    assert mock_upload.called is True

@pytest.mark.asyncio
async def test_async_upload_document(m):
    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession() as session:
        async_api = onfido.AsyncApi("<AN_API_TOKEN>", region=Region.EU, aio_session=session)
        request_body = {"applicant_id": fake_uuid,
                        "type": "driving_licence",
                        "location": {
                        "ip_address": "127.0.0.1",
                        "country_of_residence": "GBR"
                        },
                        "validate_image_quality": True
                        }

        m.post("https://api.eu.onfido.com/v3.6/documents/", payload=request_body)

        async with aiofiles.open("sample_driving_licence.png", "rb") as sample_file:
            await async_api.document.upload(sample_file, request_body)

        m.assert_called_once()

def test_upload_document_validation_error(requests_mock):
    mock_upload = requests_mock.post(
        "https://api.eu.onfido.com/v3.6/documents/",
        json={
            "error": {
                "type": "validation_error",
                "message": "There was a validation error on this request",
                "fields": {
                    "document_detection": [
                        "no document in image"
                    ]
                },
            }
        },
        headers={ 'Content-Type': 'application/json' },
        status_code=422
    )

    sample_file = open("sample_driving_licence.png", "rb")
    request_body = {"applicant_id": fake_uuid,
                    "type": "driving_licence",
                    "validate_image_quality": True}

    with pytest.raises(OnfidoRequestError) as error:
        api.document.upload(sample_file, request_body)

    assert mock_upload.called is True
    assert error.value.args[0]['fields']['document_detection']

def test_upload_document_missing_params():
    string_io = io.StringIO("Data to be uploaded")

    with pytest.raises(TypeError):
        api.document.upload(sample_file=string_io)

def test_find_document(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.6/documents/{fake_uuid}", json=[])
    api.document.find(fake_uuid)
    assert mock_find.called is True

def test_list_documents(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.6/documents?applicant_id={fake_uuid}", json=[])
    api.document.all(fake_uuid)
    assert mock_list.called is True

def test_download_document(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.6/documents/{fake_uuid}/download", text="FAKE IMAGE BINARY", headers={"Content-type": "image/png"})
    onfido_download = api.document.download(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "image/png"
