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


