import datetime as dt

current_date = dt.datetime.now()
print(current_date)
print(current_date.weekday(), current_date.month, current_date.year, current_date.time())
date_of_birth = dt.datetime(year=1995, month=5, day=15)
print(date_of_birth)
