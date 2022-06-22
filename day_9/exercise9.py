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
    if abs(age - 28) == 1:
        print('The differences is de one years')
    else:
        print('the differences is more that two years')
else:
    print('Enter a correct ages')







