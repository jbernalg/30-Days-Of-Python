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

# e) dia del mes
print('dia del mes: ', datetime.date.today().strftime('%d'))

# f) dia de la semana
print('dia de la semana: ', datetime.date.today().strftime('%A'))