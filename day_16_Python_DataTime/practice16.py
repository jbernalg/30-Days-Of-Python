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

#-----------Formating Date Output using strftime------------
new_year = datetime(2022, 1, 1) #add datetime
print(new_year)

day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second

print(day, month, year, hour, minute)

#current date and time
now = datetime.now()

# H:M:S format
t = now.strftime('%H:%M:%S')
print('time: ', t)

# mm/dd/YY H:M:S format
time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print('time one: ', time_one)

# dd/mm/YY H:M:S format
time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
print('time two: ', time_two)

#----------------String to time using strptime-----------------
date_string = '26 August, 2022'
print('date string =' ,date_string)

date_object = datetime.strptime(date_string, '%d %B, %Y')
print('date object = ', date_object)

#---------------Using date from datetime----------------
from datetime import date
d = date(2022, 1, 1) #show date
print(d)

#current day
print('current date: ', d.today())

#date object of today's date
today = date.today()
print('current year: ', today.year)
print('current month: ', today.month)
print('current day : ', today.day)

#--------------Time objects to represent time-------------
from datetime import time

#time (H=0, M=0, S=0)
a = time()
print(a)

#time(hour, minute, second)
b = time(10, 30, 50)
print(b)

#time(hour, minute, second)
c = time(hour=12, minute=23, second= 48)
print(c)

#time(hour, minute, second, microsecond)
d = time(8, 10, 22, 23142)
print(d)

