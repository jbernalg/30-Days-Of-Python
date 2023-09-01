#------------------Escape Sequences in String-------------------------
######## new line \n
text = 'I am Happy.\nAnd you?'
'''
I am Happy.
And you?
'''

######## Tab means \t
text2 = 'Days\tTopic\tExercises'
'''
Days    Topic   Exercises
'''

text3 = 'Day 1\t3\t5'
'''
Day 1   3       5
'''

#
######### Back Slash. Colocar \ en una cadena
text4 = 'This is a backslash symbol (\\)'
'''
This is a backslash symbol (\)
'''

######### Single quote. Colocar "" en una cadena de texto
text5 = 'En cada lenguaje de rogramacion se comienza con  \"Hello Word\"'
'''
En cada lenguaje de rogramacion se comienza con  "Hello Word"
'''
print(text5)

#-----------------------String formatting---------------------------------
######### old style string formatting. Only string
first_name ='Jose'
last_name = 'Bernal'
language = 'Python'

formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
'''
I am Jose Bernal. I teach Python
'''

########## Strings and numbers
radius = 10
pi = 3.14
area = pi*radius**2
formated_string2 = 'El area del circulo con radio %s es %.3f' %(radius, area)
'''
El area del circulo con radio 10 es 314.000
'''

########## list Strings
python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string3 = 'Las siguientes librerias son de Python: %s' %(python_libraries)
'''
Las siguientes librerias son de Python: ['Django', 'Flask', 'Numpy', 'Pandas']
'''

########### New style string formatting. Only string
first_name ='Jose'
last_name = 'Bernal'
language = 'Python'
formated_string4 = 'I am {} {}. I teach {}'.format(first_name,last_name,language)
'''
I am Jose Bernal. I teach Python
'''

############# Only Numbers
a = 4
b = 3
#print('{} + {} = {}'.format(a, b, a + b))
#print('{} / {} = {:.4f}'.format(a, b, a / b))
'''
4 + 3 = 7
4 / 3 = 1.3333
'''

######### Strings and numbers
formated_string5 = 'El area del circulo con radio {} es {:.2f}'.format(radius, area)
'''
El area del circulo con radio 10 es 314.00
'''

######## f-Strings
formated_string6 = f'{a}/{b} = {a / b:.3f}'
'''
4/3 = 1.333
'''

formated_string7 = f'{a}**{b} = {a**b:.2f}'
'''
4**3 = 64.00
'''

print(formated_string7)


#-----------------Python string as sequences of characters------------------------------

########## unpacking characters
language = 'python'
a,b,c,d,e,f = language
'''
print(a)
p
print(b)
y
print(c)
t
print(d)
h
print(e)
o
print(f)
n
'''

######## Accessing characters in string by index
first_letter = language[0]
'''
print(first_letter)
p
'''
last_letter = language[-1]
'''
print(last_letter)
n
'''

######## Slicing  python string
'''
print(language[3:6])
hon
print(language[-3:])
hon
'''

######## Reversing a string
invert_language = language[::-1]
'''
nohtyp
'''

######## Skipping Characters While Slicing
character_odd = language[0:6:2]
'''
pto
'''

print(character_odd)

#----------------String Methods-----------------------
'''
- Los metodos en python se aplican seguidos del objeto. Ej: objeto.metodo()
- Las funciones en python se aplican teniendo al objeto como parametro. Ej: funcion(objeto)
- Todos los metodos son funciones pero no todas las funciones son metodos
- los metodos son funciones especificas de un objeto. En caso de no ser una funcion de un 
objeto, entonces no es un metodo
'''

###### dir(): Es una funcion. Muestra todos los metodos que se pueden aplicar al objeto pasado
'''
print(dir('hello world'))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
 '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
 '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 
 'zfill']
''' 

######## capitalize(): Converts the first charactersof the string to capital letter
#######
challenge = 'thirty days of python'
primer_letra_mayusc = challenge.capitalize()
'''
Thirty days of python
'''

######## count(): return occurrences of substring in string. count(substring,start,end). Devuelve cero si no encuentra coincidencias
########
# numeros de y en la cadena
challenge = 'thirty days of python'
n_y = challenge.count('y')
'''
print(n_y)
3
'''

#numero de y en un rango de la cadena
challenge = 'thirty days of python'
n_y_range = challenge.count('y',7,14)
'''
print(n_y_range)
1
'''

#numero de th en challenge
challenge = 'thirty days of python'
n_th = challenge.count('th')
'''
print(n_th)
2
'''
######## len(): Es una funcion que cuenta los caracteres que posse una cadena
########
challenge = 'thirty days of python'
n_caractteres = len(challenge)
'''
print(n_caractteres)
21
'''

######## endswith(): Checks if a string ends with a specified ending. Return True or False
########
challenge = 'thirty days of python'
end_on = challenge.endswith('on')
'''
print(end_on)
True
'''

challenge = 'thirty days of python'
end_ty = challenge.endswith('ty')
'''
print(end_ty)
False
'''

######## expandtabs(): Replaces tab character with spaces, default tab size is 8.
########
challenge = 'thirty\tdays\tof\tpython'
tab_8 = challenge.expandtabs()
'''
print(tab_8)
thirty  days    of      python
'''

tab_10 = challenge.expandtabs(10)
'''
print(tab_10)
thirty    days      of        python
'''

######### find(): Return the index of the first occurrence of a substring
#########
challenge = 'thirty days of python'
find_y = challenge.find('y')
'''
print(find_y)
5
'''

find_da = challenge.find('da')
'''
print(find_da)
7
'''

######## rfind(): Return the index of the last occurence oh a substring
########
index_y = challenge.rfind('y')
'''
print(index_y)
16
'''

######### index(): Returns the lowest index of a substring. Si no hay coincidencias arroja una excepcion
########
challenge = 'thirty days of python of year'
index_of = challenge.index('of')
'''
print(index_of)
12
'''
#additional arguments indicate starting and ending index. Busqueda selectiva
index_of2 = challenge.index('ye',14) 
'''
print(index_of2)
25
'''

######### rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index
#########
challenge = 'thirty days of python of year'
'''
print(challenge.rindex('of'))
22
'''

######### isalnum(): Checks alphanumeric character
#########
challenge = 'thirty days of python of year'
'''
print(challenge.isalnum())
False
'''

challenge = '30daysofpython'
'''
print(challenge.isalnum())
True
'''

challenge = 'DaysThirtyOfPython'
'''
print(challenge.isalnum())
True
'''

####### isalpha(): Checks if all string elements are alphabet character(a - z). space not allowed
#######
challenge = 'DaysThirtyOfPython'
'''print(challenge.isalpha())
True
'''

challenge = '123'
'''
print(challenge.isalpha())
False
'''

######## isdecimal(): Checks if all string elements are decimal (0 - 9)
########
challenge = '123'
'''
print(challenge.isdecimal())
True
'''

challenge = 'ThirtyDaysOfPython'
'''
print(challenge.isdecimal())
False
'''

######## isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
########
challenge = 'two'
'''
print(challenge.isdigit())
False
'''

challenge = '10021'
'''
print(challenge.isdigit())
True
'''

###### isnumeric(): Checks if al characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
######
num = '12'
'''
print(num.isnumeric())
True
'''

num = '\u00BD'
'''
print(num.isnumeric())
True
'''

###### isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
######
challenge = '30daysofpython'
'''
print(challenge.isidentifier())
False
'''

challenge = 'thirtydaysofython'
'''
print(challenge.isidentifier())
True
'''

######## isupper(): Checks if all alphabet characters in the string are uppercase
########
challenge = 'thirtydaysofython'
'''
print(challenge.isupper())
False
'''

######## islower(): Checks if all alphabet characters in the string are lowercase
########
challenge = 'thirtydaysofython'
'''
print(challenge.islower())
True
'''

######## join(): Returns a concatenated string
########
web_tech = ['HTML', 'CSS', 'Javascript', 'React']
'''
print(' '.join(web_tech))
HTML CSS Javascript Reac
'''

######## strip(): Removes all given characters starting from the beginning and end of the string
########
challenge = 'thirty days of pythooon'
'''
print(challenge.strip('noth'))
irty days of py
'''

######## replace(): Replaces substring with a given string
########
challenge = 'thirty days of python'
'''
print(challenge.replace('python', 'coding'))
thirty days of coding
'''

######## split(): Splits the string, using given string or space as a separator. Return a list
########
challenge = 'thirty days of python'
'''
print(challenge.split())
['thirty', 'days', 'of', 'python']
'''

######## title(): Returns a title cased string
########
challenge = 'thirty days of python'
'''
print(challenge.title())
Thirty Days Of Python
'''

######## swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
########
challenge = 'thirty days of python'
'''
print(challenge.swapcase())
THIRTY DAYS OF PYTHON
'''

########## startswith(): Checks if String Starts with the Specified String
##########
challenge = 'thirty days of python'
'''
print(challenge.startswith('thirty'))
True


print(challenge.startswith('30'))
False
'''
