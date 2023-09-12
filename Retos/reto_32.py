'''
Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
- Utiliza el menor número de líneas para resolver el ejercicio.
'''

def esBisiesto(year:int):
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0 or year % 100 == 0:
        return True
    else:
        return False

def next_bisiesto(year:int):

    count = 0
    while count < 31:

        year += 1
        if esBisiesto(year) == True:
            count += 1
            print(year)

##### Test
next_bisiesto(2020)
# 2024
# 2028
# 2032
# 2036
# 2040
# 2044
# 2048
# 2052
# 2056
# 2060
# 2064
# 2068
# 2072
# 2076
# 2080
# 2084
# 2088
# 2092
# 2096
# 2100
# 2104
# 2108
# 2112
# 2116
# 2120
# 2124
# 2128
# 2132
# 2136
# 2140
# 2144