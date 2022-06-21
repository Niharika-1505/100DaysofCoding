def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if is_leap(year):
            return month_days[month - 1] + 1
        else:
            return month_days[month - 1]
    else:
        return month_days[month - 1]


years = int(input("Enter a year: "))
months = int(input("Enter a month in number format: "))
days = days_in_month(years, months)
print(days)
