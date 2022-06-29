#---------------------FUNCTIONS--------------------------------

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




