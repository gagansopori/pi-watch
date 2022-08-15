class SystemDateAndTimeModel:
    def __init__(self):
        # time parameters
        self._hour: int = 00
        self._minute: int = 00
        self._seconds: int = 00
        self._meridian: str = 'AM'

        # date parameters
        self._day_of_month: int = 11
        self._month_of_year: str = 'Dec'
        self._weekday_name: str = 'Fri'

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hr):
        self._hour = hr

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, mm):
        self._minute = mm

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, sec):
        self._seconds = sec

    @property
    def meridian(self):
        return self._meridian

    @meridian.setter
    def meridian(self, mer):
        self._meridian = mer

    @property
    def day_of_month(self):
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, dom):
        self._day_of_month = dom

    @property
    def month_of_year(self):
        return self._month_of_year

    @month_of_year.setter
    def month_of_year(self, moy):
        self._month_of_year = moy

    @property
    def weekday_name(self):
        return self._weekday_name

    @weekday_name.setter
    def weekday_name(self, dow):
        self._weekday_name = dow
