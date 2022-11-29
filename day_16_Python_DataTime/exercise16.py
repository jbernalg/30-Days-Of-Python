#-------------------Datetime---------------------

# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

print(day, month, year, hour, minute, second)
print('timestamp', timestamp)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = now.strftime('%m/%d/%Y, %H:%M:%S')
print(t)

# Today is 5 December, 2019. Change this time string to time.
date_string = '5 December, 2019'

date_object = datetime.strptime(date_string, '%d %B, %Y')
print('date: ', date_object)

# Calculate the time difference between now and new year.
from datetime import date

today = date(year=2022, month=8, day=27)
new_year = date(year=2023, month=1, day=1)

time_left_for_new_year = new_year - today
print(time_left_for_new_year)

# Calculate the time difference between 1 January 1970 and now.
other_day = date(year=1970, month=1, day=1)

difference_between_two_year = today - other_day
print(difference_between_two_year)