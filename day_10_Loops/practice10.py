#-----------------WHILE LOOP--------------------
# It is used to execute a block repeatedly until a given condition is satisfied.

#### When the condition become false, the line of code after the loop will be continued to be executed.
count = 0
while count < 5:
    print(count)
    count += 1
'''
0
1
2
3
4
'''

#### If we are interested to run block of code once the condition is no longer true, we can use else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)
'''
0
1
2
3
4
5
'''

#-----------------Break and continue in While -----------------------
#### break: it used break when like to get out of or stop loop
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
'''
0
1
2
'''

#### continue: with the continue statement we can skip the current iteration, and continue with the next.
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
'''
0
1
2
4
'''

#-----------------For loop with list-----------------------
#### Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0,1,2,3,4,5]

for i in numbers:
    print(i)
'''
0
1
2
3
4
5
'''

#--------------- for loop with string ------------------------
lenguage = 'Python'

for letter in lenguage:
    print(letter)
'''
P
y
t
h
o
n
'''

#------------------ for loop with tuple ---------------------------
numbers = (0,1,2,3,4,5)

for number in numbers:
    print(number)
'''
0
1
2
3
4
5
'''

#---------------- for loop with dictionary ---------------------------
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

#### recorre solo las keys del diccionario
for key in person:
    print(key)
'''
first_name
last_name
age
country
is_marred
skills
address
'''

#### get both keys and values printed out. items devuelve una tupla con la llae y el valor 
for key, value in person.items():
    print(key, value)
'''
first_name Asabeneh
last_name Yetayeh
age 250
country Finland
is_marred True
skills ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
address {'street': 'Space street', 'zipcode': '02210'}
'''

#### otra forma de obtener ambos datos: kays y values
for datos in person.items():
    key = datos[0]
    value = datos[1]
    print(f'Llave:{key}     Valor:{value}')
'''
Llave:first_name     Valor:Asabeneh
Llave:last_name     Valor:Yetayeh
Llave:age     Valor:250
Llave:country     Valor:Finland
Llave:is_marred     Valor:True
Llave:skills     Valor:['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
Llave:address     Valor:{'street': 'Space street', 'zipcode': '02210'}
'''


#---------------- for loops with set ------------------------------- 
#### recorre el set con los elementos sin orden definido
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
'''
Microsoft
Oracle
Google
IBM
Facebook
Amazon
Apple
'''

#### loop set with enumerate. Forma optima de recorrer un set. 
numeros = {2,34,11,6,32}
for num in enumerate(numeros):
    print(num)
'''
(0, 32)
(1, 2)
(2, 34)
(3, 6)
(4, 11)
'''

#### No puedes recorrer los elementos del set por el indice con range
'''
for num in range(len(numeros)):
    print(numeros[num])
TypeError: 'set' object is not subscriptable
'''

#-----------------------Recorriendo dos listas al mismo tiempo------------------------
#### Para que funcione, las listas deben ser del mismo size.
#### funciona tambien para mas de dos listas
animales = ['perro', 'gato', 'leon', 'tigre']
numeros = [2,56,12,8]

for animal, numero in zip(animales, numeros):
    print(f'recorriendo lista1 : {animal}')
    print(f'recorriendo lista2 : {numero}')
'''
recorriendo lista1 : perro
recorriendo lista2 : 2
recorriendo lista1 : gato
recorriendo lista2 : 56
recorriendo lista1 : leon
recorriendo lista2 : 12
recorriendo lista1 : tigre
recorriendo lista2 : 8
'''

#-----------------------Break and continue en bucle For----------------------------
#break is used when we like to stop aur loop before it is completed
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
#### the range(start, end, step) takes three parameters: starting, ending and increment.

#### Creating sequence using range
#### lista con numeros del 0 al 9
lista = list(range(10))
'''
print(lista)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

#### lista con numeros del 1 al 10
lista2 = list(range(1,11))
'''
print(lista2)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

#### conjunto con numeros pares
lista3 = set(range(0,11,2))
'''
print(lista3)
{0, 2, 4, 6, 8, 10}
'''

#### mostrar los numeros pares con for
for number in range(0,11,2):
    print(number)
'''
0
2
4
6
8
10
'''

#### Recorriendo valores mediante el indice. No es la forma optima de hacerlo
lenguage = 'python'
for i in range(len(lenguage)):
    print(lenguage[i])
'''
P
y
t
h
o
n
''' 

#-----------------------Forma optima de recorrer una lista-------------------------
#### Enumerate(): comprime los valores junto a sus indices en una tupla
numeros = [2,34,1,60,18]
for num in enumerate(numeros):
    print(type(num))
'''
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
'''

#### obtener indice y valor en una tupla
for num in enumerate(numeros):
    print(num)
'''
(0, 2)
(1, 34)
(2, 1)
(3, 60)
(4, 18)
'''

#### Acceder a los indices de las tuplas
for num in enumerate(numeros):
    print(num[0])
'''
0
1
2
3
4
'''

#### Acceder a los valores de las tuplas
for num in enumerate(numeros):
    print(num[1])
'''
2
34
1
60
18
'''    

#### Acceder a los indices y valores al mismo tiempo
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'indice: {indice}. Valor: {valor}')
'''
indice: 0. Valor: 2
indice: 1. Valor: 34
indice: 2. Valor: 1
indice: 3. Valor: 60
indice: 4. Valor: 18
'''

#------------------For else----------------------------
# los bucles for pueden contener al final un bloque else donde podras colocar acciones que se 
# realicen una sola vez. Se recorra o no el bucle, lo que esta dentro de else se va a ejecutar
for num in enumerate(numeros):
    print(num)
else:
    print('termino el programa')
'''
(0, 2)
(1, 34)
(2, 1)
(3, 60)
(4, 18)
termino el programa
'''

#------------------ for en una sola linea de codigo ----------------------
#### Util para simplificar codigo
numeros = [2,3,5,6,8]
# vamos a duplicar los valores de la lista
numeros_duplicados = [x*2 for x in numeros]
'''
print(numeros_duplicados)
[4, 6, 10, 12, 16]
'''

#-----------------------Nested for loop-----------------------
#### Recorre una lista dada como valor en un diccionario
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
'''
JavaScript
React
Node
MongoDB
Python
'''


#----------------------Pass----------------------------
#In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors.
for number in range(6):
    pass 
