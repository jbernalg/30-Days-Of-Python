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

