# ----------------------File Handling-------------------------

#-------------Open() built-in function----------------
# to handle data
# syntax
# open('filename', mode)  mode(r, a, w, x, t, b)

# r: Read. Opens a file for reading, it returns an error if the file does not exist.
# a: Append. Opens a file for appending, creates the file if it does not exist.
# w: Write. Opens a file for writing, creates the file if it does not exist.
# x: Create. Creates the specified file, return an error if the file exist.
# t: Text. Default value. Text mode
# b: Binary. Binary mode. (images)

#----------------Opening files for reading ----------------------
# the deafult mode of open is reading
# To open file I have created and saved a file named reading_file.txt in the current directory
f = open('./reading_file.txt')
print(f) 

#----------------Reading Methods--------------------
# read(): read the whole text as string
# If we want to limit the number of character we want to read, we can limit it by passing int value
# to the read(number) method.
txt = f.read()
print(type(txt))
print(txt)
f.close()

# let us print the first 10 characters of the text file.
f = open('./reading_file.txt')
txt = f.read(10)
print(txt)
f.close()

# readlines(): read all text line by line and returns a list of lines
f = open('./reading_file.txt')
lines = f.readlines()
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines()
f = open('./reading_file.txt')
lines = f.read().splitlines()
print(lines)
f.close()

# There is a new way of opening files using with - closes the files by itself
with open('./reading_file.txt') as f:
    lines = f.read().splitlines()
    print(lines)

# ------------------Opening Files for writing and updating--------------------
# To write to an existing file, we must add a mode as parameters to the open() function:
# a : will append to the end of the file, if the file does not it creates a new file
# w : will overwrite any existing content, if the file does not exist it creates

# append some text to the file 
with open('./reading_file.txt', 'a') as f:
    f.write(' Texto agregado externamente')

# creates a new file, if the file does not exist:
with open('./file_example.txt', 'w') as f:
    f.write(' Nueva oracion para el nuevo archivo')

# --------------Deleting Files---------------
# if we want to remove a file we use os module.
import os
os.remove('./file_example.txt')

# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:
if os.path.exists('./example.txt'):
    os.remove('./exmple.txt')
else:
    print('The file does not exist')

# ---------------File Types-----------------

# --------------File with txt extension----------------
# File with JSON extension
# JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
 
# Changing JSON to dictionary
# To change a JSON to a dictionary, first we import the json module and then we use loads method.
import json

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing dictionary to JSON
# To change a dictionary to a JSON we use dumps method from the json module.
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

