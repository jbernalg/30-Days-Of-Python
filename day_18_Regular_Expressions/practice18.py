 # ------------------Regular Expressions---------------------
'''
RegEx is a special text string that helps to find patterns in data.
A regEx can be used to check if some pattern exists in a different data type.
After importing the module we can use it to detect or find patterns.
To find a patterns we use different set of re character sets that allow 
to search for a macth in a string
'''
import re

#--------------------Methods in re Module-------------------

#------------------- Match --------------------------

##### Seaches only in the beginning of the first line of the string and return matched 
# objects if found

txt = 'I love to teach python'
match = re.match('I love to teach', txt, re.I)
'''
print(match)
<re.Match object; span=(0, 15), match='I love to teach'>
'''

##### Get the starting and ending position of the match as tuple
span = match.span()
'''
print(span) 
(0, 15)
'''

##### Find the start and stop position from the span
start, end = span  
'''
print(start, end) 
0 15
'''

##### Extrae los chars contenidos entre la posicion inicial y final
substring = txt[start:end]
'''
print(substring)
I love to teach
'''

##### The match function returns an object only if the text starts with the pattern
txt = 'I love to teach python'
match = re.match('I like to teach', txt, re.I)
'''
print(match)
None
'''

# -------------------Search----------------------

##### Returns a match object if there is one anywhere in the string, 
# including multiline strings 
txt = '''Python is the most beautifull language 
that a human being has ever created
I recommend python for a first programming language'''

# objeto match
match = re.search('first', txt, re.I)
'''
print(match)
<re.Match object; span=(101, 106), match='first'>
'''

#### Obtener la posicion inicial y final de la coincidencia en una tupla
span = match.span()
'''
print(span)
(101, 106)
'''

#### asignar los valores de la posicion de la coincidencia a dos variables 
start, end = span
'''
print(start, end)
101 106
'''
#### Obtener el texto buscado mediante la posicion
substring = txt[start:end]
'''
print(substring)
first
'''

#-------------------findall------------------
##### Return all the matches as a list
txt = '''Python is the most beautifull language 
that a human being has ever created
I recommend python for a first programming language'''

matches = re.findall('language', txt, re.I)
'''
print(matches)
['language', 'language']
'''

matches = re.findall('Python', txt, re.I)
'''
print(matches)
['Python', 'python']
'''

# since we are using re.I both lowercase and uppercase letters are included
# If we do not have the re.I flag , then will have to write our pattern differently
matches = re.findall('Python|python', txt)
'''
print(matches)
['Python', 'python']
'''

matches = re.findall('[Pp]ython', txt)
'''
print(matches)
['Python', 'python']
'''

#------------Replacing a substring-----------------
txt = '''Python is the most beautifull language 
that a human being has ever created
I recommend python for a first programming language'''

#### Reemplazar python por Javascript
match_replaced = re.sub('Python|python', 'Javascript', txt, re.I)
'''
print(match_replaced)
Javascript is the most beautifull language 
that a human being has ever created
I recommend Javascript for a first programming language
'''

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
'''
print(matches)
I am teacher and  I love teaching. 
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. 
Does this motivate you to be a teacher?
'''


#------------Splitting text using regEx split----------------
txt = '''I am teacher and I love teaching.
There is nothing as 
rewarding as educating 
and empowering people'''

#### Crea una lista donde cada elemento sea las lineas del texto
list_line = re.split('\n', txt)
'''
print(list_line)
['I am teacher and I love teaching.', 'There is nothing as ', 
 'rewarding as educating ', 'and empowering people']
'''

#----------------Writing RegEx patterns------------------
txt = 'Apple and bananas are fruits. An old cliche says an apple'

#### Retorna una lista con el patron dado encontrado en txt
regex_pattern = r'apple'
matches = re.findall(regex_pattern, txt, re.I)
'''
print(matches)
['Apple', 'apple']
'''

#### Si no se coloca re.I, debe tenerse en cuenta dentro del patron
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['Apple', 'apple']
'''

#--------------Square bracket---------------

#### Use to include lower and upper case
regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['Apple', 'banana', 'apple']
'''

#-------------Escape character (\)-------------------

txt = '''This regular expression example was made on December 6,  
2019 and revised on July 8, 2021'''

#### d is a special character which mean digits
# encuentra todos los digitos dentro de txt y devuelve una lista
regex_pattern = r'\d' 
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']
'''

#### + mean one or more times
regex_pattern = r'\d+'  
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['6', '2019', '8', '2021']
'''

#------------Period (.)-------------
txt = 'Apple and banana are fruits'

#### this square brackets means a and . means any character except new line
regex_pattern = r'[a].' 
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['an', 'an', 'an', 'a ', 'ar']
'''

##### . any character, + any character one or more times
regex_pattern = r'[a].+' 
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['and banana are fruits']
'''

#---------------Zero or more times (*)---------------------
txt = 'Apple and banana are fruits'

#### . any character, *any character zero or more times
regex_pattern = r'[a].*'  
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['and banana are fruits']
'''

#---------------Zero or one time (?)----------------
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''

#### ? means here that '-' is optional
regex_pattern = r'[Ee]-?mail' 
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['e-mail', 'email', 'Email', 'E-mail']
'''

#---------------Quantifier in regEx-----------------
txt = '''This regular expression example was made on December 6,  
2019 and revised on July 8, 2021'''

#### digit exactly four times
regex_pattern = r'\d{4}' 
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['2019', '2021']
'''

#### numeros de 1 o 4 digitos
regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['6', '2019', '8', '2021']
'''

#---------------cart ^----------------
txt = '''This regular expression example was made on December 6,  
2019 and revised on July 8, 2021'''

#### start with
regex_pattern = r'^This' # ^ means starts with
matches = re.findall(regex_pattern, txt)
'''
print(matches) 
['This']
'''

#--------------Negation----------------
txt = '''This regular expression example was made on December 6,  
2019 and revised on July 8, 2021'''

# ^ in set character means negation, not A to Z, no space
regex_pattern = r'[^A-Za-z ]+'  
matches = re.findall(regex_pattern, txt)
'''
print(matches)
['6,', '2019', '8,', '2021']
'''
