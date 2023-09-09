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
print(len(fruits))

#---------------Accessing Tuples items-------------------
print('first fruit:', fruits[0])
print('last fruits: ',fruits[len(fruits) - 1])
print('first fruit: ', fruits[-5])
print('last fruit: ', fruits[-1])

#---------------Slicing tuples--------------------
all_fruits = fruits[:] #all fruits
print(all_fruits)
orange_mango = fruits[1:3]
print(orange_mango)

print('all fruits: ', fruits[-5:])
print('orange mango: ', fruits[-4:-2])

#---------------Changing tuples to list--------------------
fruits = list(fruits)
print(fruits)
fruits = tuple(fruits)
print(fruits)

#----------------Checking an item in a tuple------------------
print('orange' in fruits)
print('apple' in fruits)

#----------------Joining tuples----------------------
fruits = ('banana', 'orange', 'mango', 'lemon', 2)
vegetable = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_vegetable = fruits + vegetable
print(fruits_vegetable)

#----------------Delete tuples--------------------
del fruits

