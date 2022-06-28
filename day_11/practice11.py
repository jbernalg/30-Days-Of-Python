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




