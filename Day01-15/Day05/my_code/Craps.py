from random import randint

class Status:
    LOST = 0
    WIN = 1
    CONTINUE = 2

def dice():
    return randint(1, 6) + randint(1, 6)

def first_roll(first_point):
    if first_point in [7, 11]:
        return Status.WIN
    elif first_point in [2, 3, 12]:
        return Status.LOST
    else:
        return Status.CONTINUE

def reroll(first_point, point):
    if point == first_point:
        return Status.WIN
    elif point == 7:
        return Status.LOST
    else:
        return Status.CONTINUE

def main():
    firstpoint = dice()
    print("player's first point = %d" % firstpoint)
    status = first_roll(firstpoint)

    while status == Status.CONTINUE:
        point = dice()
        print("player's point = %d" % point)
        status = reroll(firstpoint, point)


#    print("Player WIN!" if status == Status.WIN else "Player LOSE.")
    if status == Status.WIN:
        print("Player WIN!")
    else:
        print("player LOSE")

##########
main()