import random

ACTION_PENALTY = 1
ONE_CLEAN = 1
TWO_CLEAN = 3

print("ACTION_PENALTY:", ACTION_PENALTY)
print("ONE_CLEAN:", ONE_CLEAN)
print("TWO_CLEAN:", TWO_CLEAN)
print()

# Finish the program here..
Environment = [['CLEAN', 'RUMBA'], ['CLEAN', '-----']]
score = 0
dirt_prob = int(input("Enter the probability of dirt appearing (0 - 100): "))
print("Environment: [['clean', 'RUMBA'],['CLEAN' , '-----']]")
print("Score : 0")
action = input("Choose an action: (l)eft, (r)ight, (v)acuum, (n)othing, (q)uit: ")
round = 0


# comparing prob of dirt to random value
def get_dirty(dirt_prob):
    if random.randrange(0, 101) < dirt_prob:
        return True
    else:
        return False


# end get dirt function
while action != 'q':
    round += 1
    if action == 'l' or action == 'L':
        Environment[0][1] = "RUMBA"
        Environment[1][1] = "-----"
    elif action == 'r' or action == 'R':
        Environment[0][1] = "-----"
        Environment[1][1] = "RUMBA"

    elif action == 'v' or action == 'V':
        if Environment[0][1] == "RUMBA":
            Environment[0][0] = "CLEAN"

        else:
            Environment[1][0] = "CLEAN"

    # last I need to check for the dirt or not
    if get_dirty(dirt_prob) == True:
        Environment[0][0] = "DIRTY"
    if get_dirty(dirt_prob) == True:
        Environment[1][0] = "DIRTY"
    #  base on the environment I need to give a score
    if action == "l" or action == "r" or action == "v" or action == "L" or action == "R" or action == "V":
        score = score - ACTION_PENALTY
    if Environment[0][0] == "CLEAN" and Environment[1][0] == "CLEAN":
        score = score + TWO_CLEAN
    elif Environment[0][0] == "CLEAN" or Environment[1][0] == "CLEAN":
        score = score + ONE_CLEAN

    print("Environment : ", Environment)
    print("After round " + str(round) + ":")
    print("Score: ", score)
    action = input("Choose an action: (l)eft, (r)ight, (v)acuum, (n)othing, (q)uit: ")
print("Bye !!")
