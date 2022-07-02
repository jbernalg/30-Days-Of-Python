#-------------CONDITIONAL-------------

#-------------if condition--------------
#if condition:
#   this part of code runs for truthy conditions

a = 3
if a > 0:
    print(f'{a} es un numero positivo')

#-------------if else---------------
b = 3
if b < 0:
    print(f'{b} is a negative number')
else:
    print(f'{b} is a positive number')

#-------------if elif else-------------
if a > 0:
    print(f'{a} is a positive number')
elif a < 0:
    print(f'{a} is a negative number')
else:
    print(f'{a} is zero')

#-------------Short Hand-------------
# code if condition else code
print(f'{a} is positive') if a > 0 else print(f'{a} is negative')

#------------Nerted conditions----------------
a = 0
if a > 0:
    if  a % 2 == 0:
        print(f'{a} is a positive and even integer')
    else:
        print(f'{a} is a positive number')
elif a == 0:
    print(f'{a} is Zero')
else:
    print('{a} is a negative number')

#-----------if conditions and logical operators--------------
# if condition and condition:
#   code

a = 4
if a > 0 and a % 2 == 0:
    print(f'{a} is an even and positive number')
elif a > 0 and a % 2 != 0:
    print(f'{a} is a positive integer')
elif a == 0:
    print(f'{a} is Zero')
else:
    print(f'{a} is negative')

#-----------If and Or logical operators----------------
# if condition or condition:
#   code
user = 'James'
acces_level = 3
if user == 'admin' or acces_level >= 4:
    print('Acces granted')
else:
    print('Acces denied')


