# ---------------- List Comprehension -------------------
# Is a compact way of creating a list from a sequence. It is a short way to create a new list 
# Is considerably faster than processing  a list using the for loop

# syntax
#[i for i in iterable if expression]

# if you want to change a string to a list of characters
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

# if you want to generate a list of numbers
numbers = [i for i in range(11)]
print(numbers)

# it is possible to do mathematical operations during iteration
square = [i * i for i in range(11)]
print(square)

# it is possible  to make a list of tuples
numbers_tuples = [(i, i * i) for i in range(11)]
print(numbers_tuples)

# list comprehension can be combined with if expression
# Generating  even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# Filter numbers:
numbers = [-8,-5,-4,-3,-1,0,2,4,6,7,8]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
flattened_list = [number for row in list_of_list for number in row]
print(flattened_list)

# ------------------- Lambda Function -----------------------
# is a small anonymous function without a name.
# It can take any numbers of arguments, but only have one expression
# We need it when we want to write an anonymous function inside another function

# syntax
# x = lambda param1, param2, param3 : param1, param2, param3

# Name function
def add_two_nums(a, b):
    return a + b
print(add_two_nums(5,25)) 

# lambda function
add_two_nums2 = lambda a,b : a + b
print(add_two_nums2(5,12))

