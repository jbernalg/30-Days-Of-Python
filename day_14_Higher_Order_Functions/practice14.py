# -------------------Higher Order Functions-------------------
# In python you can do the following operations with functions:
# - A function can take one or more functions as parameters
# - A function can be returned as a result of another function
# - A function can be modified
# - A function can be assigned to a variable

#function as a parameter
def sum_numbers(nums):
    return sum(nums) #a funtion abusing the built-in sum function

lista = [1,4,5,2,6]
print(sum_numbers(lista)) 

def high_order_function(f, lst): #concatenation of functions
    summation = f(lst)
    return summation

result = high_order_function(sum_numbers, [1,3,5,7])
print(result)

# Function as a return value: the higher order function is returning different functions depending on the passed parameter
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

# Python Closures
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