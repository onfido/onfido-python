from ..resource import Resource


class Autofill(Resource):
    def perform(self, request_body: dict):
        return self.post("extractions/", **request_body)
