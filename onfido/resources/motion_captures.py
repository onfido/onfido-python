from ..resource import Resource


class MotionCaptures(Resource):
    def find(self, motion_capture_id:str):
        return self._get(f"motion_captures/{motion_capture_id}")

    def all(self, applicant_id:str):
        payload = {"applicant_id": applicant_id}
        return self._get("motion_captures/", payload=payload)

    def download(self, motion_capture_id:str):
        return self._download_request(f"motion_captures/{motion_capture_id}/download")

    def download_frame(self, motion_capture_id:str):
        return self._download_request(f"motion_captures/{motion_capture_id}/frame")