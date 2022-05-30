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
