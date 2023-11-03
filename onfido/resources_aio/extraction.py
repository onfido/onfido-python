from ..aio_resource import Resource


class Extraction(Resource):
    def perform(self, document_id: str):
        return self._post("extractions/", document_id=document_id)
