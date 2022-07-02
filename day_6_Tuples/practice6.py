#-----------------TUPLES-------------------------

#----------------Create a Tuple-------------------
#Empty tuple
empty_tuple = ()
print(empty_tuple)

empty_tuple = tuple()
print(empty_tuple)

#tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon', 2)
print(fruits)

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

