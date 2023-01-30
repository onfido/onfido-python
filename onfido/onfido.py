from .resources.applicants import Applicants
from .resources.documents import Documents
from .resources.address_picker import Addresses
from .resources.checks import Checks
from .resources.reports import Reports
from .resources.live_photos import LivePhotos
from .resources.live_videos import LiveVideos
from .resources.motion_captures import MotionCaptures
from .resources.webhooks import Webhooks
from .resources.sdk_tokens import SdkToken
from .resources.extraction import Extraction
from .resources.watchlist_monitors import WatchlistMonitors
from .regions import Region
from .exceptions import OnfidoRegionError


class Api:
    def __init__(self, api_token, region, timeout=None):
        self.applicant = Applicants(api_token, region, timeout)
        self.document = Documents(api_token, region, timeout)
        self.address = Addresses(api_token, region, timeout)
        self.check = Checks(api_token, region, timeout)
        self.report = Reports(api_token, region, timeout)
        self.sdk_token = SdkToken(api_token, region, timeout)
        self.webhook = Webhooks(api_token, region, timeout)
        self.live_photo = LivePhotos(api_token, region, timeout)
        self.live_video = LiveVideos(api_token, region, timeout)
        self.motion_capture = MotionCaptures(api_token, region, timeout)
        self.extraction = Extraction(api_token, region, timeout)
        self.watchlist_monitor = WatchlistMonitors(api_token, region, timeout)

        if region in [Region.EU, Region.US, Region.CA]:
            pass
        elif "api.onfido.com" in region:
            raise OnfidoRegionError("The region must be one of Region.EU, Region.US or Region.CA. We previously defaulted to Region.EU, so if you previously didn’t set a region or used api.onfido.com, please set your region to Region.EU")
