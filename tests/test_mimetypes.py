from onfido.mimetype import mimetype_from_name

def test_mimetypes():
    assert mimetype_from_name("filename.jpg") == "image/jpeg"
    assert mimetype_from_name("filename.png") == "image/png"
    assert mimetype_from_name("file.pdf") == "application/pdf"

def test_secondary_mimetypes():
    assert mimetype_from_name("filename.jpeg") == "image/jpeg"

def test_uppercase():
    """Uppercase file extensions are handled."""
    assert mimetype_from_name("filename.JPG") == "image/jpeg"
