# -------------------Higher Order Functions-------------------
# In python you can do the following operations with functions:
# - A function can take one or more functions as parameters
# - A function can be returned as a result of another function
# - A function can be modified
# - A function can be assigned to a variable

#function as a parameter
def sum_numbers(nums):
    return sum(nums) #a funtion abusing the built-in sum function

lista = [1,4,5,2,6]
print(sum_numbers(lista)) 

def high_order_function(f, lst): #concatenation of functions
    summation = f(lst)
    return summation

result = high_order_function(sum_numbers, [1,3,5,7])
print(result)