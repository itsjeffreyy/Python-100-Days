'''
Find the GCD and LCM of two integer numbers
Greatest common Divisor (GCD) and Least common Multiple (LCM)
'''

x = int(input("x= "))
y = int(input("y= "))

if x > y:
    x, y = y, x

for fact in range(x, 0, -1):
    if x%fact==0 and y%fact==0:
        print("%d is the GCD of %d and %d" % (fact,x,y))
        print("%d is the LCM of %d and %d" % ( x*y/fact ,x,y))
        break