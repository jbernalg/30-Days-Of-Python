'''
Crea un programa que invierta el orden de una cadena de texto
 * Sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''
word = 'hola mundo'
print(word[::-1])

#----------- Otra forma de resolverlo------------------
def invert_string(string_phrase):

    list_character = list(string_phrase)
    list_invert = []

    for i in range(len(list_character)-1, -1, -1):
        list_invert.append(list_character[i])

    word_invert = ''.join(map(str, list_invert))
    return word_invert

print(invert_string('hola mundo'))