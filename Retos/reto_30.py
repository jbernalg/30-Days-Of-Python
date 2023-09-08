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



##### Ordenamiento por seleccion

def selectionSort(lista:list, orden:str):
    
    # creamos una lista que contendra los valores ordenandos
    # y una variable que servira de bandera en el bucle
    lista_ord = []
    band = True

    # orden ascendente
    if orden == 'Asc':       

        while band:
            val_search = lista[0]
            for i in lista:
                if i < val_search:
                    val_search = i
            

            lista_ord = lista_ord + [val_search]
            lista.remove(val_search)

            if len(lista) == 0:
                band = False    

        return lista_ord
    
    # orden descendente
    elif orden == 'Desc':

        while band:
            val_search = lista[0]
            for i in lista:
                if i > val_search:
                    val_search = i
            

            lista_ord = lista_ord + [val_search]
            lista.remove(val_search)

            if len(lista) == 0:
                band = False    

        return lista_ord 

    # otro tipo de orden
    else:
        return 'Ingrese un tipo de orden correcto!'       

###### Test
print(selectionSort([3,1,2,2,5,4,6], 'Asc'))
print(selectionSort([3,1,2,2,5,4,6], 'Desc'))
print(selectionSort([3,1,2,2,21,4,6], 'Asc'))
print(selectionSort([3,1,2,2,5,4,6], 'desc'))

# [3,1,2,2,5,4,6], 'Asc' --> [1, 2, 2, 3, 4, 5, 6]
# [3,1,2,2,5,4,6], 'Desc' --> [6, 5, 4, 3, 2, 2, 1]
# [3,1,2,2,21,4,6], 'Asc' --> [1, 2, 2, 3, 4, 6, 21]
# [3,1,2,2,5,4,6], 'desc' --> Ingrese un tipo de orden correcto!



#------------- Ordenamiento por Fusion

def merge_sort(lista, orden:str):

    if orden == 'Asc' or orden == 'Desc':

        if len(lista) <= 1:
            return lista
    
        # dividir la lista en dos mitades
        mitad = len(lista) // 2
        lado_der = lista[mitad:]
        lado_izq = lista[:mitad]

        # llamada recursiva para llegar a listas con un solo elemento
        lado_der = merge_sort(lado_der, orden)
        lado_izq = merge_sort(lado_izq, orden)

        # combinamos las mitades ordenadas con otra funcion
        return merge(lado_izq, lado_der, orden)

    else:
        return 'Ingrese orden correcto!'
    

def merge(izq, der, orden):

    # creamos una lista que almacenara la lista ordenada
    result = []

    # creamos dos variables como bandera para salir del bucle
    ind_izq, ind_der = 0, 0

    # orden Ascendente
    if orden == 'Asc':
        
        # combinamos las sublista
        while ind_izq < len(izq) and ind_der < len(der):

            if izq[ind_izq] < der[ind_der]:
                result.append(izq[ind_izq])
                ind_izq += 1
            else:
                result.append(der[ind_der])
                ind_der += 1

        # agregar elementos restantes si los hay
        result.extend(izq[ind_izq:])
        result.extend(der[ind_der:])
    
    # Orden descendente
    else:

         # combinamos las sublista
        while ind_izq < len(izq) and ind_der < len(der):

            if izq[ind_izq] > der[ind_der]:
                result.append(izq[ind_izq])
                ind_izq += 1
            else:
                result.append(der[ind_der])
                ind_der += 1

        # agregar elementos restantes si los hay
        result.extend(izq[ind_izq:])
        result.extend(der[ind_der:])
    
    return result

##### Test    
print(merge_sort([3,1,2,2,5,4,6], 'Desc'))
print(merge_sort([3,1,2,2,5,4,6], 'Asc'))
print(merge_sort([3,1,2,2,15,4,6], 'Desc'))
print(merge_sort([3,1,2,2,5,4,6], 'daesc'))

# [3,1,2,2,5,4,6], 'Desc' --> [6, 5, 4, 3, 2, 2, 1]
# [3,1,2,2,5,4,6], 'Asc' --> [1, 2, 2, 3, 4, 5, 6]
# [3,1,2,2,15,4,6], 'Desc' --> [15, 6, 4, 3, 2, 2, 1]
# [3,1,2,2,5,4,6], 'daesc' --> Ingrese orden correcto!