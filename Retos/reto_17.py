'''
Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula 
la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''
# Base de Datos del abecedario
minus_mayus = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e': 'E', 'f':'F', 'g':'G', 'h':'H',
               'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'ñ':'Ñ', 'o':'O',
               'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W',
               'x':'X', 'y':'Y', 'z':'Z'}

string = ' saludos d'
#string[0]= 'A'
print(string)

if string[0] in minus_mayus:
    string = string.replace(string[0], minus_mayus[string[0]])



for i in range(len(string)):
    
    if string[i] == ' ' and i+1 < (len(string)-1):

        if string[i+1] in minus_mayus:
            #string[i+1] = minus_mayus[string[i+1]]
            print(string)
         
print(string)
   
    