from aiohttp.client_reqrep import ClientResponse

class OnfidoDownload:
    def __init__(self, response):
        self.content = response.content
        self.content_type = response.headers['content-type']

class OnfidoAioDownload:
    def __init__(self, response: ClientResponse):
        self.content = response.content
        self.content_type = response.content_type
