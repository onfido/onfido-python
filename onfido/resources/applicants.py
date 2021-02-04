from ..resource import Resource


class Applicants(Resource):
    def create(self, request_body:dict):
        return self._post("applicants/", **request_body)

    def update(self, applicant_id:str, request_body:dict):
        return self._put(f"applicants/{applicant_id}", request_body)

    def find(self, applicant_id:str):
        return self._get(f"applicants/{applicant_id}")

    def delete(self, applicant_id:str):
        self._delete_request(f"applicants/{applicant_id}")

    def all(self, **user_payload:dict):
        payload = {"include_deleted": False, "per_page": 20, "page": 1}
        payload.update(user_payload)
        return self._get("applicants", payload=payload)

    def restore(self, applicant_id:str):
        self._post(f"applicants/{applicant_id}/restore")
