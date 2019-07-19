row = int(input("row = "))

for i in range(1, row+1):
    print('*'*i)
print()

for i in range(1, row+1):
    j=0
    while j < row-i:
        print(' ',end = '')
        j+=1
    print('*'*i)
print()

for i in range(1, row+1, 1):
    j=0
    while j < row-i:
        print(' ',end='')
        j+=1
    print('*'*(2*i-1))
    