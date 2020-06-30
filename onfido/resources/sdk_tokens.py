from ..resource import Resource

class SdkToken(Resource):
    def generate(self, request_body):
        return self.post("sdk_token", **request_body)
