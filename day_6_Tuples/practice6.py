#-----------------TUPLES-------------------------
'''
- Manejan mejor la memoria por lo que son recomendadas para leer datos fijos inmutables.
- Las listas ocupan dos espacios de memoria: uno donde almacena y otro donde guarda las
modificaciones
- Las tuplas solo ocupan un espacio en memoria por lo que son mas optimas 
'''


#----------------Create a Tuple-------------------
##### Empty tuple
empty_tuple = ()
'''
print(empty_tuple)
()
'''

empty_tuple = tuple()
'''
print(empty_tuple)
()
'''

##### Tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon', 2)
'''
print(fruits)
('banana', 'orange', 'mango', 'lemon', 2)
'''

###### Creando una tupla a partir de una lista
vegetable = tuple(['tomate', 'cebolla', 'pepino', 'lechuga'])
'''
print(vegetable)
print(type(vegetable))
('tomate', 'cebolla', 'pepino', 'lechuga')
<class 'tuple'>
'''

##### Crear tuplas sin parentesis
tupla = 'dato1', 'dato2', 'dato3'
'''
print(tupla)
print(type(tupla))
('dato1', 'dato2', 'dato3')
<class 'tuple'>
'''

##### Crear tuplas sin parentesis de un solo valor
tupla = 'dato1',
'''
print(tupla)
print(type(tupla))
('dato1',)
<class 'tuple'>
'''

#---------------Tuple Length--------------------
fruits = ('banana', 'orange', 'mango', 'lemon', 2)
'''
print(len(fruits))
5
'''

#---------------Accessing Tuples items-------------------
##### Accede a las tuplas mediante los slicing
fruits = ('banana', 'orange', 'mango', 'lemon', 'mora')
'''
print('first fruit:', fruits[0])
first fruit: banana

print('last fruits: ',fruits[len(fruits) - 1])
last fruits:  mora

print('first fruit: ', fruits[-5])
first fruit:  banana

print('last fruit: ', fruits[-1])
last fruit:  mora
'''

#---------------Slicing tuples--------------------
fruits = ('banana', 'orange', 'mango', 'lemon', 'mora')

#### Selecciona toda la tupla
all_fruits = fruits[:] 
'''
print(all_fruits)
('banana', 'orange', 'mango', 'lemon', 'mora')
'''

#### Selecciona una parte de la tupla
orange_mango = fruits[1:3]
'''
print(orange_mango)
('orange', 'mango')
'''

#### Otra forma de seleccionar partes de la tupla
'''
print('all fruits: ', fruits[-5:])
all fruits:  ('banana', 'orange', 'mango', 'lemon', 'mora')

print('orange mango: ', fruits[-4:-2])
orange mango:  ('orange', 'mango')
'''

#---------------Changing tuples to list--------------------
fruits = ('banana', 'orange', 'mango', 'lemon', 'mora')
fruits = list(fruits)
'''
print(fruits)
['banana', 'orange', 'mango', 'lemon', 'mora']
'''

fruits = tuple(fruits)
'''
print(fruits)
('banana', 'orange', 'mango', 'lemon', 'mora')
'''

#----------------Checking an item in a tuple------------------
'''
print('orange' in fruits)
True

print('apple' in fruits)
False
'''

#----------------Joining tuples----------------------
fruits = ('banana', 'orange', 'mango', 'lemon', 'mora')
vegetable = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_vegetable = fruits + vegetable
'''
print(fruits_vegetable)
('banana', 'orange', 'mango', 'lemon', 'mora', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
'''
#----------------Delete tuples--------------------
del fruits