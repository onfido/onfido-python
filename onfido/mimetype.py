import mimetypes
import os

def mimetype_from_name(filename):
    name, extension = os.path.splitext(filename)
    return mimetypes.types_map[extension]
