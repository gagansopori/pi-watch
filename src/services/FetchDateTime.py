import time as Time

from src.model.DateTimeModel import SystemDateAndTimeModel


class RetrieveDateAndTime:
    def __init__(self):
        self.current_time = SystemDateAndTimeModel()
        self.time_text: str = 'Fetching Time...'
        self.date_text: str = 'Fetching Date...'

    def fetch_time(self) -> str:
        # %H for 24hr
        self.current_time.hour = Time.strftime('%I')
        self.current_time.minute = Time.strftime('%M')
        self.current_time.meridian = Time.strftime('%p')
        self.time_text = f"{self.current_time.hour}:{self.current_time.minute} {self.current_time.meridian}"

        return self.time_text

    def fetch_date(self) -> str:
        self.current_time.day_of_month = Time.strftime('%d')
        # %B for full Month name | %m for Month as a number (1,12)
        self.current_time.month_of_year = Time.strftime('%b')
        # %A for full Weekday Name
        self.current_time.weekday_name = Time.strftime('%a')
        self.date_text = f"{self.current_time.weekday_name}, {self.current_time.month_of_year} {self.current_time.day_of_month}"

        return self.date_text
