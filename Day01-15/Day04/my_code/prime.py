import math

num = int(input("Enter a int number: "))
end = int(math.sqrt(num))

record = 0
for x in range(2, end+1):
    if num% x == 0:
        record = 1
        print("%d is NOT prime number" % num)
        break

if record == 0:
    print("%d is prime number" % num)