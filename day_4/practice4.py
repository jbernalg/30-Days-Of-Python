#------------------Escape Sequences in String-------------------------
#new line
print('I am Happy.\nAnd you?')

#Tab means
print('Days\tTopic\tExercises')
print('Day 1\t3\t5')

#Back Slash
print('This is a backslash symbol (\\)')

#Single quote
print('En cada lenguaje de rogramacion se comienza con  \"Hello Word\"')

#-----------------------String formatting---------------------------------
#old style string formatting
#only string
first_name ='Jose'
last_name = 'Bernal'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
#other alternative
print('I am %s %s. I teach %s' %(first_name, last_name, language))


#Strings and numbers
radius = 10
pi = 3.14
area = pi*radius**2
formated_string = 'El area del circulo con radio %s es %.3f' %(radius, area)
print(formated_string)

#list Strings
python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string = 'Las siguientes librerias son de Python: %s' %(python_libraries)
print(formated_string)

#New style string formatting
#only string
formated_string = 'I am {} {}. I teach {}'.format(first_name,last_name,language)
print(formated_string)
#other alternative
print('I am {} {}. I teach {}'.format(first_name,last_name,language))

#only numbers
a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} / {} = {:.4f}'.format(a, b, a / b))

#Strings and numbers
print('El area del circulo con radio {} es {:.2f}'.format(radius, area))

#f-Strings
print(f'{a}/{b} = {a / b:.3f}')
print(f'{a}**{b} = {a**b:.2f}')

#-----------------Python string as sequences of characters------------------------------
#unpacking characters
language = 'python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Accessing characters in string by index
first_letter = language[0]
print(first_letter)

last_letter = language[-1]
print(last_letter)

#Slicing  python string
print(language[3:6])
print(language[-3:])

#Reversing a string
greeting = 'Hello Word'
print(greeting[::-1])

#Skipping Characters While Slicing
print(greeting[0:10:2])

#----------------String Methods-----------------------
#capitalize(): Converts the first charactersof the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize())




