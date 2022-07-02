#----------------LOOPS----------------

from countries import countries
from countries_data import data


#Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)

number = 0
while  number < 11:
    print(number)
    number += 1

#Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)

number = 10
while number > -1:
    print(number)
    number -= 1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
hashtag = '#'
for element in range(7):
    print(hashtag)
    hashtag = hashtag + '#'

#Use nested loops to create the following:
hashtagH = '#'

for i in range(8):
    for j in range(8):
        hashtagH += ' #'
    print(hashtagH)
    hashtagH = '#'

#Print the following pattern:
for number in range(11):
    print(f'{number} x {number} = {number * number}')

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)


#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
count = 0
for i in range(101):
    count += i
print(f'The sum of all numbers is: {count}')

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
evenSum = 0
oddSum = 0
for i in range(101):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
print(f'The sum of all evens is {evenSum}. The sum of all odds is {oddSum}')

#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
 
for country in countries:
    if 'land' in country:
        print(country)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reverse = list()

for i in range(len(fruits) - 1, -1, -1):
    fruits_reverse.append(fruits[i])

print(fruits_reverse)

#Go to the data folder and use the countries_data.py file
#What are the total number of languages in the data
total_language = list()
i = 0
proof = list()

while i < len(data):

    for j in data[i]['languages']:
        total_language.append(j)
        
    for k in total_language:
        if k in proof:
            pass
        else:
            proof.append(k)
    
    total_language = list()
    i += 1
   
print(len(total_language))

#Find the ten most spoken languages from the data
total_language = list() # lista con los lenguajes de todos los paises
proof = list()          # lista que almacena los lenguaje de un pais momentaneamente
all_language = list()   # lista que contiene cada lenguaje
i = 0

while i < len(data):

    for j in data[i]['languages']:
        proof.append(j)
        total_language.append(j)

    for k in proof:
        if k in all_language:
            pass
        else:
            all_language.append(k)
    
    proof = list()
    i += 1

frecuency_languaje = list()
count = 0

for i in all_language:
    count = total_language.count(i)
    frecuency_languaje.append(count)
    count = 0

max_language = max(frecuency_languaje)
stop = 0
band = 0

for i in range(max_language, 0, -1):

    if i in frecuency_languaje:
        band = frecuency_languaje.index(i)
        print(all_language[band])
        stop += 1

    if stop == 10:
        break


#Find the 10 most populated countries in the world
print(data[2]['population'])
countries_population = list()
for i in data:
    countries_population.append(i.get('population'))

#print(countries_population)
countries_population.sort(reverse=True)
#print(countries_population)

count = 0

for j in countries_population:
    
    for i in range(len(data)):
        if data[i]['population'] == j:
            print(data[i]['name'])
            count += 1
    if count > 9:
        break




 






