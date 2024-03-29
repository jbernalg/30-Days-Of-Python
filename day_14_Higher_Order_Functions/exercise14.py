# -------------------Exercise Higher Order Function----------------------

# Explain the difference between map, filter and reduce
# map function applies the function passed as a parameters over all the items of the list. It return a iterable
# filter function allows you to filter the items of the list  by means of a function. Iy return a iterable
# reduce function applies the function passed as a parameters  over all the items and return a single value

# Explain the difference between higher order function, closure and decorator
# The Higher Order Function is a function that operates with another function or functions.
# It contains other functions as input parameters or it return a function as output.
# Closures are internal functions that are enclosed  within the external function.
# It can access variables present in the scope of the external function
# Decorator allows to add new functionality to an existing object without modifying its structure

from itertools import count
from ntpath import join


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list
def uppercase_word(word):
    return word.upper()

countries_upper = list(map(uppercase_word, countries))
print(countries_upper )

# Use map to create a new list by changing each number to its square in the numbers list
def square(num):
    return num**2

number_square = map(square, numbers)
print(list(number_square))

# Use map to change each name to uppercase in the names list
names_upper = map(uppercase_word, names)
print(list(names_upper))

# Use filter to filter out countries containing 'land'
def is_land(country):
    if 'land' in country:
        return True
    else:
        return False

countries_filter = filter(is_land, countries)
print(list(countries_filter))

# Use filter to filter out countries having exactly six characters
def long_names(country):
    if len(country) == 6:
        return True
    else: 
        return False

countries_filter = filter(long_names, countries)
print(list(countries_filter))

# Use filter to filter out countries containing six letters and more in the country list.
def long_name2(country):
    if len(country) >= 6:
        return True
    else:
        return False

countries_filter2 = filter(long_name2, countries)
print(list(countries_filter2))

# Use filter to filter out countries starting with an 'E'
def initial_country(country):
    if country[0] == 'E':
        return True
    else:
        return False

countries_filter3 = filter(initial_country, countries)
print(list(countries_filter3))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lista):
    if isinstance(lista, str):
        return True
    else:
        return False

elementos = [1, 'hola', 1.14, 'Adios']
result = filter(get_string_lists, elementos)
print(list(result))

# Use reduce to sum all the numbers in the numbers list.
from functools import reduce

def sum_all_numbers(a, b):
    return a + b

sum_total = reduce(sum_all_numbers, numbers)
print(sum_total)

# Finding the minimum and maximum value of the number list with reduce
def func_min(a, b):
    return a if a < b else b

def func_max(a, b):
    return a if a > b else b

print('The Minimum is: ',reduce(func_min, numbers))
print('The Maximum is: ', reduce(func_max, numbers))

# Checking if all values are true
def both_true(a, b):
    return bool(a and b)

lista1 = [1,4,0,2,13]
lista2 = [1,1,2,2,3,4]

print(reduce(both_true, lista1))
print(reduce(both_true, lista2))

# Checking if any value is true
def any_true(a, b):
    return bool(a or b)

lista3 = [0,0,1,0,0,0]
print(reduce(any_true, lista3))

# Multiply the elements of the numbers list 
product = reduce(lambda x,y: x*y, numbers)
print(product)

  
