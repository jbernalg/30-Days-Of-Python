'''
Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente
'''

def sets_arrays(list1:list, list2:list, band:bool):
    
    # si es verdadero devuelve la inteseccion
    if band:
        return list(set(list1).intersection(set(list2)))
    # si es falso devuelve la diferrencia simetrica
    else:
        return list(set(list1).symmetric_difference(set(list2)))


list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 3, 4, 5]
band = False

#### Test
print(sets_arrays(list1, list2, band)) # --> [2, 4, 7, 9] 
print(sets_arrays([1,4,6,7], [1,3,5,8], True)) # --> [1]
print(sets_arrays([1,4,6,7], [1,3,5,8], False)) # --> [3, 4, 5, 6, 7, 8]


#--------------- Otra forma de resolverlo ------------------
def sets_array2(list1:list, list2:list, band:bool):

    if len(list1) == 0 or len(list2) == 0:
        return None
    else:
        list3 = []
        if band:
            for i in list1:
                for j in list2:
                    if i == j and i not in list3:
                        list3 = list3 + [i]

        else:
            for i in list1:
                if i not in list2:
                    list3 = list3 + [i]
        
            for i in list2:
                if i not in list1:
                    list3 = list3 + [i]

        return list3

##### Test    
print(sets_array2([1,2,3,5],[2,2,7], True)) # -->  [2]
print(sets_array2([1,2,3,5],[2,2,7], False)) # --> [1, 3, 5, 7]
print(sets_array2([],[2,2,7], False)) # --> None