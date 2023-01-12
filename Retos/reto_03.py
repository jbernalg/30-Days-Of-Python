'''
 * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de 
 Fibonacci empezando en 0.
 La serie Fibonacci se compone por una sucesión de números en la que el siguiente 
 siempre es la suma de los dos anteriores.
 0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci(num):
    print(0)
    print(1)
    band = 3
    num1 = 0
    num2 = 1

    while band < num:
        result = num1 + num2
        print(result)
        num1 = num2
        num2 = result
        band += 1


def fibonacci2(num):
    a, b = 0, 1
    for i in range(1,num):
        print(a)
        a, b = b, a+b

print(fibonacci(50))
print(fibonacci2(50))