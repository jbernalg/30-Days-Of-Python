# ----------------------File Handling-------------------------

#-------------Open() built-in function----------------
'''
to handle data
syntax
open('filename', mode)  mode(r, a, w, x, t, b)

r: Read. Opens a file for reading, it returns an error if the file does not exist.
a: Append. Opens a file for appending, creates the file if it does not exist.
w: Write. Opens a file for writing, creates the file if it does not exist.
x: Create. Creates the specified file, return an error if the file exist.
t: Text. Default value. Text mode
b: Binary. Binary mode. (images)
'''
#----------------Opening files for reading ----------------------
''' 
the deafult mode of open is reading. To open file I have created and saved a 
file named reading_file.txt in the current directory
'''
ruta_archivo = "/home/jbernal/Python/30DaysOfPython/day_19_File_Handling/reading_file.txt"
f = open(ruta_archivo)
'''
print(f) 
<_io.TextIOWrapper name='/home/jbernal/Python/30DaysOfPython/day_19_File_Handling/reading_file.txt' 
mode='r' encoding='UTF-8'>
'''

#----------------Reading Methods--------------------
'''
read(): read the whole text as string
If we want to limit the number of character we want to read, we can limit it by 
passing int value to the read(number) method.
'''
#### Tipo de dato del archivo
txt = f.read()
'''
print(type(txt))
<class 'str'>
'''

#### Contenido del archivo
'''
print(txt)
hola--- saludos a todos
Que tengan un feliz dia
'''
#### Cerrar el archivo al final
f.close()

#### let us print the first 10 characters of the text file.
f = open(ruta_archivo)
txt = f.read(10)
'''
print(txt)
hola--- sa
'''
# cerrar el arhcivo. Es una buena paractica
f.close()

#### readlines(): read all text line by line and returns a list of lines
f = open(ruta_archivo)
lines = f.readlines()
'''
print(lines)
['hola--- saludos a todos\n', 'Que tengan un feliz dia]
'''

# cerrar archivo
f.close()

#### splitlines() Another way to get all the lines as a list 
f = open(ruta_archivo)
lines = f.read().splitlines()
'''
print(lines)
['hola--- saludos a todos\n', 'Que tengan un feliz dia]
'''

# cerrar archivo
f.close()

#### with open: is a new way of opening files using. Closes the files by itself
with open(ruta_archivo) as f:
    lines = f.read().splitlines()
    '''
    print(lines)
    ['hola--- saludos a todos\n', 'Que tengan un feliz dia]
    '''

# ------------------Opening Files for writing and updating--------------------
'''
To write to an existing file, we must add a mode as parameters to the open() function:
a : will append to the end of the file, if the file does not it creates a new file
w : will overwrite any existing content, if the file does not exist it creates
'''

#### append some text to the file 
with open(ruta_archivo, 'a') as f:
    f.write(' Texto Nuevo')
'''
reading_file.txt
hola--- saludos a todos
Que tengan un feliz dia Texto Nuevo
'''    

#### creates a new file, if the file does not exist:
with open('./file_example.txt', 'w') as f:
    f.write(' Nueva oracion para el nuevo archivo')
'''
file_example.txt
 Nueva oracion para el nuevo archivo
'''

# --------------Deleting Files---------------

#### if we want to remove a file we use os module.
import os
os.remove('./file_example.txt')

#### If the file does not exist, the remove method will raise an error, 
# so it is good to use a condition like this:
if os.path.exists('./example.txt'):
    os.remove('./exmple.txt')
else:
    print('The file does not exist')
'''
The file does not exist
'''

# ---------------File Types-----------------

# --------------File with txt extension----------------
'''
File with JSON extension
JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
'''
#### dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}

#### JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'skills': ['JavaScrip', 'React', 'Python']}"

#### we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
 
#### Changing JSON to dictionary
# To change a JSON to a dictionary, first we import the json module and then we use loads method.
import json

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

#### let's change JSON to dictionary
person_dct = json.loads(person_json)

#### Tipo de dato al aplicar el cambio
'''
print(type(person_dct))
<class 'dict'>
'''
#### Contenido del diccionario
'''
print(person_dct)
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 
'skills': ['JavaScrip', 'React', 'Python']}
'''

#### Contenido de la llave name
'''
print(person_dct['name'])
Asabeneh
'''

#### Changing dictionary to JSON
# To change a dictionary to a JSON we use dumps method from the json module.
import json
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

# let's convert it to json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json

# tipo de dato
'''
print(type(person_json))
<class 'str'>
'''
# contenido del json
'''
print(person_json)
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
'''

#------------------Saving as JSON File----------------------
'''
Let us save it as a json file using the following steps. For writing a json file, 
we use the json.dump() method, it can take dictionary, output file, 
ensure_ascii and indent.
'''
person = {
    'name' : 'Jose',
    'country' : 'Colombia',
    'city' : 'Medellin',
    'skills' : ['Python', 'SQL', 'Excel']
}
# indent make the json file easy to read
with open('./json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4) 
'''
json_example.json
{
    "name": "Jose",
    "country": "Colombia",
    "city": "Medellin",
    "skills": ["Python","SQL","Excel"]
}
''' 

#----------------File with csv Extension-----------------------
'''
CSV stands for comma separated values. CSV is a simple file format used to store 
tabular data, such as a spreadsheet or database. 
CSV is a very common data format in data science.
'''

import csv

with open('/home/jbernal/Python/30DaysOfPython/day_19_File_Handling/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Columns name are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}')
            line_count += 1
    print(f'Number of line: {line_count}')
'''
Columns name are: name, country, city, skills
        Asabeneh is a teacher. He lives in Finland, Helsinki
Number of line: 2
'''

#-----------------File with xlsx extension-------------------
# o read excel files we need to install xlrd package.
# We will cover this after we cover package installing using pip.

# import xlrd
# excel_book = xlrd.open_workbook('example.xls')
# print(excel_book.nsheets)

