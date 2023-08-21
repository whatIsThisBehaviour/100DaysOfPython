def is_leap_year(year):
    """Check whether the year is leap year"""
    if year % 4 == 0:
        return True
        if year % 100 == 0:
            return False
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def days_in_month(year, month):
    # Docstrings are used to add the description of the functionality to our function. It is declared right 
    # after the function is declared.
    """Counts the number of days in a month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Vague Input."
    if is_leap_year(year) and month == 2:
        return 29
    return month_days[month-1]

year = int(input("Enter the YEAR : "))
month = int(input("Enter the MONTH : "))
days = days_in_month(year, month)
print(days)
