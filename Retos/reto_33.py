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

# [1,2,4,5,7,9,15,1,22], 15 --> 6
# [1,2,4,5,7,9,15,1,22], 3 --> -1
# [1,2,4,5,7,9,15,1,22], 8 --> 8