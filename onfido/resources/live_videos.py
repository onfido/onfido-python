from ..resource import Resource


class LiveVideos(Resource):
    def find(self, live_video_id:str):
        return self._get(f"live_videos/{live_video_id}")

    def all(self, applicant_id:str):
        payload = {"applicant_id": applicant_id}
        return self._get("live_videos/", payload=payload)

    def download(self, live_video_id:str):
        return self._download_request(f"live_videos/{live_video_id}/download")

    def download_frame(self, live_video_id:str):
        return self._download_request(f"live_videos/{live_video_id}/frame")