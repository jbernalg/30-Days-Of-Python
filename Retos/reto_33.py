'''
Algoritmos de busqueda
'''

######### Busqueda binaria

def binary_search(lista, elemento):

    # definimos los valores inicial y final de la lista
    init = 0
    end = len(lista) - 1

    # si el elemento buscado coincide con el primer valor de la lista, retornar posicion
    if lista[init] == elemento:
        return init
    # si el elemento buscado coincide con el ultimo valor de la lista, retornar posicion
    elif lista[end] == elemento:
        return end
    # buscar elemento dentro de la lista
    else:

        while init <= end:
            # valor medio de la lista
            mid = (init + end) // 2
            # si el valor medio de la lista coincide, retornar valor medio
            if lista[mid] == elemento:
                return mid
            # si el valor medio de la lista es menor, asignar al valor inicial la suma de
            # valor medio mas 1
            elif lista[mid] < elemento:
                init = mid + 1
            # si el valor medio de la lista es mayor, asignar al valor final la resta
            # del valor medio menos 1
            else:
                end = mid - 1
        # si no encuentra el elemento, retornar -1
        return -1
    
# Test
print(binary_search([1,3,5,7,9,12,15,20], 12))
print(binary_search([1,3,5,7,9,12,15,20], 13))
print(binary_search([1,3,5,7,9,12,15,20], 1))
print('--------------------------------')

# [1,3,5,7,9,12,15,20], 12 --> 5
# [1,3,5,7,9,12,15,20], 13 --> -1
# [1,3,5,7,9,12,15,20], 1 --> 0


######## Busqueda Lineal

def sequential_search(lista, elemento):
    # recorre toda la lista
    for i in enumerate(lista):
        # si el valor de la lista coincide con el elemento, retornar posiciondel valor de lista
        if i[1] == elemento:
            return i[0]
            # sale del loop
            break
        
    return -1

# Test
print(sequential_search([1,2,4,5,7,9,15,1,22], 15))
print(sequential_search([1,2,4,5,7,9,15,1,22], 3))
print(sequential_search([1,2,4,5,7,9,15,1,22], 22))
print('--------------------------------')
# [1,2,4,5,7,9,15,1,22], 15 --> 6
# [1,2,4,5,7,9,15,1,22], 3 --> -1
# [1,2,4,5,7,9,15,1,22], 8 --> 8

##### Busqueda Exponencial

def exponential_search(lista, elemento):
    # si el elemento coincide con el primer valor de la lista, retornar 0
    if lista[0] == elemento:
        return 0
    
    n = len(lista)
    i = 1
    
    # estimar un rango aproximado en el que se encuentra el elemento
    while i < n and lista[i] <= elemento:
        i *= 2

    # aplicar la busqueda binaria en el rango aproximado
    init = i//2
    end = min(i, n - 1)

    while init <= end:
        
        mid = (init + end)//2

        if lista[mid] == elemento:
            return mid
        elif lista[mid] < elemento:
            init = mid + 1
        else:
            end = mid - 1
        
    return -1
    
print(exponential_search([1,4,6,9,12,23,32,45,47,49], 45))
print(exponential_search([1,4,6,9,12,23,32,45,47,49], 44))
print(exponential_search([1,4,6,9,12,23,32,45,47,49], 49))
print('--------------------------------')

# [1,4,6,9,12,23,32,45,47,49], 45 --> 7
# [1,4,6,9,12,23,32,45,47,49], 44 --> -1
# [1,4,6,9,12,23,32,45,47,49], 49 -->


############# Busqueda de Saltos
import math

def jump_search(lista, elemento):
    # si el elemento coincide con el primer valor de la lista, retornar 0
    if lista[0] == elemento:
        return 0
    elif lista[len(lista)-1] == elemento:
        return len(lista)-1
    
    # calculo del size del bloque
    n = len(lista)
    size_block = int(math.sqrt(n))

    # iniciamos en cero el indice
    i = 0

    # determinamos el ancho del bloque
    while i < n and lista[i] < elemento:
        i += size_block

    # aplicar la busqueda lineal al bloque determinado
    block_init = i - size_block

    for j in range(block_init, min(i, n - 1)):
        if lista[j] == elemento:
            return j

    return -1

# Test
print(jump_search([1,4,6,9,12,23,32,45,47,49], 49))
print(jump_search([1,4,6,9,12,23,32,45,47,49], 1))
print(jump_search([1,4,6,9,12,23,32,45,47,49], 50))

# [1,4,6,9,12,23,32,45,47,49], 49 --> 9
# [1,4,6,9,12,23,32,45,47,49], 1 --> 0
# [1,4,6,9,12,23,32,45,47,49], 50 --> -1