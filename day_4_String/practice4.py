#------------------Escape Sequences in String-------------------------
#new line \n
text = 'I am Happy.\nAnd you?'

#Tab means \t
text2 = 'Days\tTopic\tExercises'
text3 = 'Day 1\t3\t5'

#Back Slash. Colocar \ en una cadena
text4 = 'This is a backslash symbol (\\)'

#Single quote. Colocar "" en una cadena de texto
text5 = 'En cada lenguaje de rogramacion se comienza con  \"Hello Word\"'

print(text5)

#-----------------------String formatting---------------------------------
#old style string formatting
#only string
first_name ='Jose'
last_name = 'Bernal'
language = 'Python'

formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)

#other alternative
#print('I am %s %s. I teach %s' %(first_name, last_name, language))

#Strings and numbers
radius = 10
pi = 3.14
area = pi*radius**2
formated_string2 = 'El area del circulo con radio %s es %.3f' %(radius, area)

#list Strings
python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string3 = 'Las siguientes librerias son de Python: %s' %(python_libraries)

#New style string formatting. Only string
formated_string4 = 'I am {} {}. I teach {}'.format(first_name,last_name,language)

#other alternative
#print('I am {} {}. I teach {}'.format(first_name,last_name,language))

#only numbers
a = 4
b = 3
#print('{} + {} = {}'.format(a, b, a + b))
#print('{} / {} = {:.4f}'.format(a, b, a / b))

#Strings and numbers
formated_string5 = 'El area del circulo con radio {} es {:.2f}'.format(radius, area)

#f-Strings
formated_string6 = f'{a}/{b} = {a / b:.3f}'
formated_string7 = f'{a}**{b} = {a**b:.2f}'

print(formated_string7)

#-----------------Python string as sequences of characters------------------------------
#unpacking characters
language = 'python'
a,b,c,d,e,f = language
#print(a)
#print(b)
#print(c)
#print(d)
#print(e)
#print(f)

#Accessing characters in string by index
first_letter = language[0]

last_letter = language[-1]

#Slicing  python string
#print(language[3:6])
#print(language[-3:])

#Reversing a string
invert_language = language[::-1]

#Skipping Characters While Slicing
character_odd = language[0:6:2]

print(character_odd)

#----------------String Methods-----------------------
# Los metodos en python se aplican seguidos del objeto. Ej: objeto.metodo()
# Las funciones en python se aplican teniendo al objeto como parametro. Ej: funcion(objeto)

#dir(): muestra todos los metodos que se pueden aplicar al objeto pasado
#print(dir('hello world'))

challenge = 'thirty days of python'

#capitalize(): Converts the first charactersof the string to capital letter
primer_letra_mayusc = challenge.capitalize()

#count(): return occurrences of substring in string. count(substring,start,end)
n_y = challenge.count('y')
#numero de y en un rango de busqueda
n_y_range = challenge.count('y',7,14)
#numero de th
n_th = challenge.count('th')

#endswith(): Checks if a string ends with a specified ending. Return True or False
end_on = challenge.endswith('on')
end_ty = challenge.endswith('ty')

#expandtabs(): Replaces tab character with spaces, default tab size is 8.
challenge = 'thirty\tdays\tof\tpython'
tab_8 = challenge.expandtabs()
tab_10 = challenge.expandtabs(10)

#find(): Return the index of the first occurrence of a substring
challenge = 'thirty days of python'
find_y = challenge.find('y')
find_da = challenge.find('da')

#rfind(): Return the index of the last occurence oh a substring
index_y = challenge.rfind('y')

#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index 
print(challenge.index('of'))
print(challenge.index('of',8))

#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index
print(challenge.rindex('of'))

#isalnum(): Checks alphanumeric character
print(challenge.isalnum())
challenge = '30daysofpython'
print(challenge.isalnum())
challenge = 'DaysThirtyOfPython'
print(challenge.isalnum())

#isalpha(): Checks if all string elements are alphabet character(a - z). space not allowed
print(challenge.isalpha())
challenge = '123'
print(challenge.isalpha())

#isdecimal(): Checks if all string elements are decimal (0 - 9)
print(challenge.isdecimal())
challenge = 'ThirtyDaysOfPython'
print(challenge.isdecimal())

#isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'two'
print(challenge.isdigit())
challenge = '10021'
print(challenge.isdigit())

#isnumeric(): Checks if al characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '12'
print(num.isnumeric())
num = '\u00BD'
print(num.isnumeric())

#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30daysofpython'
print(challenge.isidentifier())
challenge = 'thirtydaysofython'
print(challenge.isidentifier())

#isupper(): Checks if all alphabet characters in the string are uppercase
print(challenge.isupper())

#islower(): Checks if all alphabet characters in the string are lowercase
print(challenge.islower())

#join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'Javascript', 'React']
print(' '.join(web_tech))

#strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythooon'
print(challenge.strip('noth'))

#replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

#split(): Splits the string, using given string or space as a separator
print(challenge.split())

#title(): Returns a title cased string
print(challenge.title())

#swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
print(challenge.swapcase())

#startswith(): Checks if String Starts with the Specified String
print(challenge.startswith('thirty'))
print(challenge.startswith('30'))

