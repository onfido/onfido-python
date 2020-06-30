class OnfidoDownload:
    def __init__(self, response):
        self.content = response.content
        self.content_type = response.headers['content-type']
