#---------Exercise List Comprehension-----------

#Filter only negative and zero in the list using list comprehension
from operator import is_, le
import re
from tkinter import Y
from turtle import st


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_numbers = [i for i in numbers if i <= 0]
print(filter_numbers)

#Flatten the following list of lists of lists to a one dimensional list :
#[number for row in list_of_list for number in row]
list_of_list =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list = [number for row in list_of_list for number in row]
new_list2 = [number for row in new_list for number in row]
print(new_list2)

# Find all of the numbers from 1-100 that are divisible by 7
div7 = [n for n in range(1,100) if n % 7 == 0]
print(div7)

# Find all of the numbers from 1-100 that have a 3 in them
num_3 = [x for x in range(1, 100) if '3' in str(x)]
print(num_3)

# Count the number of spaces in a string
stringN = 'hello How are you? fine'
space = [s for s in stringN if s == ' ']
print(len(space))

# Consonants in a string: 
# Create a list of all the consonants in the string "Yellow Yaks like yelling and 
# yawning and yesturday they yodled while eating yuky yams"
sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = [letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(consonants)

# Get index and value from list
# Get the index and the value as a tuple for items in the list ["hi", 4, 8.99, 'apple', ('t,b','n')].  
# Result would look like [(index, value), (index, value)]
list1 = ["hi", 4, 8.99, 'apple', ('t,b','n')]
result = [(index, item) for index, item in enumerate(list1)]
print(result)

# Find common numbers in two lists of numbers
list_a = [1,2,3,4]
list_b = [2,3,4,5]
common = [n for n in list_a if n in list_b]
print(common)

# Find numbers in sentence
# Get only the numbers in a sentence like 'In 1984 there were 13 instances 
# of a protest with over 1000 people attending'.
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
word = sentence.split()
numbers = [n for n in word if not n.isalpha()]
print(numbers) 

# Determine even or odd in list of numbers
# Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even, and the word 'odd' if the number is odd.  
# Result would look like ['odd','odd', 'even']
result = ['even' if n % 2 == 0 else 'odd' for n in range(10)]
print(result)

# Common number tuples
# Produce a list of tuples consisting of only the matching numbers in these lists .  
# Result would look like (4,4), (12,12)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
list_b = [2, 7, 1, 12]

result = [(a, b) for a in list_a for b in list_b if a == b]
print(result)

# Find words with more than 4 letters
# Find all of the words in a string that are less than 4 letters
sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
examine = sentence.split()
result = [n for n in examine if len(n) >= 4]
print(result)

# Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)
result = [n for n in range(1,100) if True in [True for x in range(2,10) if n % x  == 0]]
print(result)

# Create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and print the result
op = lambda x: x + 15
print(op(10))

mult = lambda x,y: x*y 
print(mult(2,3))

# create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def multiplo(n):
    return lambda x: x*n

result = multiplo(2)
print('Double the number of 15:',result(15))
result = multiplo(3)
print('Triple the number of 15:',result(15))
result = multiplo(4)
print('Quadruple the number of 15:',result(15))
result = multiplo(5)
print('Quiintuple the number of 15:',result(15))

# Write a Python program to sort a list of tuples using Lambda.
#sort by number
items = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
items.sort(key = lambda x: x[1])
print(items)

#sort by name
items_sort = sorted( items, key = lambda x: x[0])
print(items_sort)

# Write a Python program to sort a list of dictionaries using Lambda. 
#sort by color
cellphone = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
             {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
             {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_cellphone = sorted(cellphone, key = lambda x: x['color'])
print(sorted_cellphone)

# Write a Python program to filter a list of integers using Lambda. 
# Filter function: can be used to create a new iterator from an existing iterable (such as a list or dictionary) 
# that will efficiently filter items using a function that we provide
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, list_numbers)) 
print(even)
odd = list(filter(lambda x: x % 2 != 0, list_numbers))
print(odd)

# Filter names starting with a vowel in a given list
names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']

def name_vowels(x):
    return x[0].lower() in 'aeiou'

filtered_name = list(filter(name_vowels, names))
print(filtered_name)

# Write a Python program to square and cube every number in a given list of integers using Lambda.
# map funciton: used to apply a function to each element in an iterable (such as a list or a dictionary) 
# and return a new iterator to retrieve the results.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_number = list(map(lambda x: x**2, numbers))
print(square_number)

cube_numbers = list(map(lambda x: x**3, numbers))
print(cube_numbers) 

# Write a Python program to find if a given string starts with a given character using Lambda.
# The startswith() method returns True if a string starts with the specified prefix(string). If not, it returns False.
start_with = lambda x: True if x.startswith('P') else False
print(start_with('Python'))

# Write a Python program to extract year, month, date and time using Lambda. 
import datetime
now = datetime.datetime.now()
print(now)

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

# Write a Python program to check whether a given string is number or not using Lambda
is_num = lambda x: x.replace('.', '',1).isdigit()  #type string
print(is_num('123'))
print(is_num('4.281'))
print(is_num('hola mundo.'))

# Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
# takes as an argument a set of values ​​(a list, a tuple, or any iterable object) and "reduces" it to a single value
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1])
print(fib_series(5)) 

# Write a Python program to find intersection of two given arrays using Lambda.
list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9, 14, 15, 16]

result = list(filter(lambda x: x in list1, list2))
print(result)

# Write a Python program to rearrange positive and negative numbers in a given array using Lambda
list_numbers = [-1, 2, -3, 5, 7, 8, 9, -10]
result = sorted(list_numbers, key = lambda i: 0 if i == 0 else -1/i)
print(result)

