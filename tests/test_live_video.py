import pytest

from onfido import ApiException, LiveVideo, LiveVideosList
from os import environ


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return environ["ONFIDO_SAMPLE_APPLICANT_ID"]


@pytest.fixture(scope="function")
def live_video_id(onfido_api):
    return environ["ONFIDO_SAMPLE_VIDEO_ID_1"]


def test_list_live_videos(onfido_api, applicant_id):
    live_videos = onfido_api.list_live_videos(applicant_id)

    assert len(live_videos.live_videos) > 0
    assert isinstance(live_videos, LiveVideosList)
    assert isinstance(live_videos.live_videos[0], LiveVideo)


def test_retrieve_live_video(onfido_api, live_video_id):
    get_live_video = onfido_api.find_live_video(live_video_id)

    assert get_live_video.id == live_video_id
    assert isinstance(get_live_video, LiveVideo)


def test_download_live_video(onfido_api, live_video_id):
    file = onfido_api.download_live_video(live_video_id)

    assert len(file) > 0


def test_download_live_video_frame(onfido_api, live_video_id):
    file = onfido_api.download_live_video_frame(live_video_id)

    assert len(file) > 0


def test_download_inexistent_live_video(onfido_api):
    inexistent_live_video_id = "00000000-0000-0000-0000-000000000000"

    with pytest.raises(ApiException):
        onfido_api.download_live_video(inexistent_live_video_id)
