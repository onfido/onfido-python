from ..aio_resource import Resource


class WatchlistMonitors(Resource):
    def create(self, request_body: dict):
        return self._post("watchlist_monitors/", **request_body)

    def find(self, monitor_id: str):
        return self._get(f"watchlist_monitors/{monitor_id}")

    def all(self, applicant_id: str):
        payload = {"applicant_id": applicant_id}
        return self._get("watchlist_monitors/", payload=payload)

    def delete(self, monitor_id: str):
        return self._delete_request(f"watchlist_monitors/{monitor_id}")
