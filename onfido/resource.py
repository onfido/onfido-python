import requests
from .onfido_download import OnfidoDownload
from .exceptions import error_decorator, OnfidoUnknownError
from .mimetype import mimetype_from_name

class Resource:
    def __init__(self, api_token, base_url):
        self.api_token = api_token
        self.base_url = base_url

    @property
    def url(self):
        return getattr(self.base_url, "region_url", self.base_url)

    def build_url(self, path):
        return self.url + path

    @property
    def _headers(self):
        return {
            "Authorization": f"Token token={self.api_token}"
        }

    def handle_response(self, response):
        response.raise_for_status()
        if response.status_code == 204:
            return None

        try:
            return response.json()
        except ValueError as e:
            raise OnfidoUnknownError("Onfido returned invalid JSON") from e

    @error_decorator
    def upload_request(self, path, file, **request_body):
        files = {
            'file': (file.name, file, mimetype_from_name(file.name))
        }
        
        response = requests.post(self.build_url(path), data=request_body, files = files, headers=self._headers)

        return self.handle_response(response)

    @error_decorator
    def post(self, path, **request_body):
        response = requests.post(self.build_url(path), json=request_body,
                                 headers=self._headers)

        return self.handle_response(response)

    @error_decorator
    def put(self, path, data=None):
        response = requests.put(self.build_url(path), json=data,
                                headers=self._headers)

        return self.handle_response(response)

    @error_decorator
    def get(self, path, payload=None):
        response = requests.get(self.build_url(path), headers=self._headers, params=payload)

        return self.handle_response(response)

    @error_decorator
    def download_request(self, path):
        response = requests.get(self.build_url(path), headers=self._headers)

        response.raise_for_status()

        try:
            return OnfidoDownload(response)
        except ValueError as e:
            raise OnfidoUnknownError("Onfido returned invalid JSON") from e


    @error_decorator
    def delete_request(self, path):
        response = requests.delete(self.build_url(path), headers=self._headers)

        return self.handle_response(response)

