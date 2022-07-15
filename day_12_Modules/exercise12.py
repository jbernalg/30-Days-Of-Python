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


