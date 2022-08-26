#-------------Python datetime------------
import datetime
print(dir(datetime))
# With dir or help built-in commands it is possible to know the available functions in a certain module
# we will focus on date, datetime, time and timedelta

#-------------Getting datetime information------------
from datetime import datetime
now = datetime.now()
print(now) # show datetime right now

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()  #  timestamp is the number of seconds elapsed from 1st of January 1970 

print(day, month, year, hour, minute)
print(timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')