year = int(input("Please enter the year: "))
is_leap = (year%4 ==0 and year%100 != 0 or year%400==0)
print("The is leap year:", is_leap)