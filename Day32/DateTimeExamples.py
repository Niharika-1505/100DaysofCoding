import datetime as dt

current_date = dt.datetime.now()
print(current_date)
print(current_date.weekday(), current_date.month, current_date.year, current_date.time())
date_of_birth = dt.datetime(year=2021, month=12, day=6)
print(date_of_birth.weekday())
