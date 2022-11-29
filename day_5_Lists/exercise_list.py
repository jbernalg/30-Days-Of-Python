#-----------------------Ejecicios---------------------

# 1. escriba un programa que sume todos los elementos de una lista
def sum_list(lista):
    count = 0

    for i in lista:
        count += i
    return count

print(sum_list([2,3,4]))

# 2. Escriba un programa en Python para multiplicar todos los elementos de una lista
def mult_list(lista):
    mult = 1

    for i in lista:
        mult *= i
    return mult

print(mult_list([2,5,2]))

# Escriba un programa en Python para obtener el número más grande de una lista.
def max_list(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

print(max_list([3,-2,0,10,4]))

#Escriba un programa en Python para obtener el número más pequeño de una lista
def min_list(lista):
    min = lista[0]

    for i in lista:
        if i < min:
            min = i
    return min

print(min_list([4,2,8,0,1]))

# Escriba un programa en Python para contar el número de cadenas donde la longitud de la 
# cadena es 2 o más y el primer y último carácter de la cadena son el mismo.
def match_word(words):
    match = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            match += 1
    return match

print(match_word(['abc', 'xyz', 'aba', '1221']))

# Escriba un programa en Python para obtener una lista, ordenada en orden creciente 
# por el último elemento de cada tupla de una lista dada de tuplas no vacías
def ultimo(n) :
    return n[-1]

def sort_list_tuples(lista):
    return sorted(lista, key=ultimo) #key:Una función a ejecutar para decidir el orden.

print(sort_list_tuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# Escriba un programa de Python para eliminar duplicados de una lista
def delete_dupl(lista):
    lista1 = set(lista)
    lista = list(lista1)
    return lista

print(delete_dupl([1,2,2,4,5,3,1]))

# 8. Escriba un programa en Python para comprobar si una lista está vacía o no.
def empty_list(lista):
    if len(lista) == 0:
        return True
    else:
        return False

print(empty_list([1,2,3]))

# Escriba un programa Python para clonar o copiar una lista.
def copy_list(lista):
    lista1 = lista.copy()
    return lista1

print(copy_list([1,2,3,4]))

# 10. Escriba un programa de Python para encontrar la lista
# de palabras que son más largas que n de una oracion dada
def word_long(oracion, n):
    txt = oracion.split(' ')
    word_list = [word for word in txt if len(word) > n]
    return word_list

oracion = 'Adios mundo cruel sol de oro y miel'
print(word_long(oracion, 3))

# Escriba una función de Python que tome dos listas y devuelva True 
# si tienen al menos un miembro común.
def compare_list(lista1, lista2):

    for i in lista1:
        if i in lista2:
            return True
            break
        else:
            continue
    return False

numbers = [1,3,5,7,9]
numbers2 = [2,4,5,8,10]
print(compare_list(numbers, numbers2))

# Escriba un programa de Python para imprimir una lista específica después de 
# eliminar los elementos 0, 4 y 5
def remove_index(lista):
    del lista[0]
    del lista[3:5]
    return lista

print(remove_index([1,3,4,5,7,9,10,12]))

# 13. Escriba un programa Python para generar una matriz 3D de 3*4*6 cuyos elementos sean *
array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

# 14. Escriba un programa Python para imprimir los números de una lista específica 
# después de eliminar los números pares de ella
def delete_pair(lista):
    numbers_odd = [odd for odd in lista if odd % 2 != 0]
    return numbers_odd

print(delete_pair([1,3,4,5,7,8,10,11]))

# 15. Escriba un programa de Python para mezclar e imprimir una lista específica.
from random import shuffle
color = ['naranja', 'rosado', 'azul', 'morado', 'verde']
shuffle(color)
print(color)

# 16. Escriba un programa Python para generar e imprimir una lista de los primeros y últimos 
# 5 elementos donde los valores son cuadrados de números entre 1 y 30 (ambos incluidos)
def print_values():
    lista = []
    for i in range(1,31):
        lista.append(i**2)
    print(lista[:5])
    print(lista[-5:])

print_values()

# 17. Escriba un programa en Python para generar e imprimir una lista a excepción de los primeros
#  5 elementos, donde los valores son cuadrados de números entre 1 y 30 (ambos incluidos).
def print_values2():
    lista = []
    for i in range(1,31):
        lista.append(i**2)
    print(lista[5:])
    
print_values2()

# 18. Escriba un programa en Python para generar todas las permutaciones de una lista en Python.
import itertools

def permut_list(lista):
    return list(itertools.permutations(lista))

number = [1,2,3]
print(permut_list(number))

# 19. Escriba un programa Python para obtener la diferencia entre dos listas.
lista1 = [4,8,12,3,6]
lista2 = [5,3,7,9,14]

def difference_lists(lista1, lista2):
    lista1_menos_lista2 = list(set(lista1) - set(lista2))
    lista2_menos_lista1 = list(set(lista2) - set(lista1))
    difference = lista1_menos_lista2 + lista2_menos_lista1
    return difference

print(difference_lists(lista1, lista2))

# 20. Escriba un programa de Python para acceder al índice de una lista.
def index_value(lista, value):
    if value in lista:
        return lista.index(value)
    else:
        return 'El elemento no esta en la lista'

print(index_value([1,2,3,4,5,6], 10))

# Otra alternativa
def index_values(lista):
    for num_index, num_val in enumerate(lista):
        print(num_index, num_val)

index_values([1,4,12,78,32,9])

# 21. Escriba un programa en Python para convertir una lista de caracteres en una cadena
def list_to_string(lista):
    text = ' '.join(lista)
    return text

print(list_to_string(['hola','nuevo','mundo']))

# 22. Escriba un programa Python para encontrar el índice de un elemento en una lista específica.
def index_value(lista, value):
    if value in lista:
        return lista.index(value)
    else:
        return 'El elemento no esta en la lista'

print(index_value([1,2,3,4,5,6], 1))

# 23. Escriba un programa Python para aplanar una lista poco profunda
import itertools

def merged_list(lista):
    return list(itertools.chain(*lista))

matrix = [[1,2,3], [5], [32, 91], [14, 20]]
print(merged_list(matrix))

# 24. Escriba un programa Python para agregar una lista a la segunda lista.
def combine_lists(lista1, lista2):
    return lista1 + lista2

numbers = [2,4,6]
numbers_odd = [7,9,1]
print(combine_lists(numbers, numbers_odd))
