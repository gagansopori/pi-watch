class LocationModel:
    def __init__(self):
        # location will default to Bentonville Square
        self._latitude: float = 36.3725
        self._longitude: float = -94.2106
        self._country: str = "US"

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, lat):
        self._latitude = lat

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, lon):
        self._longitude = lon

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, cc):
        self._country = cc