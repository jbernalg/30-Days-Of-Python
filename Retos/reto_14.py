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

