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