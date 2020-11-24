from .resources.applicants import Applicants
from .resources.documents import Documents
from .resources.address_picker import Addresses
from .resources.checks import Checks
from .resources.reports import Reports
from .resources.live_photos import LivePhotos
from .resources.live_videos import LiveVideos
from .resources.webhooks import Webhooks
from .resources.sdk_tokens import SdkToken
from .resources.extraction import Extraction
from .regions import Region


class Api:
    def __init__(self, api_token, base_url=Region.EU, timeout=None):
        self.applicant = Applicants(api_token, base_url, timeout)
        self.document = Documents(api_token, base_url, timeout)
        self.address = Addresses(api_token, base_url, timeout)
        self.check = Checks(api_token, base_url, timeout)
        self.report = Reports(api_token, base_url, timeout)
        self.sdk_token = SdkToken(api_token, base_url, timeout)
        self.webhook = Webhooks(api_token, base_url, timeout)
        self.live_photo = LivePhotos(api_token, base_url, timeout)
        self.live_video = LiveVideos(api_token, base_url, timeout)
        self.extraction = Extraction(api_token, base_url, timeout)
