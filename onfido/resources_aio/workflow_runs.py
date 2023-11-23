from ..aio_resource import Resource


class WorkflowRuns(Resource):
    def evidence(self, workflow_run_id: str):
        return self._download_request(f"workflow_runs/{workflow_run_id}/signed_evidence_file")
