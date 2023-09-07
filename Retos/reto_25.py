'''
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
- ¿De cuántas maneras eres capaz de hacerlo?
- Crea el código para cada una de ellas.
'''

# con for
num = 0
for i in range(1,101):
    num += i
print(num)

# con while
num = 0
cont = 1
while(cont < 101):
    num += cont
    cont += 1
print(num)

# con formula
# n(n + 1)/2 , donde n es el numero hasta donde queremos sumar
n = 100
print(n*(n + 1)//2)