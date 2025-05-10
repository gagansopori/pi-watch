#This classs will have the View Elements
# 1. Blank Screen & a method that displays data on the screen
# 2. A,B,X,Y Buttons
from PIL import Image

from application.constants.DisplayConstants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK_TRANSPARENT


class ParentView:
    def __init__(self):
        # create a new image - Basically a transparent background for adding an icon later
        self._img = Image.new('RGBA', (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK_TRANSPARENT)
        # self._drawing_context =
        # img_w, img_h = img.size
