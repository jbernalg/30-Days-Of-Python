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
