#---------------------FUNCTIONS--------------------------------

from countries_data import data

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(12, 16))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    area = 3.14*r**2
    return area
print(area_of_circle(12))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        num2 = str(num)
        if num2.isnumeric() == True:
            total += num
        else:
            return 'Deben ser numeros y enteros'
    return total

print(sum_all_nums(3,6,6))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def c_to_f(celcius):
    f = (celcius * (9/5)) + 32
    return f
print(c_to_f(36))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()

    if month == 'diciembre' or month == 'enero' or month == 'noviembre':
        return 'Winter'
    elif month == 'febrero' or month == 'marzo' or month == 'abril':
        return  'Autumn'
    elif month == 'mayo' or month == 'junio' or month == 'julio':
        return 'Spring'
    elif month == 'agosto' or month == 'septiembre' or month == 'obtubre':
        return 'Summer'
    else:
        return 'Ingrese el nombre del mes correctamente!'

print(check_season('NovieMBre'))

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(t_dep):
    a,b = t_dep
    
    if a.isnumeric() == True:
        return 'La pendiente es ', a
    elif b.isnumeric() == True:
        return 'La pendiente es ', b
    else:
        return 'Ingrese un valor dependiente correcto!'

print(calculate_slope('2x'))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    sol1 = (-b + (b*b - 4*a*c)**0.5)/2*a
    sol2 = (-b - (b*b - 4*a*c)**0.5)/2*a
    print(f'solucion 1: {sol1:.3f}. solucion 2: {sol2:.3f}')

print(solve_quadratic_eqn(2,4,2))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lista):
    for i in lista:
        print(i)

cosas = [2, 3, 4, 'queso']
print(print_list(cosas))

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lista):
    return lista[::-1]
print(reverse_list(cosas))

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lista):
    listaM = []
    for i in lista:
        listaM.append(i.upper())
    return listaM

fruits = ['banana', 'mango', 'uva', 'fresa']
print(capitalize_list_items(fruits))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lista, element):
    lista.append(element)
    return lista

print(add_item(fruits, 'manzana'))

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lista, element):
    lista.remove(element)
    return lista

print(remove_item(fruits, 'uva'))

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    suma = 0
    for i in range(num + 1):
        suma += i
    return suma

print(sum_of_numbers(10))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sumOdds = 0
    for i in range(num + 1):
        if i % 2 != 0:
            sumOdds += i

    return sumOdds

print(sum_of_odds(10))

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    sumEven = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sumEven += i

    return sumEven

print(sum_of_even(10))

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    even = 0
    odds = 0
    for i in range(num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odds += 1

    return f'even: {even} odds: {odds}'

print(evens_and_odds(100)) 

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i

    return fact

print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(objeto):
    band = False
    if len(objeto) == 0:
        band = True
    return band

lista = list()
print(len(lista))
print(is_empty(lista))
dictionary = dict()
print(is_empty(dictionary))
lista2 = [3,5,6,8,'hola']
print(is_empty(lista2))

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lista):
    sum_total = 0
    for i in lista:
        sum_total += i

    mean = sum_total/len(lista)
    return mean

def calculate_median(lista):
    lista.sort()
    n = len(lista)

    if n % 2 == 0:
        media1 = n//2
        media2 = media1 - 1
        median = (lista[media1] + lista[media2])/2
        return median
    else:
        med = n // 2
        median = lista[med]
        return median

def calculate_mode(lista):
    count = 0
    freq = []

    for i in lista:
        count = lista.count(i)
        freq.append(count)
    
    may = max(freq)
    if may == 1:
        return 'todos tienen la misma cantidad'
    else:
        band = freq.index(may)
        return lista[band]
            

def calculate_range(lista):
    lista.sort()
    rang = lista[len(lista) - 1] - lista[0]
    return rang

numeros = [1,7,12,1,9,4,4]
print(calculate_mean(numeros))
print(calculate_median(numeros))
print(calculate_range(numeros))
print(calculate_mode(numeros))

#Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    band = True

    if num == 1:
        band = False
    else:
        for i in range(2, num):
            if num % i == 0:
                band = False
                break

    return band

print(is_prime(1))

#Write a functions which checks if all items are unique in the list.
def items_unique(lista):
    band = True

    for item in lista:
        if lista.count(item) > 1:
            band = False
            break

    return band

fruits = ['naranja', 'pera', 'uva', 'mango', 'pera']
print(items_unique(fruits))

#Write a funtion which checks if all the items of the list are of the same data type.c
def same_type(lista):
    band = True
    type1 = type(lista[0]) 

    for item in lista:
        if type(item) != type1:
            band = False
            break

    return band

print(same_type(fruits))

#Write a function which check if provided variable is a valid python variable

#Go to the data folder and access the countries-data.py file.
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

def most_spoken_languages(num, data):
    total_language = list() # lista con los lenguajes de todos los paises
    proof = list()          # lista que almacena los lenguaje de un pais momentaneamente
    all_language = list()   # lista que contiene cada lenguaje
    i = 0

    # loop que almacena cada lenguaje en all_language y todos los lenguajes en total_language 
    while i < len(data):
        
        for j in data[i]['languages']:
            proof.append(j)
            total_language.append(j)

        for k in proof:
            if k in all_language:
                pass
            else:
                all_language.append(k)
    
        proof = list()
        i += 1

    frecuency_languaje = list()   # lista que almacena la frecuencia de los lenguajes
    count = 0

    for i in all_language:
        count = total_language.count(i)
        frecuency_languaje.append(count)
        count = 0

    max_language = max(frecuency_languaje) # lenguaje con mayor cantidad de paises
    stop = 0
    band = 0
    list_show = [] # lista con los lenguajes mas usados en el mundo

    for i in range(max_language, 0, -1):

        if i in frecuency_languaje:
            band = frecuency_languaje.index(i)
            list_show.append(all_language[band])
            stop += 1

        if stop == num:
            return list_show
            break

print(most_spoken_languages(10, data))


