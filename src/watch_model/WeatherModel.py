from dataclasses import dataclass

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


class WeatherModel:

    # I am currently looking into the use of @property annotations & decorators for getter & setter methods
    # However I am not sure on how to use them right now, so i am manually creating mapping methods
    def __init__(self):
        self.lat, self.lon = 0, 0

    @property
    def coord(self):
        return self.lat, self.lon

    @coord.setter
    def coord(self, lat, lon):
        self.lat, self.lon = lat, lon
