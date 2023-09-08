'''
Crea una función que ordene y retorne una matriz de números.
- La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional 
"Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''

#### Ordenamiento Burbuja

def bubbleSort(lista:list, orden:str):
    
    # orden ascendente
    if orden == 'Asc':
    
        band = True
        while(band):
            
            band = False
            for i in range(len(lista)-1):   
                if lista[i] > lista[i+1] and i + 1 < len(lista):
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    band = True
        return lista
    # orden descendente
    elif orden == 'Desc':
        
        band = True
        while(band):
            
            band = False
            for i in range(len(lista)-1):   
                if lista[i] < lista[i+1] and i + 1 < len(lista):
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    band = True
        return lista
    
    # orden incorrecto
    else:
        return 'Ingrese un tipo de orden correcto!'

###### Test
print(bubbleSort([3,1,2,7,5,4,6], 'Asc'))
print(bubbleSort([3,1,2,7,5,4,6], 'Desc'))
print(bubbleSort([3,1,2,7,5,4,6], 'asc'))

# [3,1,2,7,5,4,6], 'Asc' --> [1, 2, 3, 4, 5, 6, 7]
# [3,1,2,7,5,4,6], 'Desc' --> [7, 6, 5, 4, 3, 2, 1]
# [3,1,2,7,5,4,6], 'asc' --> Ingrese un tipo de orden correcto!



##### Ordenamiento por Insercion

def insertionSort(lista:list, orden:str):

    # creamos una lista vacia que contendra los valores ordenados
    lista_ord = []

    # agregar el primer elemento a la lista ordenada
    lista_ord = lista_ord + [lista[0]]

    # orden ascendente
    if orden == 'Asc':
        
        # recorremos los elementos de la lista y comparamos con elementos de lista ordenada
        for i in range(1,len(lista)):
    
            for j in range(i - 1, -1, -1):
                if lista_ord[j] <= lista[i]:
                    lista_ord.insert(j + 1, lista[i])
                    break
            
                else:
                    if j == 0:
                        lista_ord.insert(0, lista[i])
            
        return lista_ord
    
    # orden descendente
    elif orden == 'Desc':

        # recorremos los elementos de la lista y comparamos con elementos de lista ordenada
        for i in range(1,len(lista)):
    
            for j in range(i - 1, -1, -1):
                if lista_ord[j] >= lista[i]:
                    lista_ord.insert(j + 1, lista[i])
                    break
            
                else:
                    if j == 0:
                        lista_ord.insert(0, lista[i])
            
        return lista_ord
    else:
        return 'Ingrese un tipo de orden correcto!'

##### Test
print(insertionSort([3,1,2,2,5,4,6], 'Desc'))
print(insertionSort([3,1,2,2,5,4,6], 'Asc'))
print(insertionSort([3,1,7,2,5,4,6], 'Desc'))
print(insertionSort([3,1,2,2,5,4,6], 'aesc'))

# [3,1,2,2,5,4,6], 'Desc' --> [6, 5, 4, 3, 2, 2, 1]
# [3,1,2,2,5,4,6], 'Asc' --> [1, 2, 2, 3, 4, 5, 6]
# [3,1,7,2,5,4,6], 'Desc' --> [7, 6, 5, 4, 3, 2, 1]
# [3,1,2,2,5,4,6], 'aesc' --> Ingrese un tipo de orden correcto!


lista = [3,1,2,2,5,4,6]