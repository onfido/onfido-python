import onfido
from onfido.regions import Region
import io

api = onfido.Api("<AN_API_TOKEN>", region=Region.EU)

fake_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_find_live_video(requests_mock):
    mock_find = requests_mock.get(f"https://api.eu.onfido.com/v3.4/live_videos/{fake_uuid}", json=[])
    api.live_video.find(fake_uuid)
    assert mock_find.called is True

def test_list_live_videos(requests_mock):
    mock_list = requests_mock.get(f"https://api.eu.onfido.com/v3.4/live_videos/?applicant_id={fake_uuid}", json=[])
    api.live_video.all(fake_uuid)
    assert mock_list.called is True

def test_download_live_video(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.4/live_videos/{fake_uuid}/download", text="FAKE VIDEO BINARY", headers={"Content-type": "video/mp4"})
    onfido_download = api.live_video.download(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "video/mp4"

def test_download_live_video_frame(requests_mock):
    mock_download = requests_mock.get(f"https://api.eu.onfido.com/v3.4/live_videos/{fake_uuid}/frame", text="FAKE VIDEO BINARY", headers={"Content-type": "video/mp4"})
    onfido_download = api.live_video.download_frame(fake_uuid)
    assert mock_download.called is True
    assert onfido_download.content_type == "video/mp4"
