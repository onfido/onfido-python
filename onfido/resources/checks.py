from ..resource import Resource


class Checks(Resource):
    def create(self, request_body:dict):
        return self.post("checks/", **request_body)

    def find(self, check_id:str):
        return self.get(f"checks/{check_id}")

    def all(self, applicant_id:str):
        payload = {"applicant_id": applicant_id}
        return self.get("checks/", payload=payload)

    def resume(self, check_id:str):
        self.post(f"checks/{check_id}/resume")
