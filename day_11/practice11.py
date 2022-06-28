#-------------------FUNCTION-----------------------

#-------------------Declaring and Calling a function-------
#syntax
#def function_name:
#   codes

#Calling a function
#function_name

#-------------------Function without parameters--------------------
def generate_full_name():
    first_name = 'Jose'
    last_name = 'Bernal'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()

def add_two_numbers():
    num_one = 4
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()

#-------------------Function returning a value------------------------
def generate_full_name():
    first_name = 'Jose'
    last_name = 'Bernal'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

#-------------------Function with parameters----------------------
#Single parameter
def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Rivera'))

def square_numbers(x):
    return x * x

print(square_numbers(22))

def area_of_circle(r):
    PI = 3.14
    area = PI*r**2
    return area

print(area_of_circle(13))

#Two parameters
def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

print('Sum of two number: ',sum_two_numbers(1,16))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2022, 1994))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ 'N'
    return weight

print('Weight of an object in Newtons: ',weight_of_object(90, 9.81))

#---------------Passing arguments with Key and Values---------------------
def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(print_fullname(first_name='Daniel', last_name='Vergara'))

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

print(add_two_numbers(num2 = 13, num1 = 2))

#---------------Function Returning a Value----------------------
#Returning a string
def print_name(first_name):
    print(first_name)
print_name('Gerardo')

#Returning a number:
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2022, 2003))

#Returning a boolean
def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(10))
print(is_even(21))

#Returning a list:
def find_even_numbers(n):
    even = []
    for i in range(n + 1):
        if i % 2 == 0:
            even.append(i)
    return even

print(find_even_numbers(87))

#---------------Function with default parameters------------------
#Sometimes we pass default values to parameters, when we invoke the function. 
#If we do not pass arguments when calling the function, their default values will be used.
def greetings(name = 'Peter'):
    message = name + ',Welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Samuel'))

def calculate_age(birth_year, current_year = 2022):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1900))




