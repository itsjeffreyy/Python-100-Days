'''
find out perfect number from 1 to the number user entered.
'''

end = int(input("end number = "))

for end_n in range(1, end):
    factor_sum = 0
    for i in range(1, end_n):
        if end_n%i ==0 :
            factor_sum += i

    if factor_sum == end_n:
        print("%d is perfect number" % end_n)