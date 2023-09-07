'''
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra  que calcule el 
mínimo común múltiplo (mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

def mcm(num1:int, num2:int):

    if num1 < 1 or num2 < 1:
        return None
    else:
        # definimos el mayor y menor
        if num1 > num2:
            num1, num2 = num2, num1
        elif num1 == num2:
            return None
        
        sum_num1 = 0
        sum_num2 = 0
        sum_num1 += num1
        sum_num2 += num2
        
        while(sum_num1 != sum_num2):

            if sum_num1 < sum_num2:
                sum_num1 += num1
                if sum_num1 > sum_num2:
                    sum_num2 += num2

        return sum_num1
    
##### Test
print(mcm(3, 11)) # --> 33
print(mcm(11, 3)) # --> 33
print(mcm(2, 3)) # --> 6
print(mcm(2, 2)) # --> None
print(mcm(3, -11)) # --> None
print(mcm(11, 15)) # --> 165


print(5%2)

def mcd(num1:int, num2:int):

    if num1 > num2:
        num1, num2 = num2, num1
    
    resto = num2 % num1

    