'''
Crea un programa que determine si dos vectores son ortogonales.
- Los dos array deben tener la misma longitud.
- Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''

def ortogonalidad(list1, list2):
     
    # verificar que sean del mismo size
    if len(list1) == len(list2):
        
        # multiplicar elementos con la misma ubicacion y sumar
        result = 0
        for i in range(len(list1)):
            result += list1[i]*list2[i]

        # si la suma es 0 devolver True
        if result == 0:
            return True
        # si la suma es diferente de 0 devolver False
        else:
            return False
    # si no son del mismo size, devolver None
    else:
        return None
    
#### Test
print(ortogonalidad([1, 0],[0, -1])) # --> True
print(ortogonalidad([1, 0, 3],[0, -1, 2])) # --> False
print(ortogonalidad([1, 0, 3],[0, -1])) # --> None