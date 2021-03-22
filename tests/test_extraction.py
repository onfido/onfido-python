import onfido

api = onfido.Api("<AN_API_TOKEN>")

fake_document_uuid = "58a9c6d2-8661-4dbd-96dc-b9b9d344a7ce"


def test_perform_extraction(requests_mock):
    mock_upload = requests_mock.post("https://api.eu.onfido.com/v3.1/extractions/", json=[])

    api.extraction.perform(fake_document_uuid)

    assert mock_upload.called is True
