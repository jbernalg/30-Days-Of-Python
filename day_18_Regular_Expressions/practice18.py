 # ------------------Regular Expressions---------------------
 # RegEx is a special text string that helps to find patterns in data.
 # A regEx can be used to check if some pattern exists in a different data type

 #-------------------The re Module-----------------------
 # after importing the module we can use it to detect or find patterns
import re

#--------------------Methods in re Module-------------------
# to find a patterns we use different set of re character sets that allow to search for a macth in a string

# Match
# seaches only in the beginning of the first line of the string and return matched objects if found
txt = 'I love to teach python'
match = re.match('I love to teach', txt, re.I)
print(match)

span = match.span()
print(span) # get the starting and ending position of the match as tuple

