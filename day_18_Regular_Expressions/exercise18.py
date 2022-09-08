#------------------------Exercise reGex---------------

# What is the most frequent word in the following  paragraph?
paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities 
to develop an application what else can you love'''

# Write a program to check that a string contains only a certain set of characters (a-z, A-Z, 0-9)
import re

def specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9. ]')
    string = charRe.search(string) 
    return not bool (string)

# re.complie compila un patron de expresion regular en un objeto de expresion regular que puede
# ser usado para las coincidencias usando match(), search()

print(specific_char('hola 123'))
print(specific_char('% & $'))

# Write  a program that matches a string that has an followed by zero or more b's
def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match('ac'))
print(text_match('abc'))
print(text_match('a'))
print(text_match('abb'))

# Write  a program that matches a string that has an followed by one or more b's
def text_match(text):
    patterns = 'ab+?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match('ab'))
print(text_match('acb'))

