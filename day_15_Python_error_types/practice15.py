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

