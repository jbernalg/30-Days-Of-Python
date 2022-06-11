#-----------------------Create a list------------------------------
#list built in funtion
lista = list()

#empty list
empty_list = list()
print(len(empty_list))

#squares brackets []
lista = []
print(len(lista))

#List with initial values.
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Fruits: ', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetable: ', vegetables)
print('Number of vegetables: ',len(vegetables))
print('Animal Products: ', animal_products)
print('Number of animalproducts: ',len(animal_products))
print('Web Tecnologies: ',web_techs)
print('Number of Web: ',len(web_techs))
print('Countries: ', countries)
print('Number of countries: ', len(countries))

#List can have items of different data types
lista = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]
print(lista)

#--------------Accessing list items using indexing----------------------------
print(fruits[0])
print(fruits[2])
last_index = len(fruits) - 1
print(last_index)

print(fruits[-4])
print(fruits[-2])





