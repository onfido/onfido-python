import pytest

from onfido import ApiException, MotionCapture, MotionCapturesList
from os import environ


@pytest.fixture(scope="function")
def applicant_id(onfido_api):
    return environ["ONFIDO_SAMPLE_APPLICANT_ID"]


@pytest.fixture(scope="function")
def motion_id(onfido_api):
    return environ["ONFIDO_SAMPLE_MOTION_ID_1"]


def test_list_motion_captures(onfido_api, applicant_id):
    motion_captures = onfido_api.list_motion_captures(applicant_id)

    assert len(motion_captures.motion_captures) > 0
    assert isinstance(motion_captures, MotionCapturesList)
    assert isinstance(motion_captures.motion_captures[0], MotionCapture)


def test_retrieve_motion_capture(onfido_api, motion_id):
    get_motion_capture = onfido_api.find_motion_capture(motion_id)

    assert get_motion_capture.id == motion_id
    assert isinstance(get_motion_capture, MotionCapture)


def test_download_motion_capture(onfido_api, motion_id):
    file = onfido_api.download_motion_capture(motion_id)

    assert len(file) > 0


def test_download_motion_capture_frame(onfido_api, motion_id):
    file = onfido_api.download_motion_capture_frame(motion_id)

    assert len(file) > 0


def test_download_inexistent_motion_capture(onfido_api):
    inexistent_motion_id = "00000000-0000-0000-0000-000000000000"

    with pytest.raises(ApiException):
        onfido_api.download_live_video(inexistent_motion_id)
