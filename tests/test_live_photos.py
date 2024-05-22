import pytest

from onfido import ApiException, LivePhoto, LivePhotosList
from tests.conftest import create_applicant, upload_live_photo


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function", autouse=True)
def live_photo(onfido_api, applicant_id):
    return upload_live_photo(onfido_api, applicant_id)


def test_create_live_photo(applicant_id, live_photo):
    assert live_photo is not None
    assert live_photo.file_name == "sample_photo.png"
    assert isinstance(live_photo, LivePhoto)


def test_list_live_photos(onfido_api, applicant_id):
    live_photos = onfido_api.list_live_photos(applicant_id)

    assert len(live_photos.live_photos) > 0
    assert isinstance(live_photos, LivePhotosList)


def test_retrieve_live_photo(onfido_api, live_photo):
    get_live_photo = onfido_api.find_live_photo(live_photo.id)

    assert get_live_photo.id == live_photo.id
    assert isinstance(get_live_photo, LivePhoto)


def test_download_live_photo(onfido_api, live_photo):
    file = onfido_api.download_live_photo(live_photo.id)

    assert len(file) > 0


def test_download_inexistent_live_photo(onfido_api):
    inexistent_live_photo_id = "00000000-0000-0000-0000-000000000000"

    with pytest.raises(ApiException):
        onfido_api.download_live_photo(inexistent_live_photo_id)
