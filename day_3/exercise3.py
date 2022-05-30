# Declara tu edad como variable entera
age =  23

#Declara tu altura como una variable flotante
height = 1.72

#Declarar una variable que almacene un número complejo
complejo = 1 + 3j

#Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo 
#y calcule el área de este triángulo (área = 0,5 xbxh).
base = int(input('Base: '))
height = int(input('Altura: '))
area = 0.5 * base * height
print(f'El area del triangulo es: {area}')

#Escriba un script que solicite al usuario que ingrese el lado a, 
#el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c).
sidea = int(input('side a: '))
sideb = int(input('side b: '))
sidec = int(input('side c: '))
perimetro = sidea + sideb + sidec
print(f'El perimetro del triangulo es {perimetro}')

#Obtenga la longitud y el ancho de un rectángulo usando el indicador. 
#Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
length = float(input('longitud del rectangulo: '))
width = float(input('Ancho del rectangulo: '))
areaR = length*width
perimetro = 2*(length + width)
print(f'Area: {areaR}. Perimetro: {perimetro}')

#Obtenga el radio de un círculo usando el indicador. Calcula el área (área = pi xrxr) 
#y la circunferencia (c = 2 x pi xr) donde pi = 3,14.r
ratio = float(input('Radio del circulo: '))
areaC = 3.14*ratio**2
c = 2*3.14*ratio
print(f'Area del circulo: {areaC} , Circunferencia del circulo: {c}')

#Calcule la pendiente, la intersección x y la intersección y de y = 2x -2
print('Ecuacion de una recta: y = 2x - 2')
pendiente = 2
interY = -2
interX = 1
print(f'Pendiente {pendiente}, interseccion en el eje x: {interX}, interseccion en el eje y: {interY}')


