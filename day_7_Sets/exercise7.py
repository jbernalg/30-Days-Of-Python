#SETS
it_companies = {'Facebbok', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
new_companies = {'Whatsapp', 'Lenovo', 'Sony', 'Tik Tok'}
it_companies.update(new_companies)
print(it_companies)

#Remove one of the companies from the set it_companies
remove_company = it_companies.pop()
print(it_companies)
print(remove_company)

#What is the difference between remove and discard
#Remove elimina un elemento del set siempre y cuando tal elemento exista en el set
#De lo contrario, el metodo arroja error.
#Discard elimina un elemento del set exista o no exista en el set. 
#No devuelve un error

#Join A and B
print(A.union(B))

#Find A intersection B
print(A.intersection(B))

#Is A subset of B?
print(A.difference(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
print(A.union(B))
print(B.union(A))

#What is the symmetric difference between A and B?
print(A.symmetric_difference(B))

#Delete the sets completely
del A

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
length_list = len(age)
age = set(age)
length_set = len(age)
print(f'{length_list}, {length_set}')

#Explain the difference between the following data types: string, list, tuple and set

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence = set(sentence.split())
print(len(sentence))


