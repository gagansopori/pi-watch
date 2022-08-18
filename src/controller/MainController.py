import time

from src.constants.DisplayConstants import TWENTY_MINS, FIVE_SEC_DELAY
from src.model.WeatherModel import WeatherModel
from src.views.BuildClockScreen import BuildClockScreen
from src.services.FetchCurrentWeather import RetrieveLocationBasedWeatherInfo
from src.services.FetchDateTime import RetrieveDateAndTime
from src.services.FetchUserLocation import FetchUserLocation


class MainController:
    def __init__(self):
        self.clock_view = BuildClockScreen()

        self.user_location = FetchUserLocation()
        self.time_date = RetrieveDateAndTime()
        self.weather = RetrieveLocationBasedWeatherInfo()

        self.ctr = 0

    def start_clock(self):
        """
        Driver/Controller method for getting location based weather. This method might have to be refactored when
        adding capabilities to the clock such as Alarm, Music etc. also when the clock makes DB inserts in later
        revisions.
        """
        weather_object = WeatherModel()
        while True:
            current_time = self.time_date.fetch_time()
            if self.ctr == 0 or self.ctr >= TWENTY_MINS:
                geo_location = self.user_location.get_location()
                weather_object = self.weather.get_weather(geo_location)
                self.ctr = 0
            self.ctr += 1

            self.clock_view.clock_face(weather_object, current_time)
            time.sleep(FIVE_SEC_DELAY)
