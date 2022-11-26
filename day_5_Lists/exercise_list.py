#-----------------------Ejecicios---------------------

# 1. escriba un programa que sume todos los elementos de una lista
def sum_list(lista):
    count = 0

    for i in lista:
        count += i
    return count

print(sum_list([2,3,4]))

# 2. Escriba un programa en Python para multiplicar todos los elementos de una lista
def mult_list(lista):
    mult = 1

    for i in lista:
        mult *= i
    return mult

print(mult_list([2,5,2]))

# Escriba un programa en Python para obtener el número más grande de una lista.
def max_list(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

print(max_list([3,-2,0,10,4]))