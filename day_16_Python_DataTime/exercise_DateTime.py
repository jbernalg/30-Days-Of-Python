#------------ Date Time-------------
import time
import datetime

# 1. Escriba una secuencia de comandos de Python para mostrar los 
# distintos formatos de fecha y hora

# a) Fecha y hora
print('hora y fecha actual: ', datetime.datetime.now())

# b) Año actual
print('año actual :', datetime.date.today().strftime('%Y'))

# c) Mes del año
print('Mes actual: ', datetime.date.today().strftime('%B'))

# d) Numero de la semana
print('Numero de semana del año: ',datetime.date.today().strftime('%W'))

# e) Dias del años
print('dias del año: ', datetime.date.today().strftime('%j'))

# f) Numero del dia de la semana
print('numero del dia de la semana: ', datetime.date.today().strftime('%w'))

# g) dia del mes
print('dia del mes: ', datetime.date.today().strftime('%d'))

# h) dia de la semana
print('dia de la semana: ', datetime.date.today().strftime('%A'))

# 2. Escriba un programa en Python para determinar si un año dado es un año bisiesto.
def año_bisiesto(año):
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    else:
        return False

result = año_bisiesto(1995)
print(result)