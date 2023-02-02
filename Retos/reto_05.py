'''
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def poligono(a,b,c,d = 0):
    if d == 0:
        area = (b*c)/2
        print(f'Area del triangulo {area}')
        return area

    elif a == b and b == c and c == d:
        area = a*b 
        print(f'Area del cuadrado {area}')

    elif (a == c and b == d) or (a == b and c == d):
        area = a*b
        print(f'Area del rectangulo {area}')

    else: 
        print('Error: Figura geometrica incorrecta')


# probamos los diferentes poligonos
poligono(1,4,6)
poligono(2,2,2,2)
poligono(5,4,5,4)
poligono(1,5,3,2)