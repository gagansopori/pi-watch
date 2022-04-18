import time as Time


class RetrieveDateAndTime:
    def __init__(self):
        self.time_text: str = 'Fetching Time...'
        self.date_text: str = 'Fetching Date...'

    def fetch_time(self) -> str:
        # %H for 24hr
        hour = Time.strftime('%I')
        minute = Time.strftime('%M')
        meridian = Time.strftime('%p')
        self.time_text = ("{}:{} {}".format(hour, minute, meridian))

        return self.time_text

    def fetch_date(self) -> str:
        day_of_month = Time.strftime('%d')
        # %B for full Month name | %m for Month as a number (1,12)
        month_of_year = Time.strftime('%b')
        # %A for full Weekday Name
        weekday_name = Time.strftime('%a')
        self.date_text = ("{}, {} {}".format(weekday_name, month_of_year, day_of_month))

        return self.date_text
