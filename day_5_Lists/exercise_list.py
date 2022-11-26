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

#Escriba un programa en Python para obtener el número más pequeño de una lista
def min_list(lista):
    min = lista[0]

    for i in lista:
        if i < min:
            min = i
    return min

print(min_list([4,2,8,0,1]))

# Escriba un programa en Python para contar el número de cadenas donde la longitud de la 
# cadena es 2 o más y el primer y último carácter de la cadena son el mismo.
def match_word(words):
    match = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            match += 1
    return match

print(match_word(['abc', 'xyz', 'aba', '1221']))

