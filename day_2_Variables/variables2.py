#----------- VARIABLES ---------------

# se declaran luego se definen
# declarar  definir 
nombre = 'Pedro Pedrito'
'''
print(nombre)
Pedro Pedrito
'''

# son modificables
nombre = 'Jose' 
nombre = 'Miguel'
nombre = 'Maria'
'''
print(nombre)
Maria
'''

# Son operables
numero = 10
numero += 5
'''
print(numero)
15
'''

# Se concatenan
nombre = 'Maicol'
bienvenida = 'Hola ' + nombre + ' Como estas?'
'''
print(bienvenida)
Hola Maicol Como estas?
'''
# Concatenacion fstring
# convierte cualquier dato a tipo texto
nombre = True
bienvenida = f'Hola {nombre} Como estas?'
'''
print(bienvenida)
Hola True Como estas?
'''
# borrar datos
#del nombre
#print(nombre)

# Operador de pertenencia (in y not in) 
# busca una variable dentro de otra y arroja un booleano
'''
print('ola' in bienvenida)
print('pedro' in bienvenida)
print('pedro' not in bienvenida)
True
False
True
'''

# camelCase. Una forma de escribir variables
nombreCompletoDeTuArtistaFavorito = 'Jose Luis Perales'

# snakecase. forma recomendada de escribir variables en Python
nombre_completo_de_tu_artista_favorito = 'Jose Luis Perales'


#------------------ Desempaquetado ---------------------------
#### consiste en asignarle los valores contenidos en un array a varias variables.
#### funciona solo cuando la cantidad de valores es igual a la cantidad de variables
datos = ('cilantro', 'cebolla')
verdura1, verdura2 = datos
'''
print(verdura2)
print(verdura1)
cebolla
cilantro
'''
