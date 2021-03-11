from ..resource import Resource


class Checks(Resource):
    def create(self, request_body:dict):
        return self._post("checks/", **request_body)

    def find(self, check_id:str):
        return self._get(f"checks/{check_id}")

    def all(self, applicant_id:str):
        payload = {"applicant_id": applicant_id}
        return self._get("checks/", payload=payload)

    def resume(self, check_id:str):
        self._post(f"checks/{check_id}/resume")

    def download(self, check_id:str):
        return self._download_request(f"checks/{check_id}/download")
