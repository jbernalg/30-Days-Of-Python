'''
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 - La función recibe un listado que contiene pares, representando cada jugada.
 - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
            Entrada: [("R","R"), ("R","R"), ("P","P")]. Resultado: "Tie".
'''

def result_game(input):
    
    # contar cantidad de elementos
    count = 0
    for i in input:
        for j in i:
            if j in 'SPRsrp':
                count += 1

    # verificar que hayan 6 jugadas
    if count != 6:
        return 'Revisar entradas'
    else:
    
        # lista que almacena el jugador ganador en cada ronda
        # 1 para el jugador1, dos para el jugador2 y 0 si hay empate
        win_round = []

        # reglas
        # S: tijera, P: papel, R: piedra
        rules = ['SP','PS','RS','SR','PR','RP'] 
                #  1    2    1    2    1    2

        #Rondas
        for sub in input:
            round = ''
            for j in sub:
                round += j.upper()

            if round in rules:
                ubicacion = rules.index(round)

                if ubicacion % 2 == 0:
                    win_round = win_round + [1]
                else:
                    win_round = win_round + [2]
            else:
                win_round = win_round + [0]

        if win_round.count(1) > 1:
            return 'Player 1'
        elif win_round.count(2) > 1:
            return 'Player 2'
        elif win_round.count(0) == 3:
            return 'Tie'
        elif win_round.count(1) == 1 and win_round.count(2) == 1 and win_round.count(0) == 1:
            return 'Tie'

##### Test        
print(result_game([("r","s"), ("S","r"), ("r","R")])) # --> Tie
print(result_game([("r","s"), ("S","r"), ("R")])) # --> Revisar entradas
print(result_game([("R","S"), ("S","R"), ("S","R")])) # --> Player 2
print(result_game([("R","S"), ("S","R"), ("R","S")])) # --> Player 1    

