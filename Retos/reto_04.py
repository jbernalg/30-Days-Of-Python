'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def is_prime(num):
    for n in range(2, num):  # rango que va desde el 2 hasta el numero seleccionado
        if num % n == 0:     # comprueba si el numero es divisible por alguno de lo numeros del ciclo for
            print(f'{num} No es primo')
            return False

    print(f'{num} Es primo')
    return True

# Probamos la funcion para los numeros del 1 al 100
for i in range(100):
    if i <= 1:
        pass
    else:
        is_prime(i)

