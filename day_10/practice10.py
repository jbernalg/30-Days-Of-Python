#-----------------WHILE LOOP--------------------
#It is used to execute a block repeatedly until a given condition is satisfied.
#When the condition become false, the line of code after the loop will be continued to be executed.

count = 0
while count < 5:
    print(count)
    count += 1

#If we are interested to run block of code once the condition is no longer true, we can use else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)

#-----------------Break and continue-----------------------
#break: it used break when like to get out of or stop loop
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

#continue: with the continue statement we can skip the current iteration, and continue with the next.
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

#-----------------For loop-----------------------
#Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0,1,2,3,4,5]

for i in numbers:
    print(i)

#for loop with string
lenguage = 'Python'

for letter in lenguage:
    print(letter)

for i in range(len(lenguage)):
    print(lenguage[i])

#for loop with tuple
numbers = (0,1,2,3,4,5)

for number in numbers:
    print(number)


