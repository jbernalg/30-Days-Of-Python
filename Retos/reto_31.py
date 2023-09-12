'''
Crea una función que reciba un texto y muestre cada palabra en una línea,
formando un marco rectangular de asteriscos.
- ¿Qué te parece el reto? Se vería así:
   **********
   * ¿Qué   *
   * te     *
   * parece *
   * el     *
   * reto?  *
   **********
'''
text = '¿Qué te parece el reto?'
def format_text(text:str):

    # crear una lista donde cada elemento es una palabra
    list_text = text.split(' ')

    # crear una lista con el numero de caracteres de cada palabra
    length_word = []
    for word in list_text:
        length_word = length_word + [len(word)]

    # determinar la palabra con mayor numero de caracteres
    word_max = max(length_word)

    # crear lineas al inicio y al final
    # sumamos 4 a word_max
    char_lines = word_max + 4

    # linea inicio  
    print('*'*char_lines)

    for i in enumerate(length_word):
        # calcular numero de espacios
        num_space = word_max - i[1]
        char_space = ' '*num_space
        print(f'* {list_text[i[0]]}{char_space} *')

    #linea final
    print('*'*char_lines)

##### Test
format_text('hola mundo! buenos dias!!!') 
# ***********
# * hola    *
# * mundo!  *
# * buenos  *
# * dias!!! *
# ***********