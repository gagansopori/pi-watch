from PIL import Image
import time

from src.watch_backend.RetrieveDateAndTime import RetrieveDateAndTime
from src.watch_backend.RetrieveLocationBasedWeatherInfo import RetrieveLocationBasedWeatherInfo
from src.watch_interfaces.CreateDisplayElements import CreateDisplay
from src.watch_constants.DisplayConstants import SCREEN_WIDTH, SCREEN_HEIGHT, TWENTY_MINS, BLACK_TRANSPARENT, \
    WHITE_TRANSPARENT, FIVE_SEC_DELAY


class BuildClockScreen:
    def __init__(self):
        self.clock_screen = CreateDisplay()
        self.time_and_date = RetrieveDateAndTime()
        self.weather = RetrieveLocationBasedWeatherInfo()

        self.ctr = 0
        self.weather_dict = {}

    ''' 
    Utility method that prepares the UI view with data that needs to be displayed. It takes the weather & possibly 
    location parameters and based on the screen size formats the the text size & placement position.
    @:param - weather_dict -> {desc_condition : str, current_temp: float, icon_id: str}
    '''
    def clock_face(self, weather_dict):
        # create a new image - Basically a transparent background for adding an icon later
        img = Image.new('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK_TRANSPARENT)
        img_w, img_h = img.size

        # build the fonts
        font_size_time = int(img_h / 6)
        time_font = self.clock_screen.build_font(font_size_time)

        font_size_date = int(img_h / 9)
        date_font = self.clock_screen.build_font(font_size_date)

        font_size_weather = int(img_h / 12)
        weather_font = self.clock_screen.build_font(font_size_weather)

        # Build a drawing context
        kntxt = Image.new('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK_TRANSPARENT)
        drawing_context = self.clock_screen.build_context(kntxt)

        time_text = self.time_and_date.fetch_time()
        time_w, time_h = self.clock_screen.measure_text(time_font, time_text.upper(), drawing_context)

        date_text = self.time_and_date.fetch_date()
        date_w, date_h = self.clock_screen.measure_text(date_font, date_text, drawing_context)

        weather_text = "{} | {}".format(weather_dict['general_temperature'], weather_dict['desc_cond'])
        weather_w, weather_h = self.clock_screen.measure_text(weather_font, weather_text, drawing_context)

        weather_icon = self.clock_screen.resize_icons(weather_dict['icon_id'], font_size_time)
        icon_x, icon_y = int((img_w - weather_icon.width) / 2), int(
            (time_h + date_h + weather_h + weather_icon.height)*1.1)

        # Border Padding: in-case its needed
        vertical_padding = int(time_h / 10)
        horizontal_padding = int(date_w / 5)

        # Actual Text Drawing on the canvas takes place below
        drawing_context.text(((img_w - time_w) / 2, (time_h - vertical_padding)),
                             time_text.upper(), font=time_font, fill=WHITE_TRANSPARENT, padx=5)

        drawing_context.text(((img_w - date_w) / 2, ((time_h + date_h) * 1.15)),
                             date_text, font=date_font, fill=WHITE_TRANSPARENT, padx=5)

        drawing_context.text(((img_w - weather_w) / 2, ((time_h + date_h + weather_h) * 1.2)),
                             weather_text, font=weather_font, fill=WHITE_TRANSPARENT, padx=5)

        kntxt.paste(weather_icon, (icon_x, icon_y))
        final_media = Image.alpha_composite(img, kntxt)
        img.close(), kntxt.close()

        return final_media

    '''
    Driver Method for Getting Location Based Weather. This method might have to be refactored when adding capabilities
    to the clock such as Alarm, Music etc etc. Also when the clock makes DB inserts in later revisions.
    '''
    def start_clock(self):
        while True:
            if self.ctr == 0 or self.ctr >= TWENTY_MINS:
                lat, lon = self.weather.get_location()
                self.weather_dict['desc_cond'], self.weather_dict['general_temperature'], self.weather_dict[
                    'icon_id'] = self.weather.get_weather(lat, lon)
                self.ctr = 0
            self.ctr += 1

            img_obj = self.clock_face(self.weather_dict)
            self.clock_screen.display_information(img_obj)
            time.sleep(FIVE_SEC_DELAY)
