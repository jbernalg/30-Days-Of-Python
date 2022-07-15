#-------------------MODULES----------------------
#A module is a file containing a set of codes or a set of functions which can be included to an application

#-------------------Create a Module-------------------
#To create a module we write our codes in a python script and we save it as a .py file.
import mymodule

print(mymodule.generate_full_name('Jose', 'Gimenez'))

#------------------Import Function from a Module-------------------
from mymodule import generate_full_name, sum_two_nums, gravity

print(generate_full_name('Daniel', 'Pereira'))
print(sum_two_nums(20, 18))

mass = 100
weight = mass * gravity
print(weight)

#------------------Import Function from a Module and Renaming----------------
#During importing we can rename the name of the module
from mymodule import generate_full_name as fullname, sum_two_nums as total, gravity as g
print(fullname('Manuel', 'Girot'))
print(total(12, 20))

mass = 14
weight = mass * g
print(weight)


#-----------------Import Built-in Modules------------------
#math, datetime, os, sys, random, statistics, collections, json...

#-----------------OS Import------------------
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
#provides functions and variables used to manipulate different parts of the Python runtime environment.
#Function sys.argv returns a list of command line arguments passed to a Python script.
#The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

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





