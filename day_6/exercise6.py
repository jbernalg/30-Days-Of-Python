#Create an empty tuple
empty = tuple()
print(empty)

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
family = ('Yeison','Manuel', 'Jennifer', 'Jose', 'Edilson')
print(family)

#Join brothers and sisters tuples and assign it to siblings
brothers = ('Manuel', 'Yeison', 'Jose')
sisters = ('Jennifer', 'Salome') #las tuplas debe contener mas de un items
siblings = brothers + sisters
print(siblings) 

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('Maria')
siblings.append('Jose')
siblings = tuple(siblings)
print(siblings)

#------------------------Level 2------------------------------------
#Unpack siblings and parents from family_members
siblings = list(siblings)
siblings1, siblings2, siblings3, siblings4,siblings5, *parents = siblings
print(parents)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('banana', 'Apple', 'Uvas', 'Pera')
vegetables = ('tomato', 'potatos', 'Cilantre')
animal = ('dog', 'cat', 'tigger', 'lion', 'delphin')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)



