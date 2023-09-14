'''
Enunciado: Dado un array de enteros ordenado y sin repetidos, 
- crea una función que calcule y retorne todos los que faltan entre el mayor y el menor.
- Lanza un error si el array de entrada no es correcto.
'''

def num_Perdidos(lista):

    # verificar que la lista sea de longitud mayor a 1
    if len(lista) <= 1:
        return None
    else:
        # verificar que la lista este ordenada
        band = lista[0]
        for num in lista:
            if num < band:
                return None
            else:
                band = num

        # guardar los numeros consecutivos que no esten en la lista
        list_perdidos = []
        init = lista[0]
        end = lista[-1]
        for num in range(init, end):
            if num not in lista:
                list_perdidos.append(num)

        return list_perdidos

#Test
print(num_Perdidos([2,5,18,23]))
print(num_Perdidos([2,1,18,23]))
print(num_Perdidos([1,10]))
print(num_Perdidos([2]))

# [2,5,18,23] --> [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22]
# [2,1,18,23] --> None
# [1,10] --> 2, 3, 4, 5, 6, 7, 8, 9]
# [2] --> None