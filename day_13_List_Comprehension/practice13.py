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

# list  comprehensin can be combined with if expression

