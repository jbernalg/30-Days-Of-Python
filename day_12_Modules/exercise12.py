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
