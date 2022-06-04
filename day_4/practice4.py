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

#count(): return occurrences of substring in string. count(substring,start,end)
print(challenge.count('y'))
print(challenge.count('y',7,14))
print(challenge.count('th'))

#endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))
print(challenge.endswith('ty'))

#expandtabs(): Replaces tab character with spaces, default tab size is 8.
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

#find(): Return the index of the first occurrence of a substring
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('da'))

#rfind(): Return the index of the last occurence oh a substring
print(challenge.rfind('y'))

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



