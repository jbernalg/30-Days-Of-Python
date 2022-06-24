#-----------------WHILE LOOP--------------------
#It is used to execute a block repeatedly until a given condition is satisfied.
#When the condition become false, the line of code after the loop will be continued to be executed.

count = 0
while count < 5:
    print(count)
    count += 1

#If we are interested to run block of code once the condition is no longer true, we can use else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)

#-----------------Break and continue-----------------------
#break: it used break when like to get out of or stop loop
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

#continue: with the continue statement we can skip the current iteration, and continue with the next.
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

#-----------------For loop-----------------------
#Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0,1,2,3,4,5]

for i in numbers:
    print(i)

#for loop with string
lenguage = 'Python'

for letter in lenguage:
    print(letter)

for i in range(len(lenguage)):
    print(lenguage[i])

#for loop with tuple
numbers = (0,1,2,3,4,5)

for number in numbers:
    print(number)

#for loop with dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

#keys
for key in person:
    print(key)

#get both keys and values printed out 
for key, value in person.items():
    print(key, value)

#loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print(company)

#-----------------------Break and continue Parte 2----------------------------
#break is used when we like to stop aur loop before  it is completed
number = (0,1,2,3,4,5)

for number in numbers:
    print(number)
    if number == 3:
        break

#continue is used when we like to skip some of the steps in the iteration of the loop
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if  number != 5 else print('loop´s end')
print('outside the loop')

#------------------------The range function-----------------------
#the range(start, end, step) takes three parameters: starting, ending and increment.
#Creating sequence using range
lista = list(range(10))
print(lista)

lista2 = list(range(1,11))
print(lista2)

lista3 = set(range(0,11,2))
print(lista3)

for number in range(0,11,2):
    print(number)
    

#-----------------------Nested for loop-----------------------
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)





