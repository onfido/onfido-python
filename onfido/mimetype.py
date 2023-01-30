import mimetypes

def mimetype_from_name(filename):
    mimetype, _ = mimetypes.guess_type(filename)
    return mimetype