 # ------------------Regular Expressions---------------------
 # RegEx is a special text string that helps to find patterns in data.
 # A regEx can be used to check if some pattern exists in a different data type

 #-------------------The re Module-----------------------
 # after importing the module we can use it to detect or find patterns
import re

#--------------------Methods in re Module-------------------
# to find a patterns we use different set of re character sets that allow to search for a macth in a string

# -------------------Match--------------------
# seaches only in the beginning of the first line of the string and return matched objects if found
txt = 'I love to teach python'
match = re.match('I love to teach', txt, re.I)
print(match)

span = match.span()
print(span) # get the starting and ending position of the match as tuple

start, end = span  # find the start and stop position from the span
print(start, end) 
substring = txt[start:end]
print(substring)

# The match function returns an object only if the text starts with the pattern
match = re.match('I like to teach', txt, re.I)
print(match)

# -------------------Search----------------------
# Returns a match object if there is one anywhere in the string, including multiline strings 
txt = '''Python is the most beautifull language that a human being has ever created
I recommend python for a first programming language'''

match = re.search('first', txt, re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

#-------------------findball------------------
# Return all the matches as a list
matches = re.findall('language', txt, re.I)
print(matches)

