a = 6
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# another way for print function
a = int(input('a='))
b = int(input('b='))
print ('%d + %d = %d'% (a, b, a+b))
print ('%d - %d = %d'% (a, b, a-b))
print ('%d * %d = %d'% (a, b, a*b))
print ('%d / %d = %f'% (a, b, a/b))
print ('%d // %d = %d'% (a, b, a//b))
print ('%d %% %d = %d'% (a, b, a%b))
print ('%d ** %d = %d'% (a, b, a**b))

# variable type
a = 100
b = 12.345
c = 1 + 5j
d = 'Hello,world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
