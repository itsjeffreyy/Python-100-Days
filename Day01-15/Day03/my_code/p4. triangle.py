"""
judge whether the three line length can make a triangle.
if can make it, calculate the area and total length.
"""
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a+b > c and b+c > a and a+c > b:
    total_length = a+b+c
    print("The total length: %f" % total_length )

    p=(total_length)/2
    area = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print("The area: %f" % area)
else:
    print("a, b, c can not make a triangle.")