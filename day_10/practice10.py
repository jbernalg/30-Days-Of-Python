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
