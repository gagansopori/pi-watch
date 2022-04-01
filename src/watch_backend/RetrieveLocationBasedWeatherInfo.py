import urllib.request, json

from src.watch_constants.GenericConstants import *


class RetrieveLocationBasedWeatherInfo:
    def __init__(self):
        self.ctr, self.desc_cond, self.general_temperature, self.icon_id = 0, 0, 0, 0
        self.lat, self.lon = 0, 0

    def get_location(self):
        try:

            with urllib.request.urlopen("http://ip-api.com/json") as url_response:
                url = url_response.read().decode('utf-8')
                ip_dat = json.loads(url)
            url_response.close()
            # set the latitude & longitude
            self.lat, self.lon = ip_dat['lat'], ip_dat['lon']

            return self.lat, self.lon

        except Exception as e:
            # traceback.print_exc()
            return "Error %s: Cannot get location" % e

    def get_weather(self, lat, lon):
        weather_url = '%slat=%s&lon=%s&appid=%s' % (base_weather_url, lat, lon, owm_key)
        response_data = {}

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
            country, city = response_data['sys']['country'], response_data['name']

            # iconCode (currentCondition)
            self.icon_id = response_data['weather'][0]['icon']

            # current conditions
            current_temperature = response_data['main']['temp']
            current_condition = response_data['weather'][0]['main']
            current_condition_desc = response_data['weather'][0]['description']
            self.desc_cond = current_condition_desc.title()
        else:
            current_temperature = 0

        if country in Imperial_Countries:
            # SI = "F"
            temperature = (current_temperature * (9 / 5)) - 459.67
            self.general_temperature = "%.0f%s" % (temperature, deg)
        else:
            # SI = "C"
            temperature = current_temperature - 273
            self.general_temperature = "%.0f%s" % (temperature, deg)

        return self.desc_cond, self.general_temperature, self.icon_id
