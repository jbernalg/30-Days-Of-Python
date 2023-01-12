'''
 Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero 
 o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(string1, string2):
    
    if string1.lower() == string2.lower():
        return False
    else:
        a = sorted(string1.lower())
        b = sorted(string2.lower())
        if a == b:
            return True
        else:
            return False

print(is_anagram('hola', 'loro'))
