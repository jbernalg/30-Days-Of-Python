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
print(len('python') == len('dragon'))

#Use a operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python')
print('on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

#There is no 'on' in both dragon and python
a = 'on'
b = 'dragon'
c = 'python'
print((a is b) and (a is c))

#Find the length of the text python and convert the value to float and convert it to string
print(str(float(len('python'))))

#Even numbers are divisible by 2 and the remainder is zero. 
#How do you check if a number is even or not using python?
number1 = int(input('Ingrese un numero entero: '))
verify = number1%2
show = verify == 0
print(f'{number1} is even number? : {show}')

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(int(7/3) == 2.7)

#Check if type of '10' is equal to type of 10
print('10' == 10)

#Check if int('9.8') is equal to 10
print(int(9.8) == 10)

