import ST7789 as st7789
import os
from PIL import Image, ImageDraw, ImageFont

from src.watch_constants.DisplayConstants import *


class CreateDisplay:
    def __init__(self, *args, **kwargs):
        # setting up the spi display on Pirate Audio Board
        self.display = st7789.ST7789(port=0,
                                     cs=st7789.BG_SPI_CS_FRONT,
                                     dc=9,
                                     rst=25,
                                     backlight=13,
                                     width=240,
                                     height=240,
                                     rotation=90,
                                     spi_speed_hz=80 * 1000 * 100,
                                     offset_left=0,
                                     offset_top=0)
        self.display.begin()
        self.display.size = (self.display.width, self.display.height)

    def start(self):
        self.display.command(st7789.ST7789_DISPON)
        self.display.set_backlight(100)

    def stop(self):
        self.display.command(st7789.ST7789_DISPOFF)
        self.display.set_backlight(0)

    def build_font(self, text_h):
        # Toggle comments for linux vs windows
        # return ImageFont.truetype('D:/zz2/Oswald.ttf', text_h)
        return ImageFont.truetype('%s/pi-watch/src/resources/Oswald.ttf' % (os.getcwd()), text_h)

    def build_context(self, kntxt):
        return ImageDraw.Draw(kntxt)

    def measure_text(self, display_font, display_text, display_context):
        return display_context.textsize(display_text, font=display_font)

    # Toggle Comments if you're not running this on a Raspberry-Pi with an attached SPI display
    def display_information(self, img_obj):
        self.display.display(img_obj)

    # def display_information(self, img_obj):
    #     img_obj.show()
