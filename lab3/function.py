
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

def filter_prime(numbers):
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
def is_palindrome(word):
    return word == word[::-1]

# Task 12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Task 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()

    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)

    guesses_taken = 0
    max_guesses = 6 

    while guesses_taken < max_guesses:
        print("Take a guess.")
        guess = int(input())

        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break 

    if guess == secret_number:
        print(f"Good job, {player_name}! You guessed my number in {guesses_taken} guesses.")

guess_the_number()

        











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


  
