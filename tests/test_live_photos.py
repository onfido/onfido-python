import onfido
from onfido.exceptions import OnfidoRequestError
from onfido.regions import Region
import io
import pytest

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_upload_photo(requests_mock):
    mock_upload = requests_mock.post("https://api.eu.onfido.com/v3.6/live_photos/", json=[])

    sample_file = open("sample_photo.png", "rb")
    request_body = {"advanced_validation": "true"}

    api.live_photo.upload(sample_file, request_body)

    assert mock_upload.called is True

def test_upload_live_photo_validation_error(requests_mock):
    mock_upload = requests_mock.post(
        "https://api.eu.onfido.com/v3.6/live_photos/",
        json={
            "error": {
                "type": "validation_error",
                "message": "There was a validation error on this request",
                "fields": {
                    "face_detection": [
                        "Face not detected in image. Please note this validation can be disabled by setting the advanced_validation parameter to false."
                    ]
                },
            }
        },
        headers={ 'Content-Type': 'application/json' },
        status_code=422
    )

    sample_file = open("sample_photo.png", "rb")
    request_body = {"advanced_validation": "true"}

    with pytest.raises(OnfidoRequestError) as error:
        api.live_photo.upload(sample_file, request_body)

    assert mock_upload.called is True
    assert error.value.args[0]['fields']['face_detection']
        
def test_find_live_photo(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.6/live_photos/{fake_uuid}", json=[])
    api.live_photo.find(fake_uuid)
    assert mock_find.called is True

def test_list_live_photos(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.6/live_photos/?applicant_id={fake_uuid}", json=[])
    api.live_photo.all(fake_uuid)
    assert mock_list.called is True

def test_download_live_photo(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.6/live_photos/{fake_uuid}/download", text="FAKE IMAGE BINARY", headers={"Content-type": "image/png"})
    onfido_download = api.live_photo.download(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "image/png"
