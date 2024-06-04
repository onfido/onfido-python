import pytest

from onfido import ApiException, IdPhoto, IdPhotosList
from tests.conftest import create_applicant, upload_id_photo


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return create_applicant(onfido_api).id


@pytest.fixture(scope="function", autouse=True)
def id_photo(onfido_api, applicant_id):
    return upload_id_photo(onfido_api, applicant_id)


def test_create_id_photo(applicant_id, id_photo):
    assert id_photo is not None
    assert id_photo.file_name == f"{id_photo.id}.png"
    assert isinstance(id_photo, IdPhoto)


def test_list_id_photos(onfido_api, applicant_id):
    id_photos = onfido_api.list_id_photos(applicant_id)

    assert len(id_photos.id_photos) > 0
    assert isinstance(id_photos, IdPhotosList)


def test_retrieve_id_photo(onfido_api, id_photo):
    get_id_photo = onfido_api.find_id_photo(id_photo.id)

    assert get_id_photo.id == id_photo.id
    assert isinstance(get_id_photo, IdPhoto)


def test_download_id_photo(onfido_api, id_photo):
    file = onfido_api.download_id_photo(id_photo.id)

    assert len(file) > 0


def test_download_inexistent_id_photo(onfido_api):
    inexistent_id_photo_id = "00000000-0000-0000-0000-000000000000"

    with pytest.raises(ApiException):
        onfido_api.download_id_photo(inexistent_id_photo_id)
