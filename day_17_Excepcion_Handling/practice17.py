# ------------------Exception Handling---------------------
'''
Python uses try and except to handle errors gracefully The cause of an exception 
is often external to the program itself. Por example: incorrect input, wrong file name, 
unable to find a file, malfuntioning IO device
Graceful handling of errors prevents our applications from crashing. 

syntax

try:
  {run this code}
except:
  {Execute this code when there is an exception}
else:
  {No exception? execute this code}
finally:
  {Always run this code}
'''

from pickletools import read_string1
from platform import java_ver

#### example 1:
# funcion que suma dos numeros
def sumas_dos():
    
    while True:
        a = input('Numero 1: ')
        b = input('Numero 2: ')
        try:
            result = int(a) + int(b)
        except:
            print('Ingresa un valor correcto')
        else:
            break
    return result
'''
print(sumas_dos())
Numero 1: 3
Numero 2: 2
5
'''
'''
print(sumas_dos())
Numero 1: hola
Numero 2: 2
Ingresa un valor correcto
Numero 1: 
'''

#### example 2:
# funcion nombre edad
def name_age():
    try:
        name = input('Enter your name: ')
        year_born = input('year you were born: ')
        age = 2022 - int(year_born)

        if name.isalpha() and type(age) == int:    
            print(f'You are {name}. And you age is {age}')
    except:
        print('Something went wrong')
'''
name_age()
Enter your name: jose
year you were born: 1990
You are jose. And you age is 32 
'''

'''
Enter your name: jose
year you were born: jose
Something went wrong
'''

#### example 3:
# funcion name_age2
def name_age2():
    try:
        name = input('Enter your name: ')
        if name.isalpha() == False:
            raise TypeError
        
        year_born = input('year you were born: ')
        age = 2022 - int(year_born)
        print(f'You are {name}. And you age is {age}')
    
    except TypeError:
        print('Type error occured')
    
    except ValueError:
        print('Value error occured')
    
    except ZeroDivisionError:
        print('zero division error occured')
'''
name_age2()
Enter your name: 23
Type error occured
'''

#### example 4:
def name_age3():
    try:
        name = input('Enter your name: ')
        if name.isalpha() == False:
            raise ValueError
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
'''
name_age3()
Enter your name: Daniel
year you were born: 2002
You are Daniel. And you age is 20
I usually run with the try block
I always run
'''

'''
name_age3()
Enter your name: Jose
year you were born: j
Value error occured
I always run
'''

##### it shorted the above code
def name_age4():
    try:
        name = input('Enter your name: ')
        year_born = input('year you were born: ')
        age = 2022 - int(year_born)
        print(f'You are {name}. And you age is {age}')
    except Exception as e:
        print(e)

'''
name_age4()
Enter your name: miguel
year you were born: 1979
You are miguel. And you age is 43
'''

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

#-----------------Spreading in Python--------------------
lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0, *lst_one, *lst_two]
print(lst)

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)


#-----------------Enumerate--------------------
# we use enumerate function to get  the index  of each  item  in the list
for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(nordic_countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

# ----------------Zip---------------------
# Sometime we would like to combine lists when looping through them.
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)