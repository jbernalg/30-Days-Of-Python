'''
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento 
final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''
import re



def count_words(text):
    # dejamos todo el texto en minuscula
    text = text.lower()

    # dividir cada palabra y guardar en una lista
    text_splitted = text.split(' ')

    # Regex encuentra todo lo que no sea una palabra o espacio
    regular_expression = r'[^\w\s]'

    # creamos un diccionario para almacenar las palabras y su numero de apariciones
    word_repetitions = {}

    # recorremos cada palabra del texto
    for word in text_splitted:

        # contamos los signos de puntuacion contenidos en cada palabra
        mathes = re.findall(regular_expression, word)
    
        # si hay al menos uno, lo eliminamos
        if len(mathes) > 0:
            word = re.sub(regular_expression, "", word)

        # si la palabra no esta en el diccionario la agregamos
        if word not in word_repetitions:
            word_repetitions[word] = 1
        # si la palabra ya esta en el diccionario le sumamos 1
        else:
            word_repetitions[word] += 1

    # sumamos todas las palabras del diccionario
    final_count = sum(word_repetitions.values())

    # imprimimos resultados
    print(f'Cantidad de palabras : {final_count}')
    print(f'Palabras junto a su frecuencia : \n{word_repetitions}')

text = 'Hola mundo, hola mUndo otra vez MUNDO:'
count_words(text)