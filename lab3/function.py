
# Task 1
def grams(grams):
    return 28.3495231 * grams

# Task 2
def fahrenheit(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Task 3
def solve(numheads, numlegs):
    num_rabbits = (numlegs - 2 * numheads) / 2
    num_chickens = numheads - num_rabbits
    return int(num_chickens), int(num_rabbits)

# Task 4  
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fprime(numbers):
    return [num for num in numbers if is_prime(num)]

# Task 5
def permutation(str1, current=''):
    if not str1:
        print(current)
    else:
        for i in range(len(str1)):
            chars = str1[:i] + str1[i+1:]
            permutation(chars, current + str1[i])

# Task 6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Task 8
def spy_game(nums):
    required_sequence = [0, 0, 7]
    for num in nums:
        if num == required_sequence[0]:
            required_sequence.pop(0)
        
        if not required_sequence:
            return True
    return False

# Task 9
def volume_of_sphere(radius):
    return (4 / 3) * math.pi * (radius ** 3)

# Task 10
def unique_elements(input_list):
    unique_list = []
    
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    
    return unique_list

# Task 11
def palindrome(word):
    if word == word[::-1]:
        True
    else:
        False

# Task 12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Task 13

import random

def guessing():
    print("Hello! What is your name?")
    player_name = input()

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    x = random.randint(1, 20)

    count = 0
   

    while True:
        print("Take a guess.")
        guess = int(input())

        guesses_taken += 1

        if guess < x:
            print("Your guess is too low.")
        elif guess > x:
            print("Your guess is too high.")
        else:
            break 

    if guess == x:
        print(f"Good job, {player_name}! You guessed my number in {count} guesses.")

guessing()

        








def my_function():
  print("Hello from a function")



def my_function():
  print("Hello from a function")
my_function()



def my_function(fname, lname):
  print(fname)



def my_function(x):
  return x + 5



def my_function(*kids):
  print("The youngest child is " + kids[2])




def my_function(**kid):
  print("His last name is " + kid["lname"])


  
