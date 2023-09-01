'''
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o 
no palíndromos.
- Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha 
que de derecha a izquierda.
- NO se tienen en cuenta los espacios, signos de puntuación y tildes.
- Ejemplo: Ána lleva al oso la avellana.
'''
import re

texto = 'Ána lleva al oso la Avellana.'

def is_palindrome(texto):
    # convertir texto a minuscula
    texto = texto.lower()

    # sustituir tildes
    tildes = {
        'á':'a',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u',
        'ü':'u'
    }

    for char in texto:
        if char in tildes:
            texto = texto.replace(char,tildes[char])

    # Regex encuentra todo aquello que no sea una palabra
    regular_expression = r'[^\w]'

    texto_clear = re.sub(regular_expression,'',texto)

    if texto_clear == texto_clear[::-1]:
        return True
    else:
        return False

print(is_palindrome(texto))

