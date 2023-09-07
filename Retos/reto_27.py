'''
Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
- Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
- EXTRA: ¿Eres capaz de dibujar más figuras?
'''

figure = 'cuadrado'
lados = 5

def figure_geometric(figure:str, lados:int):
    
    if lados > 1:
        if figure == 'triangulo':
            for i in range(1,lados + 1):
                print('*'*i)

        elif figure == 'cuadrado':
            for i in range(1,lados + 1):
                print('*'*lados)

        else:
            print('Indique el nombre de la figura correcta')
    else:
        print('indique un numero de lados mayor a 1')


##### Test 

figure_geometric('cuadrado',1) 
# --> indique un numero de lados mayor a 1

figure_geometric('cuadrado', 10)
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********

figure_geometric('triangulo', 10)
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

figure_geometric('circulo',3)
# --> Indique el nombre de la figura correcta