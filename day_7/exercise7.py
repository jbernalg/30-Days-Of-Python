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


