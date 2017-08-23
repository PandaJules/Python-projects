import calendar
from datetime import datetime, date


def time_conversion(t):
    """
    Convert AM/PM format to 24hr format
    """
    if t[8] == "P" and t[:2] != "12":
            t = str(int(t[:2])+12) + t[2:]
    if t[8] == "A" and t[:2] == "12":
            t = "00" + t[2:]
    return t[:-2]


def calendar_for_year(year):
    print(calendar.TextCalendar(firstweekday=0).formatyear(year))


def what_day_was_it(day, month, year):
    print(calendar.day_name[calendar.weekday(year, month, day)])


def various_date_formats():
    print(datetime.now())
    print(date.today())
    print(date(2002, 12, 4).ctime())
