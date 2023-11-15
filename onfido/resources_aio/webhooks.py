from ..aio_resource import Resource


class Webhooks(Resource):
    def create(self, request_body: dict):
        return self._post("webhooks", **request_body)

    def all(self):
        return self._get("webhooks")

    def find(self, webhook_id: str):
        return self._get(f"webhooks/{webhook_id}")

    def edit(self, webhook_id: str, request_body: dict):
        return self._put(f"webhooks/{webhook_id}", request_body)

    def delete(self, webhook_id: str):
        return self._delete_request(f"webhooks/{webhook_id}")
