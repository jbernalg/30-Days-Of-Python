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




