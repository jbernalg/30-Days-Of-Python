'''
Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta o si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.Se podría representar con un vacío "", por ejemplo.
'''

matrix = [['X','',''],
          ['O', '', 'O'], 
          ['X', 'O', '']]

# validacion de la matriz
count_x = 0
count_o = 0
count_ele = 0

for ele in matrix:
    for i in ele:
        count_ele += 1
        if i == 'X':
            count_x += 1
        elif i == 'O':
            count_o += 1

if count_ele > 9:
    print('Nulo')
elif abs(count_x - count_o) > 1:
    print('Nulo2')
elif count_o == 0 and count_x == 0:
    print('Nulo3')

