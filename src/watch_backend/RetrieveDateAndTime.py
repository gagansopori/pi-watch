import time as Time


class RetrieveDateAndTime:
    def __init__(self):
        self.time_text = 'Fetching Time...'
        self.date_text = 'Fetching Date...'

    def fetch_time(self):
        hour = Time.strftime('%I')
        minute = Time.strftime('%M')
        meridian = Time.strftime('%p')

        self.time_text = ("%s:%s %s" % (hour, minute, meridian))

        return self.time_text

    def fetch_date(self):
        day_of_month = Time.strftime('%d')
        month_of_year = Time.strftime('%b')
        day_of_week = Time.strftime('%a')

        self.date_text = ("%s, %s %s" %(day_of_week, month_of_year, day_of_month))

        return self.date_text
