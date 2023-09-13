#----------------------- LAMBDA ---------------------------------
'''
Crea funciones anonimas (No tiene nombre) que pueden ser almacenadas en variables.
- Nos ayuda a ahorrar lineas de codigo.
- Util cuando queremos realizar una operacion sencilla y rapida
- Retorna automaticamente un valor
- No es apta para cuando se requiere ejecutar mas de una instruccion
'''

#### funcion lambda para multiplicar por 2 un numero
mult = lambda x:x*2
'''
print(mult(3))
6
'''

#------------------- Filter ------------------------------
'''
Es un tipo de bucle que permite aplicar una funcion sobre un iterable
'''

# funcion que determina si un numero es par
def is_par(num):
    if num % 2 == 0:
        return True
    
#### aplicando la funcion is_par a una lista mediante filter
numeros = [1,2,3,6,8,11,23,22,30]
numeros_pares = filter(is_par, numeros)

# la variable contiene un objeto de tipo filter.
'''
print(numeros_pares)
<filter object at 0x7fb0d2263f40>
'''

# Debemos convertir la variable en una lista para obtener los valores
'''
print(list(numeros_pares))
[2, 6, 8, 22, 30]
'''

#### utilizando lambda en vez de la funcion como argumento
numeros_pares = list(filter(lambda numero:numero%2 == 0, numeros))
print(numeros_pares)