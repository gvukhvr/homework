#1
def square_gen(N):
    for i in range(N):
        yield i ** 2

N = 10
squares = square_gen(N)
print(list(squares))

#2
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

even_numbers = even_generator(n)
for num in even_numbers:
    print(num, end=", ")


#3
def divisible(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


start = int(input())
end = int(input())
numbers = divisible(start, end)
print( list(numbers))

#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())
for square in squares(a, b):
    print(square)

#5
def to_zero(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
numbers = to_zero(n)
print(list(numbers))

