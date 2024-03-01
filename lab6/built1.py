#1
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

my_list = [1, 2, 3, 4, 5]
result = multiply_list(my_list)
print( result)


#2
def count(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


my_string = "Hello World"
upper, lower = count(my_string)
print("uppercase letters:", upper)
print("lowercase letters:", lower)

#3

def is_palindrome(string):
    return string == string[::-1]

my_string = "radar"
print( is_palindrome(my_string))


#4
import time
import math

def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = 25100
milliseconds = 2123
result = square_root(number, milliseconds)
print(result)

#5
def all_true(tuple_input):
    return all(tuple_input)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(all_true(tuple1))
print(all_true(tuple2))
