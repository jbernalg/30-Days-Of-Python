#Declare an empty list
lista = list()

#Declare a list with more than 5 items
lista = [1,2,3,4,5]

#Find the length of your list
print(len(lista))

#Get the first item, the middle item and the last item of the list
print(lista[0])
print(lista[2])
print(lista[len(lista) - 1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Roberto', 'Aguilar', 1.72, 'soltero', 'Nicaragua']
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[len(it_companies) - 1])

#Print the list after modifying one of the companies
it_companies[4] = 'Acer'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('IT')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Ryzen')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = 'RYZEN'
it_companies.remove('IT')
print(it_companies)

#Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

#Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

print(sorted(it_companies, reverse=True))

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

it_companies.sort()
print(it_companies)

#Slice out the first 3 companies from the list
print(it_companies[:3])

#Slice out the last 3 companies from the list
print(it_companies[len(it_companies) - 3:])

#Slice out the middle IT company or companies from the list
print(it_companies[3:6])

#Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(3)
print(it_companies)

#Remove the last IT company from the list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(len(it_companies) - 1)
print(it_companies)

#Remove all IT companies from the list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

skill = front_end + back_end
print(skill)

#Copy the joined list and assign it to a variable full_stack.
full_stack = skill.copy()
print(full_stack)

#Insert Python and SQL after Redux
full_stack.insert(5,'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


