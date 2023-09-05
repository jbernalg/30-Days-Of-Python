'''
Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula 
la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

def Upper_First_Letter(string):

    # Base de Datos del abecedario
    minus_mayus = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e': 'E', 'f':'F', 'g':'G', 'h':'H',
                   'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'ñ':'Ñ', 'o':'O',
                   'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W',
                   'x':'X', 'y':'Y', 'z':'Z'}

    # convertimos el texto en una lista
    list_text = list(string)

    # cambiar la primera letra del texto
    if list_text[0] in minus_mayus:
        list_text[0] = minus_mayus[string[0]]

    # recorrer toda la lista y reeplazamos la letra de cada inicio de texto
    for i in range(len(list_text)-1):
    
        if list_text[i] == ' ' and i+1 <= (len(list_text)-1):

            if list_text[i+1] in minus_mayus:
                list_text[i+1] = minus_mayus[list_text[i+1]]
         
    # convertimos la lista a texto
    string = ''.join(list_text)

    return string

# test
print(Upper_First_Letter(' hola 8undo d'))
print(Upper_First_Letter('programacion en python'))
print(Upper_First_Letter('! /cada cuanto tienes  hambre'))
# ' hola 8undo d' -->  Hola 8undo D 
# 'programacion en python' -->   Programacion En Python   
# '! /cada cuanto tienes  hambre' -->   ! /cada Cuanto Tienes  Hambre 