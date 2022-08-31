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
from pickletools import read_string1
from platform import java_ver


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

# example 3:
try:
    name = input('Enter your name: ')
    year_born = input('year you were born: ')
    age = 2022 - year_born
    print(f'You are {name}. And you age is {age}')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# example 4:
try:
    name = input('Enter your name: ')
    year_born = input('year you were born: ')
    age = 2022 - int(year_born)
    print(f'You are {name}. And you age is {age}')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I usually run with the try block')
finally:
    print('I always run')

# it shorted the above code
try:
    name = input('Enter your name: ')
    year_born = input('year you were born: ')
    age = 2022 - int(year_born)
    print(f'You are {name}. And you age is {age}')
except Exception as e:
    print(e)

#----------------Packing and unpacking arguments in Python-------------------
# We use two operators:
# * for tuples
# ** for dictionaries

#----------------Unpacking------------------
# unpacking list
def sum_of_five_numbers(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]

print(sum_of_five_numbers(*lst))

# a list o tuple can also be unpacked like this:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, nor, sw, rest)

numbers = [1,2,3,4,5,6,7]
one, *middle, last = numbers
print(middle)


# unpacking dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Jose', 'country':'Colombia', 'city':'Medellin', 'age':30}
print(unpacking_person_info(**dct))

#---------------Packing--------------
# Sometimes we never know how many  arguments need to be passed to a python function.
# We can use the packing  method  to allow our function to take unlimited number or arbitrary number of arguments.

# Packing list
def sum_all(*arg):
    s = 0
    for i in arg:
        s += i
    return s

print(sum_all(1,2,3))
print(sum_all(5,2,8))

# Packing dictionaries
def packing_person_info(**kwargs):
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Javier",
      country="Finland", city="PAris", age=25))

