import urllib.request, json
from urllib.error import URLError

from application.model.LocationModel import LocationModel
from application.constants.GenericConstants import ip_api_url


class FetchUserLocation:
    def __init__(self):
        self.geo_coordinates = LocationModel()

    def get_location(self) -> LocationModel:
        """
        This method hits an ip-based geolocation service to determine the geographical coordinates of your location
        which would be used in getting the weather information for your area from the weather service.
        :returns: latitude, longitude
        """
        try:
            with urllib.request.urlopen(ip_api_url) as url_request:
                url_response = url_request.read().decode('utf-8')
                ip_data = json.loads(url_response)
            url_request.close()
            # set the latitude & longitude
            self.geo_coordinates.latitude = ip_data['lat']
            self.geo_coordinates.longitude = ip_data['lon']
        except (ConnectionError, URLError):
            print("Connection Error... Using Default Location!")

        return self.geo_coordinates
