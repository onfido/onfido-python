import requests
import requests.exceptions
from aiohttp.http_exceptions import HttpProcessingError
from aiohttp.client_exceptions import (
    ServerTimeoutError,
    ClientConnectionError,
    ClientError,
)


class OnfidoError(Exception):
    pass


class OnfidoRegionError(Exception):
    pass


class OnfidoUnknownError(OnfidoError):
    pass


class OnfidoInvalidSignatureError(OnfidoError):
    pass


class OnfidoRequestError(OnfidoError):
    pass


class OnfidoServerError(OnfidoError):
    pass


class OnfidoConnectionError(OnfidoError):
    pass


class OnfidoTimeoutError(OnfidoError):
    pass


def error_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except requests.HTTPError as e:
            if e.response.status_code >= 500:
                raise OnfidoServerError() from e
            else:
                error = None
                if e.response.status_code == 422:
                    content_type = e.response.headers.get("Content-Type", "")
                    if "application/json" in content_type:
                        resp_json = e.response.json()
                        error = resp_json.get("error")
                raise OnfidoRequestError(error) from e

        except requests.Timeout as e:
            raise OnfidoTimeoutError(e)

        except requests.ConnectionError as e:
            raise OnfidoConnectionError(e)

        except requests.RequestException as e:
            raise OnfidoUnknownError(e)

    return wrapper


def async_error_decorator(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except HttpProcessingError as e:
            if e.code >= 500:
                raise OnfidoServerError() from e
            else:
                raise OnfidoRequestError(e.message) from e

        except ServerTimeoutError as e:
            raise OnfidoTimeoutError(e)

        except ClientConnectionError as e:
            raise OnfidoConnectionError(e)

        except ClientError as e:
            raise OnfidoUnknownError(e)

    return wrapper
