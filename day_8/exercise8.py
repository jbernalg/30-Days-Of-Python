#-----------------------DICTIONARY-------------------------

#Create an empty dictionary called dog
dog = {}
print(dog)

#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'kiara'
dog['color'] = 'blanco'
dog['breed'] = 'lobo siberiano'
dog['legs'] = 'grandes'
dog['age'] = 2
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'Jose', 'last_name': 'Vergara', 'gender': 'Male', 'age': 23, 'marital_status': 'married', 'skills': ['Pyhon', 'HTML', 'CSS'], 'country': 'Viena', 'address': 'calle 23, Av Libertad'}
print(student)

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student['skills'])

#Modify the skills values by adding one or two skills
student['skills'].append('Git')
student['skills'].append('Java')
print(student['skills'])

#Get the dictionary keys as a list
print(student.keys())

#Get the dictionary values as a list
print(student.values())

#Change the dictionary to a list of tuples using items() method
print(student.items())

#Delete one of the items in the dictionary
student.pop('last_name')
print(student)

#Delete one of the dictionaries
del student

