# Exercise 11
'''
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
'''
#print(abs.__doc__)
#print(print.__doc__)
#print(property.__doc__)


# Exercise 12
'''
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module
'''
import calendar

year = int(input('Ingrese el año: '))
month = int(input('Ingrese el numero de mes: '))

print(calendar.month(year, month))

