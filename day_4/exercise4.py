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
print(company2.replace('All', 'Everyone'))

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech = 'Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon'
print(tech.split(','))




