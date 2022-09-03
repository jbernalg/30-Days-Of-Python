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

#-------------------findall------------------
# Return all the matches as a list
matches = re.findall('language', txt, re.I)
print(matches)

matches = re.findall('Python', txt, re.I)
print(matches)
# since we are using re.I both lowercase and uppercase letters are included
# If we do not have the re.I flag , then will have to write our pattern differently

matches = re.findall('Python|python', txt)
print(matches)

matches = re.findall('[Pp]ython', txt)
print(matches)

#------------Replacing a substring-----------------
match_replaced = re.sub('Python|python', 'Javascript', txt, re.I)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

#------------Splitting text using regEx split----------------
txt = '''I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people'''
print(re.split('\n', txt))

#----------------Writing RegEx patterns------------------
regex_pattern = r'apple'
txt = 'Apple and bananas are fruits. An old cliche says an apple'
matches = re.findall(regex_pattern, txt, re.I)
print(matches)

regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)

#--------------Square bracket---------------
#use to include lower and upper case
regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern, txt)
print(matches)

#-------------Escape character (\)-------------------
regex_pattern = r'\d' #d is a special character which mean digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'\d+'  # + mean one or more times
matches = re.findall(regex_pattern, txt)
print(matches)

#------------Period (.)-------------
regex_pattern = r'[a].' # this square brackets means a and . means any character except new line
txt = 'Apple and banana are fruits'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[a].+' # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)