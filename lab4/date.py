import datetime

# 1 Write a Python program to subtract five days from current date.
def subtract_days(days: int):
    return datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp() - (days * 24 * 60 * 60))
# print(subtract_days(5))

# 2 Write a Python program to print yesterday, today, tomorrow.
def get_range_dates(n: int):
    return [subtract_days(i) for i in range(n, 0, -1)] + [subtract_days(0)] + [subtract_days(-i) for i in range(1, n+1)]
# print(get_range_dates(2))

# 3 Write a Python program to drop microseconds from datetime.
def yy_mm_dd_hh_mm_ss(date: datetime):
    format = "%Y-%m-%d %H:%M:%S"
    return date.strftime(format)
# print(yy_mm_dd_hh_mm_ss(datetime.datetime.now()))

# 4 Write a Python program to calculate two date difference in seconds.
def dates_diff(a: datetime, b: datetime):
    return a.timestamp() - b.timestamp()
# print(dates_diff(datetime.datetime(2024, 3, 5), datetime.datetime(2024, 3, 3)))
