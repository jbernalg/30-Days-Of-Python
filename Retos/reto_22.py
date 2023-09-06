'''
Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
- El .txt se corresponde con las entradas de una calculadora.
- Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
- Soporta números enteros y decimales.
- Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
- El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
- Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
'''

def operation_arithem(string):
    
    f = open(f'./{string}')


    list_txt = f.read().splitlines()
    result = 0

    if list_txt[0].isnumeric():
        result = float(list_txt[0])
    else:
        return 'No ha podido resolver la operacion. Verifique la expresion'


    for i in range(1, len(list_txt), 2):

        if i + 1 <= len(list_txt) - 1:

            if list_txt[i] == '+':
                result += float(list_txt[i+1])
        
            elif list_txt[i] == '-':
                result -= float(list_txt[i+1])
        
            elif list_txt[i] == '*':
                result *= float(list_txt[i+1])
        
            elif list_txt[i] == '/':
                result = result / float(list_txt[i+1])
            
            else:
                return 'No ha podido resolver la operacion. Verifique la expresion'
        
        else:
            return 'No ha podido resolver la operacion. Verifique la expresion'

    return str(result)

print(operation_arithem('reto_22.txt'))