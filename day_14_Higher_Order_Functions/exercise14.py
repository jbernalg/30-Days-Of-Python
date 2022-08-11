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