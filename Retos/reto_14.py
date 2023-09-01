'''
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.
'''
def factorial(n):
    # caso base
    if n == 0:
        return 1
    # caso recursivo
    else:
        return n * factorial(n-1)

print(factorial(5))

'''
Calcular el n-ésimo número de la secuencia de Fibonacci utilizando recursividad.
'''
def fibonacci(n):
    # caso base
    if n <= 1:
        return n
    # caso recursivo
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(3))

'''
Calcular la suma de todos los elementos de una lista utilizando recursividad.
'''
def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([2,5,10]))