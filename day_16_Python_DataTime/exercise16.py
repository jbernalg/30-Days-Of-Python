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