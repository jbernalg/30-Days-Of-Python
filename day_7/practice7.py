#-------------------SET----------------------

#-----------Creating a Set-----------------
st = {}
print(st)
st = set()
print(st)

#Creating a set with initial items
fruits = {'bananas', 'orange', 'mango', 'lemon'}
print(fruits)

#----------Getting set's length------------
print(len(fruits))

#----------Accessing items in a set-----------
#We use loop to access items

#----------Checking an items----------------
print('mango' in fruits)

#----------Adding items to a set-----------
#usind add()
fruits.add('lime')
print(fruits)

#Using update(). Add multiple items
fruits = {'bananas', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onio', 'carrot'}
fruits.update(vegetables)
print(fruits)

#----------Removing items from a set------------------
#using remove(). To check the item exist in the set.
fruits.remove('tomato')
print(fruits)
#fruits.remove('piña') #If the items is not found, the method will raise errors
#print(fruits)

#Using discard(). This method doesn't raise any errors
fruits.discard('potato')
print(fruits)
fruits.discard('piña') #This method doesn't raise any errors if the item is not exist
print(fruits)

#Using pop() method. Remove a random item a list and it return the removed item
remove_item = fruits.pop()
print(fruits)
print(remove_item)

#-------------Clearing items in a set------------------
#clear() method. Clear or empty the set
fruits.clear()
print(fruits)

#-------------Delete a Set-----------------
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

#-------------Converting list to set------------------
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits = list(fruits)
print(fruits)

fruits = set(fruits)
print(fruits)

#--------------Joining Sets--------------------
#Using union() method. Return a new set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

#Using Update() method. Insert a set into a given set
fruits.update(vegetables)
print(fruits)

#--------------finding intersection items-----------------
#Intersection return a set of items which are in both the set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))




