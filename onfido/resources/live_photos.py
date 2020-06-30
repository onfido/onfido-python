from ..resource import Resource


class LivePhotos(Resource):
    def upload(self, sample_file:bytes, request_body):

        return self.upload_request("live_photos/", sample_file, **request_body)

    def find(self, live_photo_id:str):
        return self.get(f"live_photos/{live_photo_id}")

    def all(self, applicant_id:str):
        payload = {"applicant_id": applicant_id}
        return self.get("live_photos/", payload=payload)

    def download(self, live_photo_id:str):
        return self.download_request(f"live_photos/{live_photo_id}/download")
