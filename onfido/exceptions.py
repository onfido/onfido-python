import requests
import requests.exceptions


class OnfidoError(Exception):
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
                raise OnfidoRequestError() from e

        except requests.Timeout as e:
            raise OnfidoTimeoutError(e)

        except requests.ConnectionError as e:
            raise OnfidoConnectionError(e)

        except requests.RequestException as e:
            raise OnfidoUnknownError(e)
    return wrapper

