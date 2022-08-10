# -------------------Higher Order Functions-------------------
# In python you can do the following operations with functions:
# - A function can take one or more functions as parameters
# - A function can be returned as a result of another function
# - A function can be modified
# - A function can be assigned to a variable

#--------------------------function as a parameter-------------------------------
def sum_numbers(nums):
    return sum(nums) #a funtion abusing the built-in sum function

lista = [1,4,5,2,6]
print(sum_numbers(lista)) 

def high_order_function(f, lst): #concatenation of functions
    summation = f(lst)
    return summation

result = high_order_function(sum_numbers, [1,3,5,7])
print(result)

# ----------------------Function as a return value----------------------------- 
# the higher order function is returning different functions depending on the passed parameter
def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('absolute')
print(result(-3))

# --------------------------Python Closures---------------------------------
# Python allows a nested function to access the outer scope of the enclosing function. 
# Closure is created by nesting a function inside another encapsulating function and 
# then returning the inner function. See the example below.
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(23))

# ------------------------Python Decorators---------------------------
# A decorator is a design pattern in Python that allows a user to add new functionality 
# to an existing object without modifying its structure. 
# Decorators are usually called before the definition of a function you want to decorate.

#---------------------- Creating Decorators --------------------------
# To create a decorator function, we need an outer function with an inner wrapper function.
def greeting(): #normal function
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())

# Let us implement with a decorator
def uppercase_decorator2(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting2():
    return 'Welcome to Python'

print(greeting2())

# -----------------Applying multiple decorators to a single function--------------------
# First decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())

# -----------------Accepting parameters in decorator functions--------------------
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1,para2,para3):
        function(para1,para2,para3)
        print('I live in {}'.format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name,country):
    print('I am {} {}. I love to teach.'.format(first_name, last_name, country))

print_full_name('Jeinfferson', 'Bernal', 'Venezuela')

# -------------------Built in Higher order functions---------------------
# ----------------------------map function------------------------------------- 
# is a built-in function that takes a function and iterable as parameters
# syntax: map(function, iterable)

#example: 1
numbers = [1,2,3,4,5]

def square(x):
    return x**2

numbers_square = list(map(square, numbers))
print(numbers_square)

#example 2:
numbers_str = ['1','2','3','4','5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

#example 3:
names = ['Gabriel', 'Lily', 'Ermes', 'Abraham']

def change_to_upper(name):
    return name.upper()

name_upper_cased = map(change_to_upper, names)
print(list(name_upper_cased))

#example 4: Let us apply it with lambda function
name_upper_cased = map(lambda name: name.upper(), names)
print(list(name_upper_cased))

# -------------------------Filter function------------------------------
# calls the specified function which return boolean for each item of the specified iterable (list)
# syntax: filter(function, iterable)

#example 1: Lets filter only even numbers
numbers = [1,2,3,4,5,6,7,8,9]

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

#example 2: Lets filter only odd numbers
numbers = [1,4,6,10,11]

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))