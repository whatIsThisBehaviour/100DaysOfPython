is_leap_year = int(input("Check whether the year is leap or not : "))

if is_leap_year % 4 == 0:
    if is_leap_year % 100 == 0:
        # print(f"The year {is_leap_year} is Not a Leap Year.")
        if is_leap_year % 400 == 0:
            print(f"The year {is_leap_year} is a LEAP year.")
    else:
        print(f"The year {is_leap_year} is a LEAP Year.")
else:
    print(f"The year {is_leap_year} is not a leap year.")
