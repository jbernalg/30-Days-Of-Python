#--------------Python error type--------------------

#--------------SyntaxError---------------
# print 'hello word'
#--> SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello word')?
# we forgot to enclose the string with parenthesis and Python already suggests the solution. Let us fix it.

#--------------NameError------------------
# print(age)
# NameError: name 'age' is not defined
# The type of error was a NameError. We debugged the error by defining the variable name.

#--------------IndexError----------------
number = [1,2,3,4,5]
# print(number[5])
# IndexError: list index out of range
#  Python raised an IndexError, because the list has only indexes from 0 to 4 , so it was out of range.

#-------------ModuleNotFoundError--------------
# import maths
# ModuleNotFoundError: No module named 'maths'
# I added an extra s to math deliberately and ModuleNotFoundError was raised.

#-------------AttributeError---------------
import math
# print(math.PI)
# AttributeError: module 'math' has no attribute 'PI'
#  It raised an attribute error, it means, that the function does not exist in the module. Lets fix it by changing from PI to pi.

#-------------KeyError--------------
users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])
# print(users['county'])
# KeyError: 'county'
# there was a typo in the key used to get the dictionary value.

#------------TypeError-------------
# print(4 + '3')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# a TypeError is raised because we cannot add a number to a string

#------------ValueError------------
# print(int('a12'))
# ValueError: invalid literal for int() with base 10: 'a12'
# In this case we cannot change the given string to a number, because of the 'a' letter in it.

#------------ZeroDivisionError-------------
# print(1/0)
# ZeroDivisionError: division by zero
