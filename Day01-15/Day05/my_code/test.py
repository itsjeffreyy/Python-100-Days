x = int(input("x = "))

if x in [2, 5]:
    print("WINNER", x)
elif x in [3, 9, 10]:
    print("LOSER", x)
else:
    print("STUPID", x)