dayslist = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
    ]

def is_leap(year):
    if year%4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def no_of_days(month, year):
    number_of_days = 0
    if month == 1:
        m_limit = 12
        y_limit = year-1
    else:
        m_limit = month - 1
        y_limit = year
    for y in range(1900, y_limit+1):
        for m in range(1, 13):
            if y == y_limit and m > m_limit:
                break
            if m == 2:
                if is_leap(y):
                    number_of_days += 29
                else:
                    number_of_days += 28
            elif m in (4, 6, 9, 11):
                number_of_days += 30
            else:
                number_of_days += 31
    return number_of_days

def get_first_day(month, year, dayslist):
    number_of_days = no_of_days(month, year)
    eff_num = number_of_days % 7
    return dayslist[eff_num]

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if get_first_day(month, year, dayslist) == dayslist[6]:
            count += 1
print count
