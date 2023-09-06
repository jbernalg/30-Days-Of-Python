'''
Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
- Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar 
su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, 
sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
'''

import time

def retardate_execution(num1:int, num2:int, sleep:int):
    time.sleep(sleep)
    return num1 + num2

print(retardate_execution(1, 2, 3))
