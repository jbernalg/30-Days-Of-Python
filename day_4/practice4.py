#Escape Sequences in String
#new line
print('I am Happy.\nAnd you?')

#Tab means
print('Days\tTopic\tExercises')
print('Day 1\t3\t5')

#Back Slash
print('This is a backslash symbol (\\)')

#Single quote
print('En cada lenguaje de rogramacion se comienza con  \"Hello Word\"')

#String formatting
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

