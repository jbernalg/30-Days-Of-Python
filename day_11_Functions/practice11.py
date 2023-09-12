#-------------------FUNCTION-----------------------
'''
- Nos ayuda a evitar repetir codigo
- Modularidad: nos permite separar el programa en partes mas pequeñas para luego
solucionarlo, modificarlo, hacer pruebas y luego integrarlas de vuelta al programa
- Permite que el codigo sea mantenible y mas sencillo de depurar. Creamos el cambio en
la funcion y este se vera reflejado en todo el codigo
- Hace que el codigo sea mas legible
'''

#-------------------Declaring and Calling a function-------
#### syntax
#def function_name():
#   codes

#Calling a function
#function_name()

#-------------------Function without parameters--------------------
def generate_full_name():
    first_name = 'Jose'
    last_name = 'Bernal'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
'''
generate_full_name()
Jose Bernal
'''

def add_two_numbers():
    num_one = 4
    num_two = 3
    total = num_one + num_two
    print(total)
'''
add_two_numbers()
7
'''

#-------------------Function returning a value------------------------
def generate_full_name():
    first_name = 'Jose'
    last_name = 'Bernal'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
'''
print(generate_full_name())
Jose Bernal
'''

#-------------------Function with parameters----------------------
#Single parameter
def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message
'''
print(greetings('Rivera'))
Rivera, welcome to Python for Everyone!
'''

def square_numbers(x):
    return x * x
'''
print(square_numbers(22))
484
'''

def area_of_circle(r):
    PI = 3.14
    area = PI*r**2
    return area

'''
print(area_of_circle(13))
530.66
'''

#Two parameters
def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
'''
Sum of two number:  17
print('Sum of two number: ',sum_two_numbers(1,16))
'''

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
'''
print('Age: ', calculate_age(2022, 1994))
Age:  28
'''

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ 'N'
    return weight
'''
print('Weight of an object in Newtons: ',weight_of_object(90, 9.81))
Weight of an object in Newtons:  882.9000000000001N
'''

#---------------Passing arguments with Key and Values---------------------
def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
'''
print(print_fullname(first_name='Daniel', last_name='Vergara'))
Daniel Vergara
'''

#### el orden en que se pasan los valores no importan siempre que se declaren 
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
'''
print(add_two_numbers(num2 = 13, num1 = 2))
15
'''

#---------------Function Returning a Value----------------------
#Returning a string
def print_name(first_name):
    return first_name
'''
print(print_name('Gerardo'))
Gerardo
'''

#Returning a number:
def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
'''
print('Age: ', calculate_age(2022, 2003))
Age: 19
'''

#Returning a boolean
def is_even(n):
    if n % 2 == 0:
        return True
    return False
'''
print(is_even(10))
print(is_even(21))
True
False
'''

#Returning a list:
def find_even_numbers(n):
    even = []
    for i in range(n + 1):
        if i % 2 == 0:
            even.append(i)
    return even
'''
print(find_even_numbers(10))
[0, 2, 4, 6, 8, 10]
'''

#------------------- Desempaquetando valores de una funcion----------------------
def value_oro_plata(p_petroleo):
    val_oro = p_petroleo*2.5
    val_plata = val_oro + p_petroleo
    return val_oro,val_plata

# valor solo del oro
'''
print(round(value_oro_plata(1.44)[0],2))
3.6
'''

# valor solo de la plata
'''
print(round(value_oro_plata(1.48)[1], 2))
5.18
'''

# desempaquetando valores de la funcion
valor_oro, valor_plata = value_oro_plata(1.44)
'''
print(f'Valor del oro: {round(valor_oro,2)}')
print(f'Valor de la plata: {round(valor_plata,2)}')
Valor del oro: 3.6
Valor de la plata: 5.04
'''

#---------------Function with default parameters------------------
#Sometimes we pass default values to parameters, when we invoke the function. 
#If we do not pass arguments when calling the function, their default values will be used.
def greetings(name = 'Peter'):
    message = name + ',Welcome to Python for Everyone!'
    return message
'''
print(greetings())
print(greetings('Samuel'))
Peter,Welcome to Python for Everyone!
Samuel,Welcome to Python for Everyone!
'''

def calculate_age(birth_year, current_year = 2023):
    age = current_year - birth_year
    return age
'''
print('Age: ', calculate_age(1900))
Age:  123
'''

#---------------Arbitrary number of arguments-----------------
#### util cuando no hay una cantidad determinada de argumentos 
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
'''
print(sum_all_nums(2,3,7,11))
23
'''

#### Podemos pasarle mas argumentos solo si se usa el * para el ultimo parametro
def suma(nombre, *numeros):
    return f'{nombre}, la suma de los numeros es: {sum(numeros)}'
'''
print(suma('Jose',1,3,5,7))
Jose, la suma de los numeros es: 16
'''

#### Utilizar el operador * dentro de la funcion
def suma_total(numeros):
    return sum([*numeros])
'''
print(suma_total([1,3,5,7]))
16
'''

#---------------Default and Arbitrary Number of parameters in Function------------------------
#### Cantidad de argumentos indefinidos
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)

print(generate_groups('Team 1', 'Javier', 'Miguel'))

#----------------Function as a parameters of another function--------------------
def square_numbers(n):
    return n * n

def do_something(f, x):
    return f(x)

print(do_something(square_numbers, 3))



