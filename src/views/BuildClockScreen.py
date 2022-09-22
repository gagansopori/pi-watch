from PIL import Image

from src.constants.GenericConstants import degree_symbol
from src.configurations.CreateDisplayElements import CreateDisplay
from src.constants.DisplayConstants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK_TRANSPARENT, WHITE_TRANSPARENT


class BuildClockScreen:
    def __init__(self):
        self.create_display = CreateDisplay()

    def clock_face(self, weather_data, current_time):
        """
        Utility method that prepares the UI view with data that needs to be displayed. It takes the weather & possibly
        location parameters and based on the screen size formats the text size & placement position.
        @:param - weather_dict -> {desc_condition : str, current_temp: float, icon_id: str}
        """
        # Border Padding: in-case its needed
        vertical_padding = 25
        horizontal_padding = 5

        # create a new image - Basically a transparent background for adding an icon later
        img = Image.new('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK_TRANSPARENT)
        img_w, img_h = img.size

        # Build a drawing context
        kntxt = Image.new('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK_TRANSPARENT)
        drawing_context = self.create_display.build_context(kntxt)

        # build the fonts & texts
        # time
        font_size_time = int(img_h / 5)
        time_font = self.create_display.build_font(font_size_time)
        time_text = f"{current_time.hour}:{current_time.minute} {current_time.meridian}"
        time_w, time_h = self.create_display.measure_text(time_font, time_text.upper(), drawing_context)

        # date
        font_size_date = int(img_h / 7)
        date_font = self.create_display.build_font(font_size_date)
        date_text = f"{current_time.weekday_name}, {current_time.month_of_year} {current_time.day_of_month}"
        date_w, date_h = self.create_display.measure_text(date_font, date_text, drawing_context)

        # weather
        font_size_weather = int(img_h / 9)
        weather_font = self.create_display.build_font(font_size_weather)
        weather_text = f"{weather_data.general_temperature:.0f}{degree_symbol} | {weather_data.condition_description}"
        weather_w, weather_h = self.create_display.measure_text(weather_font, weather_text, drawing_context)

        # wind
        # wind_text = f"{weather_data.wind_speed:.0f}"

        # build the icons
        # weather
        weather_icon = self.create_display.resize_icons(weather_data.icon_id, (font_size_time + vertical_padding))
        weather_icon_x, weather_icon_y = int((img_w - weather_icon.width) / 2), int((vertical_padding + time_h + date_h
                                                                                     + weather_h))

        # wind
        # wind_icon = self.clock_screen.resize_icons('North', font_size_time).rotate(180)
        # wind_icon_x, wind_icon_y = int((horizontal_padding + weather_icon_x + weather_icon.width)), int((vertical_padding + time_h) * 1.1)

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

        self.create_display.display_information(final_media)
