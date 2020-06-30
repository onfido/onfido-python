from ..resource import Resource


class Applicants(Resource):
    def create(self, request_body:dict):
        return self.post("applicants/", **request_body)

    def update(self, applicant_id:str, request_body:dict):
        return self.put(f"applicants/{applicant_id}", request_body)

    def find(self, applicant_id:str):
        return self.get(f"applicants/{applicant_id}")

    def delete(self, applicant_id:str):
        self.delete_request(f"applicants/{applicant_id}")

    def all(self, **user_payload:dict):
        payload = {"include_deleted": False, "per_page": 20, "page": 1}
        payload.update(user_payload)
        return self.get("applicants", payload=payload)

    def restore(self, applicant_id:str):
        self.post(f"applicants/{applicant_id}/restore")
