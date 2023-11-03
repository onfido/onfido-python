from ..aio_resource import Resource


class Addresses(Resource):
    def pick(self, postcode: str):
        return self._get(f"addresses/pick?postcode={postcode}")
