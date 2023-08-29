#----------- VARIABLES ---------------

# se declaran luego se definen
# declarar  definir 
nombre = 'Pedro Pedrito'
print(nombre)

# son modificables
nombre = 'Jose' 
nombre = 'Miguel'
nombre = 'Maria'
print(nombre)

# Son operables
numero = 10
numero += 5
print(numero)

# Se concatenan
nombre = 'Maicol'
bienvenida = 'Hola ' + nombre + ' Como estas?'
print(bienvenida)

# Concatenacion fstring
# convierte cualquier dato a tipo texto
nombre = True
bienvenida = f'Hola {nombre} Como estas?'
print(bienvenida)

# borrar datos
#del nombre
#print(nombre)

# Operador de pertenencia (in y not in) 
# busca una variable dentro de otra y arroja un booleano
print('ola' in bienvenida)
print('pedro' in bienvenida)

print('pedro' not in bienvenida)

# camelCase. Una forma de escribir variables
nombreCompletoDeTuArtistaFavorito = 'Jose Luis Perales'

# snakecase. forma recomendada de escribir variables en Python
nombre_completo_de_tu_artista_favorito = 'Jose Luis Perales'