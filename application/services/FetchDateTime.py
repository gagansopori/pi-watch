import time as Time

from application.model.DateTimeModel import SystemDateAndTimeModel


class RetrieveDateAndTime:
    def __init__(self):
        self.current_time = SystemDateAndTimeModel()

    def fetch_time(self) -> SystemDateAndTimeModel:
        # %H for 24hr
        self.current_time.hour = Time.strftime('%I')
        self.current_time.minute = Time.strftime('%M')
        self.current_time.meridian = Time.strftime('%p')

        self.current_time.day_of_month = Time.strftime('%d')
        # %B for full Month name | %m for Month as a number (1,12)
        self.current_time.month_of_year = Time.strftime('%b')
        # %A for full Weekday Name
        self.current_time.weekday_name = Time.strftime('%a')

        return self.current_time
