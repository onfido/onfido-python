from aiohttp import AsyncIterablePayload, ClientSession, MultipartWriter, StringPayload
from .exceptions import OnfidoRequestError
from aiohttp.client_reqrep import ClientResponse
from .onfido_download import OnfidoAioDownload
from .exceptions import async_error_decorator, OnfidoUnknownError
from .mimetype import mimetype_from_name
from .utils import form_data_converter
from typing import BinaryIO

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

CURRENT_VERSION = importlib_metadata.version("onfido-python")


class Resource:
    def __init__(self, api_token, region, aio_session: ClientSession, timeout):
        self._api_token = api_token
        self._region = region
        self._timeout = timeout
        self._aio_session = aio_session

    @property
    def _url(self):
        return getattr(self._region, "region_url", self._region)

    def _build_url(self, path):
        return self._url + path

    @property
    def _headers(self):
        return {
            "User-Agent": f"onfido-python/{CURRENT_VERSION}",
            "Authorization": f"Token token={self._api_token}",
        }

    async def _handle_response(self, response: ClientResponse):
        if response.status == 422:
            error = None
            content_type = response.headers.get("Content-Type", "")
            if "application/json" in content_type:
                resp_json = await response.json()
                error = resp_json.get("error")
            raise OnfidoRequestError(error)

        response.raise_for_status()
        if response.status == 204:
            return None

        try:
            return await response.json()
        except ValueError as e:
            raise OnfidoUnknownError("Onfido returned invalid JSON") from e

    @async_error_decorator
    async def _upload_request(self, path, file: BinaryIO, **request_body):
        import uuid

        boundary = uuid.uuid4().hex
        with MultipartWriter("form-data", boundary=boundary) as mpwriter:
            for k, v in form_data_converter(request_body).items():
                part = mpwriter.append(
                    StringPayload(
                        v, headers={"Content-Disposition": f'form-data; name="{k}"'}
                    )
                )

            file_part = mpwriter.append_payload(
                AsyncIterablePayload(
                    file,
                    content_type=mimetype_from_name(file.name),
                    headers={
                        "Content-Disposition": f'form-data; name="file"; filename="{file.name}"'
                    },
                )
            )
            additional_headers = {
                "Content-Type": f"multipart/form-data;boundary={boundary}"
            }
            async with self._aio_session.post(
                self._build_url(path),
                data=mpwriter,
                headers=dict(self._headers, **additional_headers),
                timeout=self._timeout,
            ) as response:
                return await self._handle_response(response)

    @async_error_decorator
    async def _post(self, path, **request_body):
        async with self._aio_session.post(
            self._build_url(path),
            json=request_body,
            headers=self._headers,
            timeout=self._timeout,
        ) as response:
            return await self._handle_response(response)

    @async_error_decorator
    async def _put(self, path, data=None):
        async with self._aio_session.put(
            self._build_url(path),
            json=data,
            headers=self._headers,
            timeout=self._timeout,
        ) as response:
            return await self._handle_response(response)

    @async_error_decorator
    async def _get(self, path, payload=None):
        async with self._aio_session.get(
            self._build_url(path), headers=self._headers, timeout=self._timeout
        ) as response:
            return await self._handle_response(response)

    @async_error_decorator
    async def _download_request(self, path):
        async with self._aio_session.get(
            self._build_url(path), headers=self._headers, timeout=self._timeout
        ) as response:
            response.raise_for_status()

            return OnfidoAioDownload(response)

    @async_error_decorator
    async def _delete_request(self, path):
        async with self._aio_session.delete(
            self._build_url(path), headers=self._headers, timeout=self._timeout
        ) as response:
            return await self._handle_response(response)
