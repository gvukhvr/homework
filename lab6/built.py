#1
import math
numbers = [2, 3, 4, 5]
result = math.prod(numbers)
print( result)


#2
def count(string):
    upper = 0
    lower = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return {"upper": upper, "lower": lower}

string = input()
result = count(string)
print(result)


#3
def is_palindrome(string):
    str = string.replace(" ", "").lower()
    return str == str[::-1]

string = input()

if is_palindrome(string):
    print("palindrome.")
else:
    print("not palindrome.")


#4
    
import time
import math

def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result

number = int(input("number:"))
milliseconds = int(input("milliseconds:"))
result = square_root(number, milliseconds)
print(result)


#5
def rue(tuple_input):
    return all(tuple_input)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(rue(tuple1))
print(rue(tuple2))
