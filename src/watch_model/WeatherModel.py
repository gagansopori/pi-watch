from dataclasses import dataclass
from typing import List

'''
    {
    "coord": {
        "lon": -94.3219,
        "lat": 36.2891
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 289.92,
        "feels_like": 288.33,
        "temp_min": 288.79,
        "temp_max": 290.83,
        "pressure": 1017,
        "humidity": 26
    },
    "visibility": 10000,
    "wind": {
        "speed": 4.12,
        "deg": 360
    },
    "clouds": {
        "all": 0
    },
    "dt": 1648331656,
    "sys": {
        "type": 2,
        "id": 47727,
        "country": "US",
        "sunrise": 1648296719,
        "sunset": 1648341221
    },
    "timezone": -18000,
    "id": 4101244,
    "name": "Benton",
    "cod": 200
}
    '''

'''
{
Response from: ip-api.com/json
    "status": "success",
    "country": "United States",
    "countryCode": "US",
    "region": "AR",
    "regionName": "Arkansas",
    "city": "Bella Vista",
    "zip": "72715",
    "lat": 36.4691,
    "lon": -94.3219,
    "timezone": "America/Chicago",
    "isp": "Cox Communications Inc.",
    "org": "Cox Communications",
    "as": "AS22773 Cox Communications Inc.",
    "query": "70.178.40.20"
}
'''

# class WeatherModel:
#
#     # I am currently looking into the use of @property annotations & decorators for getter & setter methods
#     # However I am not sure on how to use them right now, so i am manually creating mapping methods
#     def __init__(self):
#         self._current_condition, self._current_condition_desc, self._icon_id = 0, 0, 0
#         self._temp, self._feels_like, self._temp_min, self._temp_max, self._pressure, self._humidity = 0, 0, 0, 0, 0, 0
#
#     @property
#     def current_condition(self):
#         return self._current_condition
#
#     @current_condition.setter
#     def current_condition(self, current_condition):
#         self._current_condition = current_condition
#
#     @property
#     def current_condition_desc(self):
#         return self._current_condition_desc
#
#     @current_condition_desc.setter
#     def current_condition_desc(self, current_condition_desc):
#         self._current_condition_desc = current_condition_desc
#
#     @property
#     def icon_id(self):
#         return self._icon_id
#
#     @icon_id.setter
#     def icon_id(self, icon_id):
#         self._icon_id = icon_id
#
#     @property
#     def temp(self):
#         return self._temp
#
#     @temp.setter
#     def temp(self, temperature):
#         self._temp = temperature
#
#     @property
#     def feels_like(self):
#         return self._feels_like
#
#     @temp.setter
#     def feels_like(self, feels_like):
#         self._feels_like = feels_like


# @dataclass
# class ResponseCoordinates:
#     lon: float
#     lat: float
#
#
# @dataclass
# class WeatherDescription:
#     id: int
#     main: str
#     description: str
#     icon: str
#
#
# @dataclass
# class TemperatureMetrics:
#     temp: float
#     feels_like: float
#     temp_min: float
#     temp_max: float
#     pressure: int
#     humidity: int
#
#     def __init__(self):
#         self.feels_like = 0
#
#     @property
#     def feels_like(self):
#         return self.feels_like
#
#     @feels_like.setter
#     def feels_like(self, feels_like):
#         self.feels_like = feels_like
#
#
# @dataclass
# class WindMetrics:
#     speed: float
#     deg: float
#
#
# @dataclass
# class CloudTypes:
#     all: int
#
#
# @dataclass
# class EarthSystems:
#     type: int
#     id: int
#     country: str
#     sunrise: int
#     sunset: int
#
#
# @dataclass
# class WeatherResponse:
#     coord: ResponseCoordinates
#     weather: List[WeatherDescription]
#     base: str
#     main: TemperatureMetrics
#     visibility: int
#     wind: WindMetrics
#     clouds: CloudTypes
#     dt: int
#     sys: EarthSystems
#     timezone: int
#     id: int
#     name: str
#     cod: int
#
#
# @dataclass
# class FinalData:
#     weather_response: WeatherResponse
