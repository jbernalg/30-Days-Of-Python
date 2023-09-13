#-------------------MODULES----------------------
'''
A module is a file containing a set of codes or a set of functions which 
can be included to an application
'''
#-------------------Create a Module-------------------
#### To create a module we write our codes in a python script and we save it as a .py file.
#### Este tipo de llamado se conoce como names space
import mymodule
nombre_completo = mymodule.generate_full_name('Jose', 'Gimenez')
'''
print(nombre_completo)
Jose Gimenez
'''

#------------------Import Functions from a Module-------------------
from mymodule import generate_full_name, sum_two_nums, gravity

nombre_completo = generate_full_name('Daniel', 'Diaz')
suma_numeros = sum_two_nums(10,14)
'''
print(nombre_completo)
print(suma_numeros)
Daniel Diaz
24
'''

mass = 100
weight = mass * gravity
'''
print(weight)
980.0000000000001
'''

#------------------Import Function from a Module and Renaming----------------
#### During importing we can rename the name of the module
from mymodule import generate_full_name as fullname, sum_two_nums as total, gravity as g
nombre_completo = fullname('Diveana','Morales')
result = total(12,6)
'''
print(nombre_completo)
print(result)
Diveana Morales
18
'''

mass = 14
weight = mass * g
'''
print(weight)
137.20000000000002
'''

#### Importar todas las funciones de un modulo.
#### Es una mala practica porque puede sobrecargar el programa
from mymodule import  *
nombre_completo = generate_full_name('Ligio', 'Vargas')
result = sum_two_nums(12,13)
'''
print(nombre_completo)
print(result)
print(gravity)
Ligio Vargas
25
9.8
'''

#----- Error al llamar una funcion que tiene el mismo nombre que una variable ------
'''
Al llamar una funcion que tiene el mismo nombre que una variable, se asigna
el valor de variable y no la funcion por lo que es importante practicar metodologias
de escritura para diferenciar ambos objetos 
'''

# ----- Metodos y propiedades de un modulo -----------

##### Metodos del modulo importado
'''
print(dir(mymodule))
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'generate_full_name', 'gravity', 'sum_two_nums']
'''

#### Nombre del metodo importado
import mymodule as m_propio
'''
print(m_propio.__name__)
mymodule
'''

#-----------------Import Built-in Modules------------------
#math, datetime, os, sys, random, statistics, collections, json...

#-----------------Enrutando Modulos ------------------
#Using os module it is possible to automatically perform many operating system task.
import os

#Creating a directory
os.mkdir('directory_name')

#Changing the current directory
#os.chdir('path')

#Getting current working directory
print(os.getcwd())

#Removing a directory
os.rmdir('directory_name')


#-----------------Sys Module------------------
'''provides functions and variables used to manipulate different parts of the Python runtime environment.
Function sys.argv returns a list of command line arguments passed to a Python script.
The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.
'''
#-----------------Statistics Module---------------------
#provide functions for mathematical statisticsof numeric data
from statistics import *
age = [20, 20, 18, 24, 30, 29, 24, 25, 24, 30]
print(mean(age))
print(median(age))
print(mode(age))
print(stdev(age))

#-----------------Math Module--------------------
#Module containing many mathematical operations and constants
import math
print(math.pi)            #constante pi
print(math.sqrt(25))      #square root
print(math.pow(2, 3))     #exponential function
print(math.floor(9.81))   #rounding to the lowest
print(math.ceil(9.81))    #rounding to the highest
print(math.log10(100))    #logarithm

#----------------String Module----------------
import string
print(string.ascii_letters) #abecedario
print(string.digits)        #digitos
print(string.punctuation)   #signos de puntuacion


#----------------Random Module----------------
from random import random, randint
print(random())
print(randint(5, 20))





