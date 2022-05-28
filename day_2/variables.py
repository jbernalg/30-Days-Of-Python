# Dia 2. 30 dia  de programacion en python

from ast import keyword
from cmath import pi


name = 'Jeinfferson'
last_name = 'Bernal'
name_complet = 'Jose Gimenez'
country = 'Mexico'
age = 29
year = 2022
is_married = False
is_True = True
is_light_on = False
shoes, computer, color = 3, 'acer', 'blue'

print(type(name))
print(type(last_name))
print(type(name_complet))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_True))
print(type(is_light_on))
print(type(shoes), type(computer), type(color))

#length name
print('Length name: ', len(name))

#Compare the length of your first and last name
print(f'''Length name: {len(name)}
Length last name: {len(last_name)}''')

#Declara 5 como num_one y 4 como num_two
num_one = 5
num_two = 4

#sumar num_one y num_two
sum_total = num_one + num_two

#restar num_two a num_one
sust_total = num_one - num_two

#multplicar num_one por num_two
mult = num_one*num_two

#dividir num_one entre num_two
divis = num_one//num_two

#Use la división de módulo para encontrar num_two dividido por num_one
rest = num_two % num_one

#calcule num_one a la potencia de num_two
expo = num_one**num_two

#Encuentre la división de piso de num_one por num_two
divfloat = num_one/num_two

# El radio de un círculo es de 30 metros. Calcule el área de un círculo y asigne el valor a un nombre 
# de variable de area_of_circle
r = 30
area_of_circle = pi*r**2
print(area_of_circle)

# Calcule la circunferencia del círculo y asigne el valor a una variable con el nombre de circum_of_circle
circum_of_circle = 2*pi*r
print(circum_of_circle)

# Tome el radio como entrada del usuario y calcule el área.
r = int(input('Ingrese el radio del circulo para calular el area: '))
area_circle = pi*r**2
print(f'El area del circulo es {area_circle}')

# Use la función de entrada incorporada para obtener el nombre, el apellido, 
# el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
nombre = input('Ingrese el nombre: ')
apellido = input('Ingrse el apellido: ')
pais = input('Ingrese pais de origen: ')
edad = input('Ingrese la edad: ')
print(f'Nombre: {nombre}, Apellido: {apellido}, Pais: {pais}, Edad: {edad}')

help('keyword')
