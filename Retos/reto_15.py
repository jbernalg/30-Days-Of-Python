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
    
    #convertir en string para listar cada numero
    list_num = list(str(num))

    exponente = len(list_num)

suma = 0
for nume in list_num:
    suma += int(nume)**exponente

if suma == num:
    print(True)
else:
    print(False)