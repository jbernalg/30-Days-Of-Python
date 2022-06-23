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

#Write a code which gives grade to students according to theirs scores:
score = 70

if score >= 0 and score <= 49:
    print('F')
elif score > 49 and score <= 59:
    print('D')
elif score > 59 and score <= 69:
    print('C')
elif score > 69 and score <= 89:
    print('B')
elif score > 89 and score <= 100:
    print('A')
else:
    print('Enter a score correct!')

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

season = input('Enter a month: ').lower()

if  season == 'september' or season == 'october' or season == 'november':
    print('the season is Autumn')

elif season == 'december' or season == 'january' or season == 'february':
    print('The season is Winter')

elif season == 'march' or season == 'april' or season == 'may':
    print('The season is Spring')

elif season == 'june' or season == 'july' or season == 'august':
    print('The season is Summer')

else:
    print('Enter a month correct')

#The following list contains some fruits
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter a fruit: '). lower()

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)

#Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'}
    }

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    list_skills = person['skills']
    middle = (len(list_skills) - 1) // 2
    print(list_skills[middle])
else:
    print('skills is not in person')

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if  'skills' in person:
    list_skills = person['skills']
    if 'Python' in list_skills:
        print('True')
    else:
        print('False')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

list_skills = person['skills']

if 'JavaScript' in list_skills and 'React' in list_skills:
    print('He is a front end developer')
    if 'Node' in list_skills and 'MongoDB' in list_skills:
        if 'Python' in list_skills:
            print('He is a backend developer')
        
        if 'React' in list_skills:
            print('He is a fullstack developer')
else:
    print('unknown title')

#If the person is married and if he lives in Finland, print the information in the following format:
married = True
live = 'Finland'

if married and live == 'Finland':
    print(f'Gabriel lives in {live}. He is married')





