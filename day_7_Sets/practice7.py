#-------------------SET----------------------
'''
- Pueden contener datos que sean inmutable. Una lista por ejemplo, no la puede contener
ya que es mutable. Una tupla si la puede contener debido a que es inmutable
'''
#-----------Creating a Set-----------------
st = {}
'''
print(st)
{}
'''
st = set()
'''
print(st)
set()
'''

##### Creating a set with initial items
fruits = {'bananas', 'orange', 'mango', 'lemon'}
'''
print(fruits)
{'bananas', 'mango', 'lemon', 'orange'}
'''
##### Elementos repetidos se eliminan del set
fruits = {'bananas', 'orange', 'mango', 'lemon', 'lemon', 'mango'}
'''
print(fruits)
{'lemon', 'bananas', 'mango', 'orange'}
'''

#----------Datos inmutables---------------
conjunto = set(['dato1', 'dato2'])
'''
print(conjunto)
{'dato2', 'dato1'}
'''

#### Lista dentro de un set
'''
conjunto = set(['dato1', ['dato2', 'dato3']])
TypeError: unhashable type: 'list'
'''

#### tupla dentro de un set
conjunto = set(['dato1', ('dato2', 'dato3')])
'''
print(conjunto)
{('dato2', 'dato3'), 'dato1'}
'''

#### Diccionario dentro de un set
'''
conjunto = set(['dato1', {'dato2', 'dato3'}])
TypeError: unhashable type: 'set'
'''

#### Conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1', 'dato2']) # crea un conjunto inmutable
conjunto2 = {conjunto1, 'dato3'}
'''
print(conjunto2)
{frozenset({'dato2', 'dato1'}), 'dato3'}
'''

#----------Getting set's length------------
'''
print(len(fruits))
4
'''

#----------Accessing items in a set-----------
#We use loop to access items

#----------Checking an items----------------
fruits = {'bananas', 'orange', 'mango', 'lemon'}
'''
print('mango' in fruits)
True
'''

#----------Adding items to a set-----------
##### Usind add(). Se agrega el elemento en una posicion indeterminada 
fruits = {'bananas', 'orange', 'mango', 'lemon'}
fruits.add('lime')
'''
print(fruits)
{'lime', 'orange', 'lemon', 'mango', 'bananas'}
'''

##### Using update(). Add multiple items. Elementos repetidos no se agregan
fruits = {'bananas', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'lemon', 'carrot'}
fruits.update(vegetables)
'''
print(fruits)
{'tomato', 'lemon', 'cabbage', 'potato', 'mango', 'orange', 'bananas', 'carrot'}
'''

#----------Removing items from a set------------------
##### Using remove(). To check the item exist in the set.
fruits = {'bananas', 'orange', 'mango', 'lemon'}
fruits.remove('orange')
'''
print(fruits)
{'bananas', 'mango', 'lemon'}
'''

##### If the items is not found, the method will raise errors
'''
fruits.remove('piña') 
print(fruits)
KeyError: 'piña'
'''

##### Using discard(). This method doesn't raise any errors
fruits = {'bananas', 'orange', 'mango', 'lemon'}
fruits.discard('piña')
'''
print(fruits)
{'lemon', 'mango', 'bananas', 'orange'}
'''

##### Using pop() method. Remove a random item a list and it return the removed item
fruits = {'bananas', 'orange', 'mango', 'lemon'}
remove_item = fruits.pop()
'''
print(remove_item)
orange

print(fruits)
{'mango', 'lemon', 'bananas'}
'''

#-------------Clearing items in a set------------------
##### clear() method. Clear or empty the set
fruits = {'bananas', 'orange', 'mango', 'lemon'}
fruits.clear()
'''
print(fruits)
set()
'''

#-------------Delete a Set-----------------
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

#-------------Converting list to set------------------
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits = list(fruits)
'''
print(fruits)
['orange', 'mango', 'lemon', 'banana']
'''

fruits = set(fruits)
'''
print(fruits)
{'orange', 'mango', 'lemon', 'banana'}
'''

#--------------Joining Sets--------------------
#### Using union() method. Return a new set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
union_set = fruits.union(vegetables)
'''
print(union_set)
{'mango', 'cabbage', 'tomato', 'onion', 'banana', 'potato', 'lemon', 'orange', 'carrot'}
'''

#### Using Update() function. Insert a set into a given set
conjunto1 = {1,3,5,7,9}
conjunto2 = {'banana','apple','orange'}
conjunto2.update(conjunto1)
'''
print(conjunto2)
{1, 'banana', 3, 5, 7, 'apple', 9, 'orange'}
'''

#--------------finding intersection items-----------------
##### Intersection: return a set of items which are in both the set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection_set = whole_numbers.intersection(even_numbers)
'''
print(intersection_set)
{0, 2, 4, 6, 8, 10}
'''

#--------------Checking the difference between two Sets-----------------
##### Return a set with the difference between two sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
difference_set = whole_numbers.difference(even_numbers)
'''
print(difference_set)
{1, 3, 5, 7, 9}
'''

#--------------Finding symmetric difference between two sets-----------------
##### Return a set that contains all items from both sets, except items that are present in both sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5, 11}
dif_sim_set = whole_numbers.symmetric_difference(some_numbers)
'''
print(dif_sim_set)
{0, 6, 7, 8, 9, 10, 11}
'''

#-------------Disjoint Sets-------------------
#If two sets do not have a common item we call them disjoint sets
#We can check if two sets are joint or disjoint using isdisjoint() method
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
result = even_numbers.isdisjoint(odd_numbers)
'''
print(result)
True
'''

conjunto1 = {1,3,5,7,9}
conjunto2 = {2,5,6}
result = conjunto1.isdisjoint(conjunto2)
'''
print(result)
False
'''

result = conjunto2.isdisjoint(conjunto1)
'''
print(result)
False
'''

#------------Checking Sets------------------

##### Verificar si un conjunto es un subconjunto de otro
conjunto1 = {1,3,5,7,9}
conjunto2 = {1,3,7}
result = conjunto2.issubset(conjunto1)
'''
print(result)
True
'''

result = conjunto1.issubset(conjunto2)
'''
print(result)
False
'''
##### Otra forma de verificar si un conjunto es un subconjunto de otro
result = conjunto2 <= conjunto1
'''
print(result)
True
'''

result = conjunto1 <= conjunto2
'''
print(result)
False
'''

##### Verificar si un conjunto es un superconjunto de otro
result = conjunto1.issuperset(conjunto2)
'''
print(result)
True
'''

#### Otra forma de verificar si un conjunto es un superconjunto de otro
result = conjunto1 > conjunto2
'''
print(result)
True
'''