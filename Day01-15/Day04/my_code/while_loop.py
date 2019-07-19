"""
guess number 
"""
import random
answer = random.randint(1,100)

counter = 0

while True:
    counter+=1
    guess = int(input("Please guess a number from 1 to 100: "))
    if answer < guess:
        print("smaller")
    elif answer > guess:
        print("bigger")
    elif answer == guess:
        print("Congrt! You got the answer.")
        break

print("You guess %d times" % counter)
if counter >7 :
    print("You are a dumb")