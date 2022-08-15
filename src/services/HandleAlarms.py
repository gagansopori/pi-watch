import time as Time
import os

from src.watch_interfaces.CreateDisplayElements import CreateDisplay


class HandleAlarms:
    def __init__(self):
        self.alarm_Screen = CreateDisplay()


    def fetch_cpu(self):
        return

    def fetch_ip(self):
        stream_letters =  os.popen('hostname -I')
        print(stream_letters.read())
