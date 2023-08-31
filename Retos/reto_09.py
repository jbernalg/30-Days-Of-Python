'''
Crea un programa que se encargue de transformar un número decimal a binario sin utilizar 
funciones propias del lenguaje que lo hagan directamente.
'''
def covert_binary(numero_d):
    # cero cuando el numero decimal es cero
    if numero_d == 0:
        return 0
    # 1 cuando el numero decimal es uno
    elif numero_d == 1:
        return 1
    else:
        # variable que almacena el numero binario
        numero_b = ''

        # bucle que corre hasta que el numero decimal sea menor o igual a cero
        while numero_d > 0:
            result = numero_d // 2  # resultado
            mod = numero_d % 2      # modulo o residuo

            # si el resultado es mayor a 1, guarda el modulo como numero binario 
            if result > 1:    
                numero_b += str(mod)
            # si el resultado es igual a 1, guarda el modulo y el resultado como numero biario
            elif result == 1:
                numero_b += str(mod)
                numero_b += str(result)

            # asigna el resultado de la division como el nuevo numero decimal
            numero_d = result

        # invierte la cadena, conviertela en numero entero y retorna el valor
        return int((numero_b[::-1]))

print(covert_binary(3))