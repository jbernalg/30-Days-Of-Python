#       Exercice modules

#Write a function which generates a six digit/character random_user_id
import random
import string

def random_user_id():
    data = list(string.ascii_lowercase) + list(string.digits)
    codigo = ''

    for i in range(6):
        codigo = codigo + (random.choice(data))
    return codigo

print(random_user_id())

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def random_user_id2(cant):
    data = list(string.ascii_lowercase) + list(string.digits)
    codigo = ''

    for i in range(cant):
        codigo = codigo + (random.choice(data))
    return codigo


def user_id_gen_by_user():
    tam = int(input())
    element = int(input())
    
    for i in range(element):
        print(random_user_id2(tam))

print(user_id_gen_by_user())

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    num1 = random.randint(0, 255)
    num2 = random.randint(0, 255)
    num3 = random.randint(0, 255)

    return f'rgb ({num1}, {num2}, {num3})'


print(rgb_color_gen())

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors():
    hexa = list(string.digits) + ['a','b','c','d','e','f']
    colors = ''

    for i in range(6):
        colors = colors + random.choice(hexa)

    return f'#{colors}'

print(list_of_hexa_colors())




