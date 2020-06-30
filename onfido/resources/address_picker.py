from ..resource import Resource


class Addresses(Resource):
    def pick(self, postcode:str):
        return self.get(f"addresses/pick?postcode={postcode}")
