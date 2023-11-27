from .resources.applicants import Applicants
from .resources.documents import Documents
from .resources.address_picker import Addresses
from .resources.checks import Checks
from .resources.workflow_runs import WorkflowRuns
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

from .resources_aio.applicants import Applicants as AsyncApplicants
from .resources_aio.documents import Documents as AsyncDocuments
from .resources_aio.address_picker import Addresses as AsyncAddresses
from .resources_aio.checks import Checks as AsyncChecks
from .resources_aio.workflow_runs import WorkflowRuns as AsyncWorkflowRuns
from .resources_aio.reports import Reports as AsyncReports
from .resources_aio.live_photos import LivePhotos as AsyncLivePhotos
from .resources_aio.live_videos import LiveVideos as AsyncLiveVideos
from .resources_aio.motion_captures import MotionCaptures as AsyncMotionCaptures
from .resources_aio.webhooks import Webhooks as AsyncWebhooks
from .resources_aio.sdk_tokens import SdkToken as AsyncSdkToken
from .resources_aio.extraction import Extraction as AsyncExtraction
from .resources_aio.watchlist_monitors import WatchlistMonitors as AsyncWatchlistMonitors

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
        self.workflowrun = WorkflowRuns(api_token, region, timeout)

        if region in [Region.EU, Region.US, Region.CA]:
            pass
        elif "api.onfido.com" in region:
            raise OnfidoRegionError("The region must be one of Region.EU, Region.US or Region.CA. We previously defaulted to Region.EU, so if you previously didn’t set a region or used api.onfido.com, please set your region to Region.EU")

class AsyncApi:
    def __init__(self, api_token, region, aio_session, timeout=None):
        self.applicant = AsyncApplicants(api_token, region, aio_session, timeout)
        self.document = AsyncDocuments(api_token, region, aio_session, timeout)
        self.address = AsyncAddresses(api_token, region, aio_session, timeout)
        self.check = AsyncChecks(api_token, region, aio_session, timeout)
        self.report = AsyncReports(api_token, region, aio_session, timeout)
        self.sdk_token = AsyncSdkToken(api_token, region, aio_session, timeout)
        self.webhook = AsyncWebhooks(api_token, region, aio_session, timeout)
        self.live_photo = AsyncLivePhotos(api_token, region, aio_session, timeout)
        self.live_video = AsyncLiveVideos(api_token, region, aio_session, timeout)
        self.motion_capture = AsyncMotionCaptures(api_token, region, aio_session, timeout)
        self.extraction = AsyncExtraction(api_token, region, aio_session, timeout)
        self.watchlist_monitor = AsyncWatchlistMonitors(api_token, region, aio_session, timeout)
        self.workflowrun = AsyncWorkflowRuns(api_token, region, aio_session, timeout)

        if region in [Region.EU, Region.US, Region.CA]:
            pass
        elif "api.onfido.com" in region:
            raise OnfidoRegionError("The region must be one of Region.EU, Region.US or Region.CA. We previously defaulted to Region.EU, so if you previously didn’t set a region or used api.onfido.com, please set your region to Region.EU")
