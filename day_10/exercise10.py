#----------------LOOPS----------------

#Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)

number = 0
while  number < 11:
    print(number)
    number += 1

#Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)

number = 10
while number > -1:
    print(number)
    number -= 1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
hashtag = '#'
for element in range(7):
    print(hashtag)
    hashtag = hashtag + '#'

#Use nested loops to create the following:
hashtagH = '#'

for i in range(8):
    for j in range(8):
        hashtagH += ' #'
    print(hashtagH)
    hashtagH = '#'

#Print the following pattern:
for number in range(11):
    print(f'{number} x {number} = {number * number}')

