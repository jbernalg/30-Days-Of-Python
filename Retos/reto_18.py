'''
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
La función recibirá dos parámetros:
- Un array que sólo puede contener String con las palabras "run" o "jump"
- Un String que represente la pista y sólo puede contener "_" (suelo)  o "|" (valla)

La función imprimirá cómo ha finalizado la carrera:
- Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará 
el símbolo de esa parte de la pista.
- Si hace "jump" en "_" (suelo), se variará la pista por "x".
- Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
'''

# funcion recibe un array con solo dos palabras y un string con solo '_' y '|'
def eval_carrera(estado_carrera:list, obstaculos:str):

    # creamos dos variables que almacenen el resultado y estado de la carrera
    band = True
    pista = ''

    # verificacion
    ver_estado = ['run','jump']
    ver_obstaculos = ['_', '|']

    for estado in estado_carrera:
        if estado not in ver_estado:
            return f'la accion {estado} no corresponde a la carrera'

    for obs in obstaculos:
        if obs not in ver_obstaculos:
            return f'El obstaculo {obs} que no corresponde a la carrera'
        
    if len(estado_carrera) != len(obstaculos):
        return 'Hay acciones demas u obstaculos demas en la carrera'

    # recorremos el string y comparamos cada elemento con los estados de la carrera
    ind = 0
    for obs in obstaculos:
        if obs == '_' and estado_carrera[ind] == 'run':
            pista += '_'

        elif obs == '_' and estado_carrera[ind] == 'jump':
            pista += 'x'  

        elif obs == '|' and estado_carrera[ind] == 'jump':
            pista += '|'
        
        elif obs == '|' and estado_carrera[ind] == 'run':
            pista += '/'
        

        ind += 1

    if 'x' in pista or '/' in pista:
        band = False

    return f'{band}, {pista}'    


##########################################################
# Test
print(eval_carrera(['run', 'jump', 'jump', 'run'], '_||_'))
print(eval_carrera(['run', 'jump', 'wild', 'run'], '_||_'))        
print(eval_carrera(['run', 'jump'], '_||_'))
print(eval_carrera(['run', 'jump', 'jump', 'run'], '_|?_'))
print(eval_carrera(['run', 'jump', 'jump', 'run'], '|__|'))

# ['run', 'jump', 'jump', 'run'], '_||_'    -->   True, _||_
# ['run', 'jump', 'wild', 'run'], '_||_'    -->   la accion wild no corresponde a la carrera
# ['run', 'jump'], '_||_'   -->     Hay acciones demas u obstaculos demas en la carrera
# ['run', 'jump', 'jump', 'run'], '_|?_'    -->   El obstaculo ? que no corresponde a la carrera
# ['run', 'jump', 'jump', 'run'], '|__|'    -->   False, /xx/