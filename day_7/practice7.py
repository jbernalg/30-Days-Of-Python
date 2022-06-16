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
fruits.discard('piña') #This method deosn't raise any errors if the item is not exist
print(fruits)

#Using pop() method. Remove a random item a list and it return the removed item

