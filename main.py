"""
@author: Gagan Sopori
"""
from application.controller.MainController import MainController


def main():
    pimoroni = MainController()
    pimoroni.start_clock()


if __name__ == '__main__':
    main()



# from ST7789 import ST7789
# from gpiozero import Button
# from PIL import Image, ImageDraw, ImageFont
# from states.clock import ClockState
# import time
#
# class ClockRadioApp:
#     def __init__(self):
#         self.disp = ST7789(port=0, cs=0, dc=9, backlight=13, spi_speed_hz=80_000_000)
#         self.width = self.disp.width
#         self.height = self.disp.height
#         self.image = Image.new("RGB", (self.width, self.height))
#         self.draw = ImageDraw.Draw(self.image)
#         self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
#
#         self.buttons = {
#             'A': Button(5),
#             'B': Button(6),
#             'X': Button(16),
#             'Y': Button(24),
#         }
#         self.button_callbacks = {}
#
#         self.state = None
#         self.change_state(ClockState(self))
#
#     def set_button_callback(self, name, callback):
#         self.buttons[name].when_pressed = callback
#         self.button_callbacks[name] = callback
#
#     def change_state(self, new_state):
#         if self.state:
#             self.state.exit()
#         self.state = new_state
#         self.state.enter()
#
#     def display_clock(self):
#         now = time.localtime()
#         self.draw.rectangle((0, 0, self.width, self.height), fill=(0, 0, 0))
#         time_str = time.strftime("%H:%M:%S", now)
#         date_str = time.strftime("%a, %b %d", now)
#         self.draw.text((10, 30), time_str, font=self.font, fill=(255, 255, 255))
#         self.draw.text((10, 70), date_str, font=self.font, fill=(200, 200, 200))
#         self.disp.display(self.image)
#
#     def display_radio_channel(self, url):
#         self.draw.rectangle((0, 0, self.width, self.height), fill=(0, 0, 50))
#         self.draw.text((5, 30), "Radio", font=self.font, fill=(255, 255, 0))
#         self.draw.text((5, 70), url[:28], font=self.font, fill=(180, 180, 180))
#         self.disp.display(self.image)
#
#     def run(self):
#         while True:
#             time.sleep(1)
#             self.state.update()
#
# if __name__ == '__main__':
#     app = ClockRadioApp()
#     app.run()
