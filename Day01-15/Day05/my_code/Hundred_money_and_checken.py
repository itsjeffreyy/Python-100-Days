'''
use one hundred to buy one hundred chicken.
one male chicken is 5 dollar.
one female chicken is 3 dollar.
one baby chicken is 1/3 dollar.
How can we do it?
'''

#5*x + 3*y + (100-x-y)/3 = 100

for x in range(0, 100):
    for y in range(0, 100):
        if (5*x + 3*y + (100-x-y)/3) == 100 :
            print("%d male chicken, %d female chicken, %d baby chicken" % (x, y, 100-x-y))