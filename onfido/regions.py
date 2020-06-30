from enum import Enum

class Region(Enum):
    EU = "https://api.onfido.com/v3/"
    US = "https://api.us.onfido.com/v3/"
    CA = "https://api.ca.onfido.com/v3/"

    @property
    def region_url(self):
        return self.value
