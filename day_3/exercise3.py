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

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
m = (10 - 2)/(6 - 2)
print(m)

#Compare the slopes of the previous exercises.
print(f'Exercise 1: slope = {pendiente}. Exercise 2: slope = {m}. Ambas son iguales')

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
lenWord1 = len('python')
lenWord2 = len('dragon')
print(lenWord1 == lenWord2)

#Use a operator to check if 'on' is found in both 'python' and 'dragon'
verified = 'on' in 'python'
verified2 = 'on' in 'dragon'
print(f'on is found in python: {verified}')
print(f'on is found in dragon: {verified2}')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
verified3 = 'jargon' in 'I hope this course is not full of jargon'
print(f'jargon is found in the sentence: {verified3}')

