#-------------DICTIONARY----------------

#-------------Creating a dictionary----------------
#### Creando un diccionario vacio
empty_dict = {}
'''
print(empty_dict)
{}

print(type(empty_dict))
<class 'dict'>
'''

empty_dict2 = dict()
'''
print(empty_dict2)
{}

print(type(empty_dict2))
<class 'dict'>
'''

#### Creando un diccionario con valores
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
    }
'''
print(person)
{'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 
 'is_marred': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 
 'address': {'street': 'Space street', 'zipcode': '02210'}}
'''

#### Otra forma de crear diccionarios con valores
mi_info = dict(mi_nombre='Mateo', mi_edad=34)
'''
print(mi_info)
{'mi_nombre': 'Mateo', 'mi_edad': 34}
'''

#### Las listas no pueden ser claves ya que son mutables
'''
diccionario = {['nombre', 'apellido']: 'Mateo Gaviria'}
TypeError: unhashable type: 'list'
'''

#### Las tuplas si pueden ser claves ya que son inmutables
diccionario = {('nombre', 'apellido'): 'Mateo Gaviria'}
'''
print(diccionario)
{('nombre', 'apellido'): 'Mateo Gaviria'}
'''

#### Los conjuntos no pueden ser claves ya que son mutables
'''
diccionario = {{'nombre', 'apellido'}: 'Mateo Gaviria'}
TypeError: unhashable type: 'set'
'''

#### Un conjunto de tipo frozenset pueden ser claves
diccionario = {frozenset(['nombre', 'apellido']): 'Mateo Gaviria'}
'''
print(diccionario)
{frozenset({'apellido', 'nombre'}): 'Mateo Gaviria'}
'''

#### Creando un diccionario con el mismo valor para diferentes claves
#### Toma como clave los elementos del iterable que se pasa como parametro
diccionario = dict.fromkeys('nombre','saludos')
'''
print(diccionario)
{'n': 'saludos', 'o': 'saludos', 'm': 'saludos', 'b': 'saludos', 'r': 'saludos', 'e': 'saludos'}
'''

#### si se pasa un valor que no sea un iterable arroja error
'''
diccionario = dict.fromkeys(1,'saludos')
TypeError: 'int' object is not iterable
'''

#### Crear un diccionario donde todos los valores sean vacios
diccionario = dict.fromkeys(['nombre','saludos'])
'''
print(diccionario)
{'nombre': None, 'saludos': None}
'''
#### Crear un diccionario donde todas las llaves tengan el mismo valor
diccionario = dict.fromkeys(['carlos','pedro','samuel'], 32)
print(diccionario)


#------------Dictionary length--------------
'''
print(len(person))
7
'''

#------------Accessing dictionary items---------------

###### Using key name: We can access Dictionary items by referring to its key name.
######
'''
print(person['first_name'])
Asabeneh
'''
'''
print(person['country'])
Finland
'''

##### Using key name incorrect. Al utilizar un nombre de llave incorrecto detiene el programa
#####
'''
print(person['media'])
Exception has occurred: KeyError
'media'
'''

##### Using get method: returns None, which is a NoneType object data type, if the key does not exist.
#####
'''
print(person.get('color')) # llave color no existe
print(person.get('age'))
None
250
'''

#------------ Metodo item para iterar un diccionario --------------
persona = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': 1.80 
}
'''
Esto no es un iterable
print(persona)
{'nombre': 'Manuel', 'apellido': 'Mesa', 'edad': 22, 'peso': 88, 'altura': 1.8}
'''

'''
Esto si es un iterable
print(persona.items())
dict_items([('nombre', 'Manuel'), ('apellido', 'Mesa'), ('edad', 22), ('peso', 88), ('altura', 1.8)])
'''

#------------Adding items to a dictionary----------------

###### adding new key and value pair
######
persona = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': 1.80 
}

persona['trabajo'] = 'Instructor'
'''
print(persona.get('trabajo'))
Instructor
'''

###### Adding new value a key existent using append() method
###### Solo funciona para agregar un valor a un value de tipo lista
######
persona = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': [1.80, 1.79, 1.82] 
}

persona['altura'].append(1.81)
'''
print(persona['altura'])
[1.8, 1.79, 1.82, 1.81]
'''

###### si no es de tipo lista, detiene el programa y arroja error
######
'''
persona['edad'].append(19)
print(persona['edad'])
AttributeError: 'int' object has no attribute 'append'
'''

#-----------Modifying items in a dictionary-------------
persona = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': 1.80 
}

persona['edad'] = 19
'''
print(persona['edad'])
19
'''

persona['nombre'] = 'Maria'
'''
print(persona)
{'nombre': 'Maria', 'apellido': 'Mesa', 'edad': 19, 'peso': 88, 'altura': 1.8}
'''

#-----------Checking keys in a dictionary------------
persona = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': 1.80 
}

'''
print('nombre' in persona)
print('Color' in persona)
True
False
'''

#-----------Removing key and value pairs from a dictionary---------------

####### pop(key) method: Removes the item with the specified key name
#######
person = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': 1.80 
}

person.pop('nombre') # remueve de 1 en 1
'''
print(person)
{'apellido': 'Mesa', 
'edad': 22, 
'peso': 88, 
'altura': 1.8}
'''

person.pop("peso")
'''
print(person)
{'apellido': 'Mesa', 
'edad': 22, 
'altura': 1.8}
'''

###### popitem() method: Removes the last item
######
person = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': 1.80 
}
person.popitem()
'''
print(person)
{'nombre': 'Manuel', 
'apellido': 'Mesa', 
'edad': 22, 
'peso': 88}
'''

#using del. Removes an item with specified key name
#del person['is_marred']
#print(person)

#person.pop('skills')
#print(person)

#-----------Changing dictionary to a list of items--------------

##### Using items()
#####
persona = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22,
    'peso': 88,
    'altura': 1.80 
}
'''
print(persona.items())
dict_items([('nombre', 'Manuel'), ('apellido', 'Mesa'), ('edad', 22), ('peso', 88), ('altura', 1.8)])
'''


#-----------Clearing a dictionary--------------

###### Using clear() method to remove all item 
######
dictionary = {
    'nombre': 'Manuel',
    'apellido': 'Mesa',
    'edad': 22 
}

dictionary.clear()
'''
print(dictionary)
{}
'''

#-----------Deleting a dictionary------------
del person

#-----------Copy a dictionary-------------

###### copy() method: We can avoid mutation of the original dictionary.
######
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
'''
print(dct_copy)
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
'''

#-----------Getting dictionary keys as a list----------------

####### keys() method
#######
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
'''
print(keys)
dict_keys(['key1', 'key2', 'key3', 'key4'])
'''

#-----------Getting dictionary values as a list--------------
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
'''
print(values)
dict_values(['value1', 'value2', 'value3', 'value4'])
'''
