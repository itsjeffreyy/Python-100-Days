
'''
Find out all Narcissistic number
'''

import math

for i in range(100, 1000):
    num = str(i)

    num_sum = 0
    for j in num:
        num_sum += int(j)**3

    if num_sum == i:
        print("%d is Narcissistic number" % i)