from PIL import Image
import time

from src.model.WeatherModel import WeatherModel
from src.services.FetchUserLocation import FetchUserLocation
from src.services.FetchDateTime import RetrieveDateAndTime
from src.services.FetchCurrentWeather import RetrieveLocationBasedWeatherInfo
from src.constants.GenericConstants import degree_symbol
from src.watch_interfaces.CreateDisplayElements import CreateDisplay
from src.constants.DisplayConstants import SCREEN_WIDTH, SCREEN_HEIGHT, TWENTY_MINS, BLACK_TRANSPARENT, \
    WHITE_TRANSPARENT, FIVE_SEC_DELAY


class BuildClockScreen:
    def __init__(self):
        self.user_location = FetchUserLocation()
        self.time_date = RetrieveDateAndTime()
        self.weather = RetrieveLocationBasedWeatherInfo()
        self.clock_screen = CreateDisplay()

        self.ctr = 0

    '''
    Driver/Controller method for getting location based weather. This method might have to be refactored when adding capabilities
    to the clock such as Alarm, Music etc etc. Also when the clock makes DB inserts in later revisions.
    '''

    def start_clock(self):
        weather_object = WeatherModel()
        while True:
            current_time = self.time_date.fetch_time()
            if self.ctr == 0 or self.ctr >= TWENTY_MINS:
                geo_location = self.user_location.get_location()
                weather_object = self.weather.get_weather(geo_location)
                self.ctr = 0
            self.ctr += 1

            img_obj = self.clock_face(weather_object, current_time)
            self.clock_screen.display_information(img_obj)
            time.sleep(FIVE_SEC_DELAY)

    ''' 
    Utility method that prepares the UI view with data that needs to be displayed. It takes the weather & possibly 
    location parameters and based on the screen size formats the the text size & placement position.
    @:param - weather_dict -> {desc_condition : str, current_temp: float, icon_id: str}
    '''

    def clock_face(self, weather_data, current_time):
        # Border Padding: in-case its needed
        vertical_padding = 20
        horizontal_padding = 5

        # create a new image - Basically a transparent background for adding an icon later
        img = Image.new('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK_TRANSPARENT)
        img_w, img_h = img.size

        # Build a drawing context
        kntxt = Image.new('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK_TRANSPARENT)
        drawing_context = self.clock_screen.build_context(kntxt)

        # build the fonts & texts
        # time
        font_size_time = int(img_h / 5)
        time_font = self.clock_screen.build_font(font_size_time)
        time_text = f"{current_time.hour}:{current_time.minute} {current_time.meridian}"
        time_w, time_h = self.clock_screen.measure_text(time_font, time_text.upper(), drawing_context)

        # date
        font_size_date = int(img_h / 8)
        date_font = self.clock_screen.build_font(font_size_date)
        date_text = f"{current_time.weekday_name}, {current_time.month_of_year} {current_time.day_of_month}"
        date_w, date_h = self.clock_screen.measure_text(date_font, date_text, drawing_context)

        # weather
        font_size_weather = int(img_h / 10)
        weather_font = self.clock_screen.build_font(font_size_weather)
        weather_text = f"{weather_data.general_temperature:.0f}{degree_symbol} | {weather_data.condition_description}"
        weather_w, weather_h = self.clock_screen.measure_text(weather_font, weather_text, drawing_context)

        # wind
        wind_text = f"{weather_data.wind_speed:.0f}"

        # build the icons
        # weather
        weather_icon = self.clock_screen.resize_icons(weather_data.icon_id, font_size_time)
        weather_icon_x, weather_icon_y = int((img_w - weather_icon.width) / 2), int((vertical_padding + time_h + date_h + weather_h))

        # wind
        wind_icon = self.clock_screen.resize_icons('North', font_size_time).rotate(180)
        wind_icon_x, wind_icon_y = int((horizontal_padding + weather_icon_x + weather_icon.width)), int((vertical_padding + time_h) * 1.1)

        # Actual Text Drawing on the canvas takes place below
        # time
        drawing_context.text(((img_w - time_w) / 2, vertical_padding),
                             time_text.upper(), font=time_font, fill=WHITE_TRANSPARENT, padx=5)
        # date
        drawing_context.text(((img_w - date_w) / 2, (vertical_padding + time_h)),
                             date_text, font=date_font, fill=WHITE_TRANSPARENT, padx=5)
        # weather - text
        drawing_context.text(((img_w - weather_w) / 2, (vertical_padding + time_h + date_h)),
                             weather_text, font=weather_font, fill=WHITE_TRANSPARENT, padx=5)
        # weather - icon
        kntxt.paste(weather_icon, (weather_icon_x, weather_icon_y))
        # kntxt.paste(wind_icon, (wind_icon_x, wind_icon_y))
        final_media = Image.alpha_composite(img, kntxt)
        img.close(), kntxt.close()

        return final_media
