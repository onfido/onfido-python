from ..resource import Resource


class WorkflowRuns(Resource):
    def create(self, request_body: dict):
        return self._post("workflow_runs/", **request_body)

    def all(self, **user_payload: dict):
        payload = {"page": 1, "sort": "desc"}
        payload.update(user_payload)
        return self._get("workflow_runs", payload=payload)

    def find(self, workflow_run_id: str):
        return self._get(f"workflow_runs/{workflow_run_id}")

    def evidence(self, workflow_run_id: str):
        return self._download_request(f"workflow_runs/{workflow_run_id}/signed_evidence_file")
