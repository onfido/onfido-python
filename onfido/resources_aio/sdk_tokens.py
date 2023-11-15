from ..aio_resource import Resource


class SdkToken(Resource):
    def generate(self, request_body):
        return self._post("sdk_token", **request_body)
