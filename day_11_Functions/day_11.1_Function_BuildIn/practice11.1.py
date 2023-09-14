#------------------Function Build In ----------------------

#### max(): encuentra el valor mayor de un iterable. aplcia para valores numericos
numeros = [2,45,21,67,33]   #lista
num_mayor = max(numeros)
'''
print(num_mayor)
67
'''
numeros = {2,45,21,67,33}   #set
num_mayor = max(numeros)
'''
print(num_mayor)
67
'''

#### min(): encuentra el valor menor de un iterable. aplcia para valores numericos
numeros = [2,45,21,67,33]   #lista
num_menor = min(numeros)
'''
print(num_menor)
2
'''

#### round(): redondeando un numero pasando la cantidad de decimales que queremos
numero = 12.348675
num_round = round(numero, 3)
'''
print(num_round)
12.349
'''

#### bool(): retorna False si se le pasa un 0, vacio, False o None. True en caso contrario
result = bool(0)
'''
print(result)
False
'''

result = bool()
'''
print(result)
False
'''

result = bool([1,'True'])
'''
print(result)
True
'''
result = bool([0])
'''
print(result)
True
'''

#### all(): evalua todos los elementos de un iterable.
# devuelve False si al menos hay un elemento con valor 0, vacio, False o None
result = all([None,1,True])
'''
print(result)
False
'''

#### sum(): suma los numero de un iterable
numeros = {1,5,2,8,7}
suma = sum(numeros)
'''
print(suma)
23
'''

#### range(): genera una secuencia de numeros
rango = range(1,20)
'''
print(list(rango))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
'''

#### abs(): devuelve el valor absoluto de un numero
absoluto = abs(-23)
'''
print(absoluto)
23
'''

#### round(): redondea un numero a una cantidad especifica de decimales
redondeo = round(123, 2)
'''
print(redondeo)
123
'''

redondeo = round(123.456, 2)
'''
print(redondeo)
123.46
'''

#### sorted(): ordena una secuencia
tupla = (3,1,6,2,7,5)
ordenado = sorted(tupla)
'''
print(ordenado)
[1, 2, 3, 5, 6, 7]
'''

#### zip(): se utiliza para combinar elementos de dos o mas secuencias (lista, tuplas)
# en tuplas emparejadas. Ambas secuencia deben tener el mismo size
nombres = ['Marco', 'Daniel', 'Salomon']
edades = [22,18,27]

# combinamos los nombres y edades en tuplas emparejadas
datos_personales = list(zip(nombres, edades))

# recorres la lista
'''
for nombre, edad in datos_personales:
    print(f'Nombre: {nombre}. Edad: {edad}')
Nombre: Marco. Edad: 22
Nombre: Daniel. Edad: 18
Nombre: Salomon. Edad: 27
'''