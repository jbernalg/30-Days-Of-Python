#-------------DICTIONARY----------------

#-------------Creating a dictionary----------------
empty_dict = {}
print(empty_dict)

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

print(person)

#------------Dictionary length--------------
print(len(person))

#------------Accessing dictionary items---------------
#Using key name. We can access Dictionary items by referring to its key name.
print(person['first_name'])
print(person['country'])

#Using get method
#The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('age'))
print(person.get('color'))

#------------Adding items to a dictionary----------------
#adding new key and value pair
person['job_title'] = 'Instructor'
print(person.get('job_title'))

#adding new value a key existent using append() method
person['skills'].append('HTML')
print(person['skills'])

#-----------Modifying items in a dictionary-------------
person['first_name'] = 'Jose'
print(person['first_name'])

person['age'] = '20'
print(person)

#-----------Checking keys in a dictionary------------
print('skills' in person)
print('Color' in person)

#-----------Removing key and value pairs from a dictionary---------------
#using pop(key) method. Removes the item with the specified key name
person.pop('first_name')
print(person)

#using popitem() method. Removes the last item
person.popitem()
print(person)

#using del. Removes an item with specified key name
del person['is_marred']
print(person)

person.pop('skills')
print(person)

#-----------Changing dictionary to a list of items--------------
#using items()
print(person.items())

#-----------Clearing a dictionary--------------
#using clear() method to remove all item 
print(person.clear())

#-----------Deleting a dictionary------------
del person

#-----------Copy a dictionary-------------
#using copy() method. We can avoid mutation of the original dictionary.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)

#-----------Getting dictionary keys as a list----------------
#using keys() method
keys = dct.keys()
print(keys)


