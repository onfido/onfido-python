from ..resource import Resource


class Reports(Resource):
    def find(self, report_id:str):
        return self._get(f"reports/{report_id}")

    def all(self, check_id:str):
        payload = {"check_id": check_id}
        return self._get("reports/", payload=payload)

    def resume(self, report_id:str):
        return self._post(f"reports/{report_id}/resume")

    def cancel(self, report_id:str):
        self._post(f"reports/{report_id}/cancel")
