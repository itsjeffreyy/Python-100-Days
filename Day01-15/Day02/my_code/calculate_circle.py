"""
calculate the area and perimeter of circle
"""

import math

radius = float(input("please enter the radius of circle: "))
perimeter = 2* radius * math.pi
area = radius * radius * math.pi
print("perimeter: %.2f" % perimeter)
print("area: %.2f" % area)