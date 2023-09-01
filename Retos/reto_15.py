'''
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
- Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
- Un número de Armstrong es aquel que es igual a la suma de sus dígitos elevados 
a la potencia del número de cifras.
- 153: 1^3 + 5^3 + 3^3 = 153
'''

num = 153

def is_num_armstrong(num):
    
    # Convertir en string para listar cada numero
    list_num = list(str(num))

    # calculamos el exponente de la potencia
    exponente = len(list_num)

    # sumamo cada numero elevado a la potencia dada
    suma = 0
    for nume in list_num:
        suma += int(nume)**exponente

    # True si es un numero armstrong. Caso contrario False
    if suma == num:
        return True
    else:
        return False
    
print(is_num_armstrong(num))
print(is_num_armstrong(100))
print(is_num_armstrong(1634))

'''
Cuantos numeros de armstrong estan contenidos en el rango de 1 a 1000?
'''
count = 0
for i in range(1001):
    if is_num_armstrong(i): 
        print(i)
        count += 1

print(f'Existen {count} de numeros de armstrong en el rango dado')
