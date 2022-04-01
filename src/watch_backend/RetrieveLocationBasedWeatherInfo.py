import urllib.request, json

from src.watch_constants.GenericConstants import *


class RetrieveLocationBasedWeatherInfo:
    def __init__(self):
        self.desc_cond, self.general_temperature, self.icon_id = 0, 0, 0
        self.lat, self.lon = 0, 0
        self.country = "US"

    '''
    This method hits a ip-based geo-location service to determine the geographical coordinates of your location which 
    would be used in getting the weather information for your area from the weather service.
    @:returns - latitude, longitude
    '''

    def get_location(self):
        try:
            with urllib.request.urlopen(ip_api_url) as url_response:
                url = url_response.read().decode('utf-8')
                ip_dat = json.loads(url)
            url_response.close()
            # set the latitude & longitude
            self.lat, self.lon = ip_dat['lat'], ip_dat['lon']
            return self.lat, self.lon
        except Exception as e:
            # traceback.print_exc()
            return "Error %s: Cannot get location" % e

    '''
    This method takes geographical coordinates & calls the open-weather api to determine the weather conditions for a given
    set of geo-coordinates.
    @:param - latitude, longitude
    @:return - current_temperature, weather_condition, icon_id
    '''

    def get_weather(self, lat, lon):
        weather_url = '%slat=%s&lon=%s&appid=%s' % (base_weather_url, lat, lon, owm_key)
        try:
            api_response = urllib.request.urlopen(weather_url)
            response_query = api_response.read().decode('utf-8')
            response_data = json.loads(response_query)
            api_response.close()
        except ConnectionError as ce:
            response_data = {'Error': 'Cannot connect to internet at the moment: {}'.format(ce)}
        except ValueError as ve:
            response_data = {'Error': ve}
        except TypeError as te:
            response_data = {'Error': te}

        if 'Error' not in response_data.keys():
            # country, city
            self.country, city = response_data['sys']['country'], response_data['name']

            # iconCode (currentCondition)
            self.icon_id = response_data['weather'][0]['icon']

            # current conditions
            current_temperature = response_data['main']['temp']
            temperature = self.scale_temperature(current_temperature, self.country)
            self.general_temperature = "%.0f%s" % (temperature, deg)

            current_condition = response_data['weather'][0]['main']
            current_condition_desc = response_data['weather'][0]['description']
            self.desc_cond = current_condition_desc.title()
        else:
            current_temperature = 0
            temperature = self.scale_temperature(current_temperature, self.country)
            self.general_temperature = "%.0f%s" % (temperature, deg)

        return self.desc_cond, self.general_temperature, self.icon_id

    '''
    Helper method to convert the temperature from Kelvin Scale to Fahrenheit or Celsius depending on the metric system 
    the given country uses.
    '''
    def scale_temperature(self, current_temp, country):
        if country in Imperial_Countries:
            return (current_temp * (9 / 5)) - 459.67
        else:
            return current_temp - 273
