#---------Exercise List Comprehension-----------

#Filter only negative and zero in the list using list comprehension
from operator import le


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_numbers = [i for i in numbers if i <= 0]
print(filter_numbers)

#Flatten the following list of lists of lists to a one dimensional list :
#[number for row in list_of_list for number in row]
list_of_list =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list = [number for row in list_of_list for number in row]
new_list2 = [number for row in new_list for number in row]
print(new_list2)

# Find all of the numbers from 1-100 that are divisible by 7
div7 = [n for n in range(1,100) if n % 7 == 0]
print(div7)

# Find all of the numbers from 1-100 that have a 3 in them
num_3 = [x for x in range(1, 100) if '3' in str(x)]
print(num_3)

# Count the number of spaces in a string
stringN = 'hello How are you? fine'
space = [s for s in stringN if s == ' ']
print(len(space))

# Consonants in a string: 
# Create a list of all the consonants in the string "Yellow Yaks like yelling and 
# yawning and yesturday they yodled while eating yuky yams"
sentence = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = [letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(consonants)

# Get index and value from list
# Get the index and the value as a tuple for items in the list ["hi", 4, 8.99, 'apple', ('t,b','n')].  
# Result would look like [(index, value), (index, value)]
list1 = ["hi", 4, 8.99, 'apple', ('t,b','n')]
result = [(index, item) for index, item in enumerate(list1)]
print(result)

# Find common numbers in two lists of numbers
list_a = [1,2,3,4]
list_b = [2,3,4,5]
common = [n for n in list_a if n in list_b]
print(common)

# Find numbers in sentence
# Get only the numbers in a sentence like 'In 1984 there were 13 instances 
# of a protest with over 1000 people attending'.
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
word = sentence.split()
numbers = [n for n in word if not n.isalpha()]
print(numbers) 

# Determine even or odd in list of numbers
# Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even, and the word 'odd' if the number is odd.  
# Result would look like ['odd','odd', 'even']
result = ['even' if n % 2 == 0 else 'odd' for n in range(10)]
print(result)

# Common number tuples
# Produce a list of tuples consisting of only the matching numbers in these lists .  
# Result would look like (4,4), (12,12)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
list_b = [2, 7, 1, 12]

result = [(a, b) for a in list_a for b in list_b if a == b]
print(result)

# Find words with more than 4 letters
# Find all of the words in a string that are less than 4 letters
sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
examine = sentence.split()
result = [n for n in examine if len(n) >= 4]
print(result)

# Use a nested list comprehension to find all of the numbers from 1-100 that are divisible by any single digit besides 1 (2-9)
result = [n for n in range(1,100) if True in [True for x in range(2,10) if n % x  == 0]]
print(result)