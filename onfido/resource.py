import requests
from .onfido_download import OnfidoDownload
from .exceptions import error_decorator, OnfidoUnknownError
from .mimetype import mimetype_from_name
from .utils import form_data_converter

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

CURRENT_VERSION = importlib_metadata.version("onfido-python")

class Resource:
    def __init__(self, api_token, region, timeout):
        self._api_token = api_token
        self._region = region
        self._timeout = timeout

    @property
    def _url(self):
        return getattr(self._region, "region_url", self._region)

    def _build_url(self, path):
        return self._url + path

    @property
    def _headers(self):
        return {
            "User-Agent": f"onfido-python/{CURRENT_VERSION}",
            "Authorization": f"Token token={self._api_token}"
        }

    def _handle_response(self, response):
        response.raise_for_status()
        if response.status_code == 204:
            return None

        try:
            return response.json()
        except ValueError as e:
            raise OnfidoUnknownError("Onfido returned invalid JSON") from e

    @error_decorator
    def _upload_request(self, path, file, **request_body):
        files = {
            'file': (file.name, file, mimetype_from_name(file.name))
        }
        
        response = requests.post(self._build_url(path), data=form_data_converter(request_body),
                                 files=files, headers=self._headers, timeout=self._timeout)

        return self._handle_response(response)

    @error_decorator
    def _post(self, path, **request_body):
        response = requests.post(self._build_url(path), json=request_body, headers=self._headers, timeout=self._timeout)

        return self._handle_response(response)

    @error_decorator
    def _put(self, path, data=None):
        response = requests.put(self._build_url(path), json=data, headers=self._headers, timeout=self._timeout)

        return self._handle_response(response)

    @error_decorator
    def _get(self, path, payload=None):
        response = requests.get(self._build_url(path), headers=self._headers, params=payload, timeout=self._timeout)

        return self._handle_response(response)

    @error_decorator
    def _download_request(self, path):
        response = requests.get(self._build_url(path), headers=self._headers, timeout=self._timeout)

        response.raise_for_status()

        try:
            return OnfidoDownload(response)
        except ValueError as e:
            raise OnfidoUnknownError("Onfido returned invalid JSON") from e

    @error_decorator
    def _delete_request(self, path):
        response = requests.delete(self._build_url(path), headers=self._headers, timeout=self._timeout)

        return self._handle_response(response)
