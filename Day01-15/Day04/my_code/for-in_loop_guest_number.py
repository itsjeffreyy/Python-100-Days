"""
Using for loop to calculate the summary from 1 to 100
"""

sum = 0
for x in range(1,101):
    sum += x

print("The summary from 1 to 100 is %f" % sum)

############################################################

"""
Using for-in loop to calculate the even summary from 1 to 100
"""

sum = 0
for y in range(0, 101, 2):
    sum += y
    #print(y)
print("The even summary from 1 to 100 is %f" % sum)

############################################################

"""
The other way to use for-in loop to calculate the even summary from 1 to 100
"""

sum = 0
for z in range(1, 101):
    if z %2 ==0:
        sum += z    
print("The even summary from 1 to 100 is %f" % sum)