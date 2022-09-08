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



