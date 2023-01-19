from enum import Enum


class Region(Enum):
    EU = "https://api.eu.onfido.com/v3.6/"
    US = "https://api.us.onfido.com/v3.6/"
    CA = "https://api.ca.onfido.com/v3.6/"

    @property
    def region_url(self):
        return self.value
