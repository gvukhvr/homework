#1
class strings:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

#2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return f"Coordinates: ({self.x}, {self.y})"
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)



#5
class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f" New balance: {self.balance}")
            else:
                print("Insufficient money. Withdrawal failed.")
        else:
            print("Invalid")


#6
            
class PrimeFilter:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_primes(self, numbers):
        return list(filter(lambda x: self.is_prime(x), numbers))




class MyClass:
  x = 5
 

class MyClass:
  x = 5
p1 = MyClass()


class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

