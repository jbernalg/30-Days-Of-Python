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
