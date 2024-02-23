#1
import math
def degree_to_radian(deg):
    rad = deg * (math.pi / 180)
    return rad
deg = float(input("Input degree: "))
rad = degree_to_radian(deg)
print(rad)

#2
import math
height = float(input())
base1 = float(input())
base2 = float(input())
x=base1+base2
area=x*height/2
print(area)

#3
import math
n = float(input())
len = float(input())
per = n*len
area=(per*len) / (4 * math.tan(math.pi / n))
print(int(area))

#4
import math
len = float(input())
h = float(input())
area=len*h
print(area)
