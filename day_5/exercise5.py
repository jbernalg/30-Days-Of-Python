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


