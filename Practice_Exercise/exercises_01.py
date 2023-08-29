''' Exercise 1
Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! 
Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, 
How I wonder what you are"
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

'''
print('''Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are''')

# Solucion alternativa
print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are')


# Exercise 2
# Write a Python program to find out what version of Python you are using.
import sys
print(sys.version)
print(sys.version_info)

# Exercise 3
# Write a Python program to display the current date and time.
import datetime
print(datetime.datetime.now())

''' Exercise 4
Write a Python program that calculates the area of a circle based 
on the radius entered by the user.Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
#r = float(input('Ingrese Radio en cm: '))
#Area = 3.14*pow(r, exp=2)
#print(f'El Area del circulo de radio {r} es: {Area} cm')

# Excercise 5
# Write a Python program that accepts the user's first and last name and 
# prints them in reverse order with a space between them.
#first_name = input('Ingrese primer nombre: ')
#last_name = input('Ingrese segundo nombre: ')
#print(f'{last_name} {first_name}')


# Exercise 6
# Write a Python program that accepts a sequence of comma-separated numbers 
# from the user and generates a list and a tuple of those numbers.
sequence = '1,4,6,78,5,21'
print(list(sequence.split(',')))
print(tuple(sequence.split(',')))

# Exercise 7
# Write a Python program that accepts a filename from the user and prints 
# the extension of the file.
# Sample filename : abc.java
# Output : java
#filename = input('Ingrese el nombre del archivo junto a su extension: ')
#lista = list(filename.split('.'))
#print(lista[-1])

# Exercise 8
# Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])

# Exercise 9
'''
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''
exam_st_date = (11, 12, 2014)
print(f'{exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}')

# Solucion alternativa
print('The examination will start from: %i / %i / %i'%exam_st_date)

# Exercise 10
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
n1 = input('Ingrese un entero: ')
n2 = n1 + n1
n3 = n1 + n1 + n1
result = int(n1) + int(n2) + int(n3)
print(result)

# solucion alternativa
n = int(input('Ingrese un entero: '))
n1 = int('%s'%n)
n2 = int('%s%s'%(n,n))
n3 = int('%s%s%s'%(n,n,n))
print(n1+n2+n3)