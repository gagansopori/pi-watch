import urllib.request, json
from urllib.error import URLError

from src.watch_constants.GenericConstants import ip_api_url, base_weather_url, owm_key, degree_symbol, \
    imperial_countries
from src.watch_model.WeatherModel import FinalData


class RetrieveLocationBasedWeatherInfo:
    def __init__(self):
        # setting these values with some defaults here - you are more than welcome to modify it to your interests.
        self.desc_cond: str = "Yee-haw"
        self.general_temperature: float = 420.00
        self.icon_id: str = "01d"

        # location will default to Bentonville City Square
        self.lat: float = 36.3725
        self.lon: float = -94.2106
        self.country: str = "US"

    '''
    This method hits a ip-based geo-location service to determine the geographical coordinates of your location which 
    would be used in getting the weather information for your area from the weather service.
    @:returns - latitude, longitude
    '''
    def get_location(self) -> (float, float):
        try:
            with urllib.request.urlopen(ip_api_url) as url_request:
                url_response = url_request.read().decode('utf-8')
                ip_data = json.loads(url_response)
            url_request.close()
            # set the latitude & longitude
            self.lat, self.lon = ip_data['lat'], ip_data['lon']
        except (ConnectionError, URLError):
            print("Connection Error... Using Default Location!")
        return self.lat, self.lon

    '''
    This method takes geographical coordinates & calls the open-weather api to determine the weather conditions for a given
    set of geo-coordinates.
    @:param - latitude, longitude
    @:return - current_temperature, weather_condition, icon_id
    '''
    def get_weather(self, lat, lon) -> (str, float, str):
        weather_url = f'{base_weather_url}lat={lat}&lon={lon}&appid={owm_key}'
        try:
            api_response = urllib.request.urlopen(weather_url)
            response_query = api_response.read().decode('utf-8')
            response_data = json.loads(response_query)
            api_response.close()
        except (ConnectionError, URLError) as ce:
            response_data = {'Error': 'Cannot connect to internet at the moment: {}'.format(ce)}
        except (ValueError, TypeError) as e:
            response_data = {'Error': 'Cannot interpret the response due to data or type mismatch: {}'.format(e)}

        if 'Error' not in response_data.keys():
            # country, city
            self.country, city = response_data['sys']['country'], response_data['name']

            # icon-code for current conditions
            self.icon_id = response_data['weather'][0]['icon']

            # current conditions
            current_temperature = response_data['main']['temp']
            temperature = self.scale_temperature(current_temperature, self.country)
            self.general_temperature = f"{temperature:.0f}{degree_symbol}"

            current_condition = response_data['weather'][0]['main']
            current_condition_desc = response_data['weather'][0]['description']
            # .title() capitalizes first character of each word
            self.desc_cond = current_condition_desc.title()
        else:
            current_temperature = 420.00
            # temperature = self.scale_temperature(current_temperature, self.country)
            self.general_temperature = f"{current_temperature:.0f}{degree_symbol}"

        return self.desc_cond, self.general_temperature, self.icon_id

    '''
    Helper method to convert the temperature from Kelvin Scale to Fahrenheit or Celsius depending on the metric system 
    the given country uses.
    '''
    def scale_temperature(self, current_temp, country) -> float:
        if country in imperial_countries:
            return (current_temp * (9 / 5)) - 459.67
        else:
            return current_temp - 273
