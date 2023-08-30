#---------------DATOS COMPUESTOS-------------------------
'''
Son datos que contienen diferentes tipos de datos que se
pueden agrupar
'''

#------------------------ Lista
# es un tipo de matriz (array) que permite agrupar datos
# Podemos modificar los elementos de una lista o agregar nuevos
lista = ["Lucas", 'Dalto', True, 177.2]
print(lista)

# mostrar un elemento de la lista
print(lista[2])

# modificar elemento de la lista
lista[3] = 'Medellin'
print(lista[3])

#---------------------- Tupla
# Es un array que agrupa datos pero no permite modificarlos
# o agregar nuevos
tupla = ("Lucas", 'Dalto', True, 177.2)
print(tupla)

# mostrar elementos de tupla
print(tupla[0])

# no permite la modificacion de elementos
#tupla[0] = 'Jose'
#print(tupla[0])

#-------------------- Set
# permiten agrupar datos sin un orden fijo
# no permite modificar o agregar elementos nuevos
conjunto = {"Lucas", 'Dalto', True, 177.2}

# No permite acceder a los elementos por el indice
# solo se hace mediante un bucle
#print(conjunto[1])

# No almacena datos duplicados
conjunto = {"Lucas", 'Dalto', True, 177.2, 'Dalto'}
print(conjunto)


#------------------- Diccionario
# permite acceder a los elementos mediante un nombre (clave)
# que nosotros le asociamos a cada elemento (valor)
diccionario = {
    'nombre' : 'Miguel',
    'canal' : 'Bola con B',
    'feliz' : True,
    'altura' : 177.3,
    'duplicado' : 'Bola con B'
}

print(diccionario['duplicado'])

# mostrar todos los elementos del diccionario
print(diccionario)