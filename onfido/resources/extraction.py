from ..resource import Resource


class Extraction(Resource):
    def perform(self, document_id: str):
        payload = {"document_id": document_id}
        return self.post("extractions/", payload=payload)
