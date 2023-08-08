age = int(input("Enter your age : "))
# this project has following constants,
# assumes every individual is lucky enough to live for 85 years.
# week count is 52 a year, days count is 365 days a year.
year_remaining = 85 - age
months_remaining = year_remaining * 12
weeks_remaining = year_remaining * 52
days_remaining = year_remaining* 365
hours_remaining = days_remaining*24
minutes_remaining = hours_remaining*60
seconds_remaining = minutes_remaining*60
remaining_days_in_life = print(f"You have {year_remaining} years remaining, {months_remaining} months left, {weeks_remaining} weeks left, {days_remaining} days left, {hours_remaining} hours left, {minutes_remaining} minutes left, {seconds_remaining} seconds left. Make them count valuable")