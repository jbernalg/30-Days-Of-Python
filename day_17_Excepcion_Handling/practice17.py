# ------------------Exception Handling---------------------

# Python uses try and except to handle errors gracefully
# The cause of an exception is often external to the program itself. Por example:
# incorrect input, wrong file name, unable to find a file, malfuntioning IO device
# Graceful handling of errors prevents our applications from crashing. 

# syntax
# try:
#   {run this code}
# except:
#   {Execute this code when there is an exception}
# else:
#   {No exception? execute this code}
# finally:
#   {Always run this code}

# example 1:
try:
    print(10 + '5')
except:
    print('Something went wrong')

# example 2:
try:
    name = input('Enter your name: ')
    year_born = input('year you were born: ')
    age = 2022 - year_born
    print(f'You are {name}. And you age is {age}')
except:
    print('Something went wrong')