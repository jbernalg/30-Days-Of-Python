contrasena_almacenada = 'OperadoresLogicos123'
contrasena_escrita = 'OperadoresLogicos123'

if contrasena_escrita == contrasena_almacenada:
    print('INICIANDO SECION ...')
else:
    print('CONTRASENA EQUIVOCADA')


#-------------------------------------------------
ingreso_mensual = 10500
gastos_mensuales = ingreso_mensual*0.4
print(gastos_mensuales)

if ingreso_mensual > 10000:
    print('Tienes un muy buen salario')
    
    if gastos_mensuales < 5000:
        print('Es buena tu economia')
    else:
        print('No estas tan bien economicamente')

elif ingreso_mensual > 1000:
    print('estas bien en latinoamerica')
else:
    print('eres pobre')