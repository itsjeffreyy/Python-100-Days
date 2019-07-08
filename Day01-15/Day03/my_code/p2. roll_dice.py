from random import randint

face = randint(1, 6)
print(face)

if face == 1:
    result = 'sing a song'
elif face == 2:
    result = 'take a dance'
elif face == 3:
    result = 'like a dog'
elif face == 4:
    result = 'do some excercise'
elif face == 5:
    result = 'speak loving you'
else:
    result = 'talk a joke'

print(result)
