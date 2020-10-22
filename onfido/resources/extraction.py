from ..resource import Resource


class Extraction(Resource):
    def perform(self, document_id: str):
        return self.post("extractions/", document_id=document_id)
