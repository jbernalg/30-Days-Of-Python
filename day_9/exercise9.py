#------------Exercise conditionals----------------

#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years

age = int(input('Enter tour age: '))

if age >= 18 :
    print('You are old enough to drive')
else:
    print('to wait for the missing amount of years')

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

print('Who is older me or you?')
age = int(input('Enter your age: '))

if age > 0:
    if age > 28:
        print(f'You are {age - 28} years older than me!')
    if age < 28:
        print(f'You are {28 - age} years younger than me!')
    if age == 28:
        print(f'We are the same age!')
else:
    print('Enter a correct ages')

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = int(input('Enter a integer number A: '))
b = int(input('Enter a integer number B: '))

if a > b:
    print('a is greater than b')
elif a < b:
    print('a is smaller than b')
else:
    print('a is equal to b')







