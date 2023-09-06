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


#--------------- Otra solucion ----------------------------
import asyncio
import time

# Corrutina
async def add_action(num1:int, num2:int, wait_time: int):

    # guarda el tiempo de inicio de tarea
    init_time = time.time()

    # realiza la tarea
    add = num1 + num2
    
    # espera el tiempo especificado
    await asyncio.sleep(wait_time)

    # guarda el tiempo de finalizacion de la tarea
    finish_time = time.time()

    # imprimir el resultado y tiempo que tomo realizar la tarea
    print(f'{num1} + {num2} = {add}. \tTiempo tomado: {round(finish_time - init_time, 3)} segundos')

    
# funcion principal que realiza el llamado de las corrutinas
async def main():

    await asyncio.gather(
        add_action(1,1,5),
        add_action(5,5,3),
        add_action(10,10,1)
    )


if __name__ == '__main__':

    # guarda inicio de tiempo de ejecucion
    init_time = time.time()

    # inicia la funcion main
    asyncio.run(main())

    # guarda el tiempo de finalizacion de ejecucion
    finish_time = time.time()

    # imprimir el tiempo total de ejecucion de las tareas
    print(f'Tiempo de ejecucion total: {round(finish_time - init_time, 3)} segundos')