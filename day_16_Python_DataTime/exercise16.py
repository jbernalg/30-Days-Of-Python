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