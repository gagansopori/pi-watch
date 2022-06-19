import RPi.GPIO as GPIO

from src.watch_constants.BoardConstants import *


class CreateBoardControls:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def handle_action(self, pin):
        label = LABELS[BUTTONS.index(pin)]
        if pin == LABELS[BUTTONS.index(pin)]:
            print("Button press detected on pin: {} label: {}".format(pin, label))

        if label == 'A':
            print("Do Something for A")
        if label == 'B':
            print("Do Something for B")
        if label == 'X':
            print("Do Something for X")
        if label == 'Y':
            print("Do Something for Y")