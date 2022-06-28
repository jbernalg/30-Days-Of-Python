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






