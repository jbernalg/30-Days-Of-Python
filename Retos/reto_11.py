'''
 Crea un programa que comprueba si los paréntesis, llaves y corchetes de una 
 expresión están equilibrados.
 - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 - Expresión no balanceada: { a * ( c + d ) ] - 5 }
'''
#-------- Primera Solucion ------------------
# variable con la expresion

def ver_equilibrio(expression):

    # lista que almacena los signos abiertos
    list_signos_open = []

    # variable con los signos de agrupacion
    signos_agrup = '{([])}'

    #Diccionario de signos abiertos con su correspondientes signos cerrados
    bd_signos = {
        '(':')',
        '[':']',
        '{':'}'
    }

    # recorrer cada elemento de la expresion
    for elem in expression:
    
        # signos abiertos
        if elem in '([{':
            list_signos_open = list_signos_open + [elem]
    
        # signos cerrados
        elif elem in '}])':

            # caso para lista varia
            if len(list_signos_open) == 0:
                list_signos_open = list_signos_open + [-1]
                break
            # caso para lista no vacia    
            else:
                # buscamos el signo abierto correspondiente
                for key, value in bd_signos.items():
                    if value == elem:
                        var_comp = key
                        print(value)

                # si hace match con el signo buscado
                if var_comp == list_signos_open[-1]:
                    del list_signos_open[-1]
                # si no hace match
                else:
                    break
                
    if len(list_signos_open) == 0:
        return 'Esta Equilibrada'
    else:
        return 'No Equilibrada'
    
expression = '[[{[a * (c + d)]) - 5}]]'
print(ver_equilibrio(expression))