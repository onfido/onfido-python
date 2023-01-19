import onfido
from onfido.regions import Region

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_find_motion_capture(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.6/motion_captures/{fake_uuid}", json=[])
    api.motion_capture.find(fake_uuid)
    assert mock_find.called is True

def test_list_live_videos(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.6/motion_captures/?applicant_id={fake_uuid}", json=[])
    api.motion_capture.all(fake_uuid)
    assert mock_list.called is True

def test_download_live_video(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.6/motion_captures/{fake_uuid}/download", text="FAKE BINARY", headers={"Content-type": "video/mp4"})
    onfido_download = api.motion_capture.download(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "video/mp4"

def test_download_live_video_frame(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.6/motion_captures/{fake_uuid}/frame", text="FAKE BINARY", headers={"Content-type": "video/mp4"})
    onfido_download = api.motion_capture.download_frame(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "video/mp4"
