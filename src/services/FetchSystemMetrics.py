import time as Time
import os

from src.constants.GenericConstants import cpu_temp_filepath
from src.configurations.CreateDisplayElements import CreateDisplay


def fetch_cpu_temp():
    cpu_temp_file = open(cpu_temp_filepath, "r")
    cpu_temp = cpu_temp_file.read()
    cpu_temp_file.close()
    return cpu_temp


class HandleAlarms:

    def fetch_cpu_percent(self):
        return

    def fetch_host_ip(self):
        stream_letters = os.popen('hostname -I')
        print(stream_letters.read())
