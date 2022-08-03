#---------Exercise List Comprehension-----------

#Filter only negative and zero in the list using list comprehension
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
print(word)
numbers = [n for n in word if not n.isalpha()]
print(numbers) 

