import datetime
from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        r = datetime.date(year,month, day)
        return r.strftime("%A")

