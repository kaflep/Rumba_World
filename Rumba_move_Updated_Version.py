import random

ACTION_PENALTY = 1
ONE_CLEAN = 1
TWO_CLEAN = 3

print("ACTION_PENALTY:", ACTION_PENALTY)
print("ONE_CLEAN:", ONE_CLEAN)
print("TWO_CLEAN:", TWO_CLEAN)
print()

# Finish the program here..
actions = ["LEFT", "RIGHT", "VACUUM", "NOTHING"]
Environment = [['CLEAN', 'RUMBA'], ['CLEAN', '-----']]
percept = Environment[0]
percept_History = []
score = 0
dirt_prob = int(input("Enter the probability of dirt appearing (0 - 100): "))
print("Environment: [['CLEAN', 'RUMBA'],['CLEAN' , '-----']]")
print("Score : 0")
action = input("Choose an action: (l)eft, (r)ight, (v)acuum, (n)othing, (q)uit: ")
round = 0
i = 0


def get_dirty(dirt_prob):
    if random.randrange(0, 101) < dirt_prob:
        return True
    else:
        return False


while action != 'q':
    round += 1
    if action == "l":
        Environment[0][1] = "RUMBA"
        Environment[1][1] = "-----"
    elif action == "r":
        Environment[0][1] = "-----"
        Environment[1][1] = "RUMBA"

    elif action == "v":
        if Environment[0][1] == "RUMBA":
            Environment[0][0] = "CLEAN"

        else:
            Environment[1][0] = "CLEAN"

    # last I need to check for the dirt or not
    # last I need to check for the dirt or not
    # random_dirt_Prob = random.randrange(1, 101)
    if get_dirty(dirt_prob) == True:
        Environment[0][0] = "DIRTY"
    if get_dirty(dirt_prob) == True:
        Environment[1][0] = "DIRTY"
    #     to counting the score
    if action == "l" or action == "r" or action == "v":
        score = score - ACTION_PENALTY
    if Environment[0][0] == "CLEAN" and Environment[1][0] == "CLEAN":
        score = score + TWO_CLEAN
    elif Environment[0][0] == "CLEAN" or Environment[1][0] == "CLEAN":
        score = score + ONE_CLEAN
    # to find the percept
    if Environment[0][1] == "RUMBA":
        percept = [0, Environment[0][0]]
    else:
        percept = [1, Environment[1][0]]
    percept_History.append(percept.copy())

    print("Environment : ", Environment)
    print("Round " + str(round) + "complete")
    print("Percept : ", percept)
    print("Score: ", score)
    action = input("Choose an action: (l)eft, (r)ight, (v)acuum, (n)othing, (q)uit: ")
# end while loop
print("Percept History :")
#  I am getting from Google to format the list
print(*percept_History, sep="\n")
