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

#-------------------------Unpacking items list-----------------------------------
lista = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lista # * resto de los elementos 
print(first_item)
print(second_item)
print(third_item)
print(rest)

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          
print(second)         
print(third)          
print(rest)           
print(tenth)

#-------------------------Slicing items from list------------------------
print(fruits[1:])
print(fruits[::2])
print(fruits[-3:])
print(fruits[::-2])

#--------------------------Modifying lists------------------------------
fruits[0] = 'Aguacate'
print(fruits)
fruits[1] = 'Apple'
print(fruits)

#------------------------Checking items in a list-----------------------
print('banana' in fruits)
exist = 'lemon' in fruits
print(exist)

#-----------------------Adding items to a list--------------------------
fruits.append('mango')
print(fruits)
fruits.append('cereza')
print(fruits)

#inserting items into a list
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

#-----------------------Removing item from list------------------------
#remove the item first ocurrence
fruits.remove('apple')
print(fruits)
fruits.remove('mango')
print(fruits)

#Removing items using pop
fruits.pop()  #remove last item
print(fruits)
fruits.pop(1)
print(fruits)

#Removing items using Del
del fruits[2]
print(fruits)

del fruits[1:]
print(fruits)

del fruits #to delete the list completely




