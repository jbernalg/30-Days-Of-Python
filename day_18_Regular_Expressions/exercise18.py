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

# Write a Python program that matches a string that has an a followed by zero or one 'b'.
def text_match(text):
    patterns = 'ab?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match('ab'))
print(text_match('abbb'))
print(text_match('a'))

# Write a Python program that matches a string that has an a followed by three 'b'
def text_match(text):
    patterns = 'ab{3}?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match('abbb'))
print(text_match('abbcbbb'))

# Write a Python program that matches a string that has an a followed by two to three 'b'
def text_match(text):
    patterns = 'ab{2,3}?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match('ab'))
print(text_match('aabbac'))

# Write a Python program to find sequences of lowercase letters joined with a underscore
def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

print(text_match('aab_cbb'))
print(text_match('abc_ABC'))

# Write a Python program to find the sequences of one upper case letter followed by lower case letters. 
def text_match(text):
   patterns = '[A-Z]+[a-z]+$'
   if re.search(patterns, text):
       return 'Found a match!'
   else:
       return 'Not matched!'

print(text_match('Python'))
print(text_match('python'))

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
def text_match(text):
   patterns = 'a.*?b$'
   if re.search(patterns, text):
       return 'Found a match!'
   else:
       return 'Not matched!'

print(text_match('cfbabdb'))
print(text_match('abaaaccc'))

# Write a Python program that matches a word at the beginning of a string.
def text_match(text):
   patterns = '^\w+'
   if re.search(patterns, text):
       return 'Found a match!'
   else:
       return 'Not matched!'

print(text_match('The quick brown'))
print(text_match(' the quick brown'))

# Write a Python program that matches a word at the end of string, with optional punctuation
def text_match(text):
   patterns = '\w+\S*$'
   if re.search(patterns, text):
       return 'Found a match!'
   else:
       return 'Not matched!'

print(text_match('The quick brown.'))
print(text_match('The quick brown '))

# Write a Python program that matches a word containing 'z'.
def text_match(text):
   patterns = '\w*z.\w*'
   if re.search(patterns, text):
       return 'Found a match!'
   else:
       return 'Not matched!'

print(text_match('The quick brown the lazy'))
print(text_match('Python exercise'))

# Write a Python program that matches a word containing 'z', not at the start or end of the word.
def text_match(text):
   patterns = '\Bz\B'
   if re.search(patterns, text):
       return 'Found a match!'
   else:
       return 'Not matched!'

print(text_match('The quick brown the lazy'))
print(text_match('The zafari'))
print(text_match('The ratioz'))

