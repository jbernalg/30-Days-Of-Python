'''
Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta o si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.Se podría representar con un vacío "", por ejemplo.
'''

matrix = [['X','X','X'],
          ['O','O','O'], 
          ['X','O','X']]

def result_game(matrix):
    
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
        return 'Nulo'
    elif abs(count_x - count_o) > 1:
        return 'Nulo'
    elif count_o == 0 and count_x == 0:
        return 'Nulo'

    # Buscar ganador
    list_win = []

    for i in range(len(matrix)):
        # rows
        if matrix[i][0] == matrix[i][1] and matrix[i][0] == matrix[i][2]:
            if matrix[i][0] == 'X' or matrix[i][0] == 'O':
                list_win = list_win + [matrix[i][0]]
        
    
        # colums
        if matrix[0][i] == matrix[1][i] and matrix[0][i] == matrix[2][i]:
            if matrix[0][i] == 'X' or matrix[0][i] == 'O':
                list_win = list_win + [matrix[0][i]]

    # cruz
    if matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]:
        if matrix[0][0] == 'X' or matrix[0][0] == 'O':
            list_win = list_win + [matrix[0][0]]

    if matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0]:
        if matrix[0][2] == 'X' or matrix[0][2] == 'O':
            list_win = list_win + [matrix[0][2]]


    if len(list_win) == 2:
        return 'Nulo'
    elif len(list_win) == 1:
        return str(list_win[0])
    elif len(list_win) == 0:
        if count_ele == count_o + count_x:
            return 'Empate'
    else:
        return 'Nulo'

#################################
# Test
print(result_game(matrix))   
# matrix = ['X','X','X'] --> Nulo



