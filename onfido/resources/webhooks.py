from ..resource import Resource


class Webhooks(Resource):
    def create(self, request_body:dict):
        return self.post("webhooks", **request_body)

    def all(self):
        return self.get("webhooks")

    def find(self, webhook_id:str):
        return self.get(f"webhooks/{webhook_id}")

    def edit(self, webhook_id:str, request_body:dict):
        return self.put(f"webhooks/{webhook_id}", request_body)

    def delete(self, webhook_id:str):
        self.delete_request(f"webhooks/{webhook_id}")
