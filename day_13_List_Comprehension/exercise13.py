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