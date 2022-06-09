#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
print('Thirty ' + 'Days ' + 'Of ' + 'Python') 

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
string1 = 'Coding '
string2 = 'For '
string3 = 'All'
complet = string1 + string2 + string3
print(complet)

#Declare a variable named company and assign it to an initial value "Coding For All"
company = 'Coding For All'
print(company)

#Print the length of the company string using len() method and print()
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string
print(company[7:])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
company2 = company.replace('Coding', 'Python')
company2 = company2.replace('All', 'Everyone')
print(company2)

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech = 'Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
print(tech.split(','))

#What is the character at index 0 in the string Coding For All.
print(company[:1])

#What is the last index of the string Coding For All.
print(len(company) - 1)

#What character is at index 10 in "Coding For All" string.
print(company[10:11])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
acompany2 = company2[0:1] + company2[7:8] + company2[11:12]
print(acompany2)

#Create an acronym or an abbreviation for the name 'Coding For All'.
acompany = company[0:1] + company[7:8] + company[11:12]
print(acompany)

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
company = 'Coding For All People'
print(company.rfind('l'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence:
print(sentence.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence:
print(sentence[31:55])

#Find the position of the first occurrence of the word 'because' in the following sentence:
print(sentence.index('because'))

#Does ''Coding For All' start with a substring Coding?
company = 'Coding For All'
print(company.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      ' 
print(sentence.strip(' '))

#Which one of the following variables return True when we use the method isidentifier():
sentence = '30DaysOfPython'
sentence1 = 'Thirty_days_of_python'
print(sentence.isidentifier())
print(sentence1.isidentifier())

#Join the following list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(libraries))

#Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge. \nI just wonder what is next.')

#Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity\nAsabenh\t250\tFinland\tHelsinki')

#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square')





