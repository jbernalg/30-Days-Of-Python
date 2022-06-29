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




