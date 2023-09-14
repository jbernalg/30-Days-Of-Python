'''
Dado un listado de números, encuentra el SEGUNDO más grande.
'''



def quick_Sort(lista):

    # utilizamos el ordenamiento rapido para ordenar la lista de menor a mayor
    if len(lista) <= 1:
        return lista
    
    # seleccion del pivot
    pivot = lista.pop()

    # 2 sublistas: menor y mayor que el pivot
    less_than_pivot = []
    greater_than_pivot = []

    # particionar la lista para agregar elementos a la sublista
    for element in lista:
        if element <= pivot:
            less_than_pivot.append(element)
        else:
            greater_than_pivot.append(element)

    # aplicar recursivamente la funcion a las sublistas
    sorted_less = quick_Sort(less_than_pivot)
    sorted_greater = quick_Sort(greater_than_pivot)

    # combinar las sublistas ordenadas
    return  sorted_less + [pivot] + sorted_greater

def second_largest(lista):
    
    lista_sorted = quick_Sort(lista)
    
    if len(lista) == 1:
        return lista[0]
    elif len(lista) == 0:
        return None
    
    return lista_sorted[-2]

lista = [5,1,7,9,10,23,14,2]

print(second_largest([5,1,7,9,10,23,14,2]))
print(second_largest([-2,-15,-13,-20]))
print(second_largest([5]))
print(second_largest([-1,0,3]))
print(second_largest([]))

# [5,1,7,9,10,23,14,2] --> 14
# [-2,-15,-13,-20] --> -13
# [5] --> 5
# [-1,0,3] --> 0
# [] --> None