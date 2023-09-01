#-----------------------Create a list------------------------------

######## list built in funtion
########
lista = list()

######## empty list
########
empty_list = list()
'''
print(len(empty_list))
0
'''

#empty list with squares brackets []
lista = []
'''
print(len(lista))
0
'''

#List with initial values.
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

####### mostrar elementos de una lista
#######
'''
print('Fruits: ', fruits)
Fruits:  ['banana', 'orange', 'mango', 'lemon']
'''
####### len(): funcion que muestra la cantidad de elementos de la lista
#######
'''
print('Number of fruits: ', len(fruits))
4
'''

######## List can have items of different data types
########
lista = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]
'''
print(lista)
['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]
'''

#--------------Accessing list items using indexing----------------------------
# primer elemento de la lista
fruits = ['banana', 'orange', 'mango', 'lemon'] 
'''
print(fruits[0])
banana
'''
# elemento de indice 2 de la lista
'''
print(fruits[2])
mango
'''
# Numero de elementos de la lista contando el 0
last_index = len(fruits) - 1
'''
print(last_index)
3
'''

# elemento con indice -4
'''
print(fruits[-4])
banana
'''

# elemento con indice -2
'''
print(fruits[-2])
mango
'''


#-------------------------Unpacking items list-----------------------------------
lista = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lista # * resto de los elementos 
'''
print(first_item)
item

print(second_item)
item2

print(third_item)
item3

print(rest)
['item4', 'item5']
'''

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
'''
print(first)          
1

print(second)         
2

print(third)          
3

print(rest)           
[4, 5, 6, 7, 8, 9]

print(tenth)
10
'''

#-------------------------Slicing items from list------------------------

# mostrar todos los elementos menos el primero
fruits = ['banana', 'orange', 'mango', 'lemon']
'''
print(fruits[1:])
['orange', 'mango', 'lemon']
'''

# mostrar elementos intercalados
fruits = ['banana', 'orange', 'mango', 'lemon']
'''
print(fruits[::2])
['banana', 'mango']
'''
# mostrar del elemento -3 en adelante
fruits = ['banana', 'orange', 'mango', 'lemon']
'''
print(fruits[-3:])
['orange', 'mango', 'lemon']
'''

# mostrar elementos intercalados en sentido contrario
fruits = ['banana', 'orange', 'mango', 'lemon']
'''
print(fruits[::-2])
['lemon', 'orange']
'''

#--------------------------Modifying lists------------------------------

# cambiar el valor del primer elemento
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Aguacate'
'''
print(fruits)
['Aguacate', 'orange', 'mango', 'lemon']
'''

# cambiar el valor del segundo elemento
fruits = ['Aguacate', 'orange', 'mango', 'lemon']
fruits[1] = 'Apple'
'''
print(fruits)
['Aguacate', 'Apple', 'mango', 'lemon']
'''

#------------------------Checking items in a list-----------------------
fruits = ['Aguacate', 'orange', 'mango', 'lemon']
exist = 'lemon' in fruits
'''
print(exist)
True
''' 

#-----------------------Adding items to a list--------------------------
####### Metodo append: agrega el elemento al final de la lista
#######
fruits = ['Aguacate', 'orange', 'mango', 'lemon']
fruits.append('mango')
'''
print(fruits)
['Aguacate', 'Apple', 'mango', 'lemon', 'mango']
'''

fruits = ['Aguacate', 'Apple', 'mango', 'lemon', 'mango']
fruits.append('cereza')
'''
print(fruits)
['Aguacate', 'Apple', 'mango', 'lemon', 'mango', 'cereza']
'''

######## Metodo insert: Selecciona por medio del indice la ubicacion del nuevo elemento
########
fruits = ['Aguacate', 'Apple', 'mango', 'lemon', 'mango', 'cereza']
fruits.insert(2, 'apple')
'''
print(fruits)
['Aguacate', 'Apple', 'apple', 'mango', 'lemon', 'mango', 'cereza']
'''

fruits = ['Aguacate', 'Apple', 'apple', 'mango', 'lemon', 'mango', 'cereza']
fruits.insert(3, 'lime')
'''
print(fruits)
['Aguacate', 'Apple', 'apple', 'lime', 'mango', 'lemon', 'mango', 'cereza']
'''

####### Metodo tradicional. Agregar el elemento al final de la lista
#######
fruits = ['Aguacate', 'Apple', 'apple', 'lime', 'mango', 'lemon', 'mango', 'cereza']
fruits = fruits + ['uva']
'''
print(fruits)
['Aguacate', 'Apple', 'apple', 'lime', 'mango', 'lemon', 'mango', 'cereza', 'uva']
'''

#-----------------------Removing item from list------------------------

######## Remove the item first ocurrence
########
fruits = ['Aguacate', 'Apple', 'apple', 'lime', 'mango', 'lemon', 'mango', 'cereza', 'uva']
fruits.remove('apple')
'''
print(fruits)
['Aguacate', 'Apple', 'lime', 'mango', 'lemon', 'mango', 'cereza', 'uva']
'''

fruits.remove('mango')
'''
print(fruits)
['Aguacate', 'Apple', 'lime', 'lemon', 'mango', 'cereza', 'uva']
'''

######## Removing items using pop
########
# remove last item
fruits = ['Aguacate', 'Apple', 'lime', 'lemon', 'mango', 'cereza', 'uva']
fruits.pop()
'''
print(fruits)
['Aguacate', 'Apple', 'lime', 'lemon', 'mango', 'cereza']

'''

# eliminamos elemento segun su indice
fruits = ['Aguacate', 'Apple', 'lime', 'lemon', 'mango', 'cereza']
fruits.pop(1)
'''
print(fruits)
['Aguacate', 'lime', 'lemon', 'mango', 'cereza']
'''

######## Removing items using Del
########
# eliminar elemento segun su indice
fruits = ['Aguacate', 'lime', 'lemon', 'mango', 'cereza']
del fruits[2]
'''
print(fruits)
['Aguacate', 'lime', 'mango', 'cereza']
'''

# eliminar todos los elementos excepto el primero
fruits = ['Aguacate', 'lime', 'mango', 'cereza']
del fruits[1:]
'''
print(fruits)
['Aguacate']
'''

# eliminar toda la lista
fruits = ['Aguacate']
del fruits #to delete the list completely
'''
print(fruits)
no existe
'''

####### Clearing list items
#######
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
'''
print(fruits)
[]
'''


#---------------------Copying a list----------------------
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
'''
print(fruits_copy)
['banana', 'orange', 'mango', 'lemon']
'''

#---------------------Joining list------------------------
##### Operator plus
#####
positive_number = [1,2,3,4,5]
zero = [0]
negative_number = [-5,-4,-3,-2,-1]
integer = negative_number + zero + positive_number
'''
print(integer)
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
'''

###### joining using extend() method
######
num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
'''
print('Numbers: ', num1)
Numbers:  [0, 1, 2, 3, 4, 5, 6]
'''


#--------------------Counting items in a list----------------
# cuenta el numero de elementos que hay hasta el elemento seleccionado
ages = [22, 19, 24, 25, 26, 24, 25, 24]
'''
print(ages.count(24))
3
'''


#--------------------Finding index of an item------------------
# muestra el indice del elemento seleccionado
fruits = ['banana', 'orange', 'mango', 'lemon']
'''
print(fruits.index('orange'))
1
'''


#--------------------Reversing a list-------------------------
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
'''
print(fruits)
['lemon', 'mango', 'orange', 'banana']
'''


#--------------------Sorting list items----------------------
####### sort(): modifica la lista original
#######
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
'''
print(fruits)
['banana', 'lemon', 'mango', 'orange']
'''

####### ordena en orden alfabetico y luego reversa la lista
#######
fruits = ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
'''
print(fruits)
['orange', 'mango', 'lemon', 'banana']
'''

####### sorted(): devuelve la lista ordenanda sin modificar la original
fruits = ['orange', 'mango', 'lemon', 'banana']
'''
print(sorted(fruits))
['banana', 'lemon', 'mango', 'orange']
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
'''
print(fruits)
['orange', 'mango', 'lemon', 'banana']
'''