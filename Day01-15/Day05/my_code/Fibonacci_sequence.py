'''
Fibonacci sequence
'''

print("Show the Fibonacci sequence below a number.")
xn = int(input("Enter a number: "))
#xn = 100

x1 = 1
x2 = 1

print(x1, x2, end=" ")
for i in range(2, xn+1):
    x = x1 + x2

    if (x > xn):
        break

    print(x, end=" ")
    x1, x2 = x2, x