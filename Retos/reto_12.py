'''
 Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras 
 dos cadenas como salida (out1, out2).
 - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
'''

texto1 = 'hola'
texto2 = 'mundo'

def del_character_common(texto1, texto2):
    
    # convertimos los textos en set
    set1 = set(texto1)
    set2 = set(texto2)
    
    # intersectamos para obtener los elementos comunes en ambos
    set_inter = set1.intersection(set2)

    # eliminamos los elementos comunes en ambos
    for elem in set_inter:
        salida1 = texto1.replace(elem,'')
        salida2 = texto2.replace(elem,'')

    return salida1, salida2

print(del_character_common(texto1, texto2))