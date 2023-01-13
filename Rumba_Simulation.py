name = "LASTNAME_FIRSTNAME"
header = " Rumba Simulation calling Agent"
import Providing_VeriousAgents_Prob as h
import random

NUM_ROUNDS = 20

f = open("file.txt", "w")

f.write(name + "\n")
f.write(header + "\n")


def rumba_simulate(agent, prob_of_dirt, action_penalty, one_clean, two_clean):
    f.write("prob_of_dirt: " + str(prob_of_dirt) + " % " + "\n")
    f.write("ACTION_PENALTY: " + str(action_penalty) + "\n")
    f.write("ONE_CLEAN : " + str(one_clean) + "\n")
    f.write("TWO_CLEAN : " + str(two_clean) + "\n")

    f.write("Environment : " + str([['CLEAN', 'RUMBA'], ['CLEAN', '-----']]) + "\n")
    f.write("Percept : " + str([0, 'CLEAN']) + "\n")
    f.write("Score: " + str(0) + "\n")

    Environment = [['DIRTY', 'RUMBA'], ['CLEAN', '-----']]
    percept = [0, 'CLEAN']
    percept_history = []
    percept_history.append(percept.copy())
    # You will make a call like this:
    # I am not appending whole percept history just getting the last percept history
    action = agent(percept_history, prob_of_dirt, action_penalty, one_clean, two_clean)
    f.write("Action : " + str(action) + "\n")
    rounds = 0
    score = 0

    while rounds < NUM_ROUNDS:
        rounds += 1

        #  making an environment
        if action == "LEFT":
            Environment[0][1] = 'RUMBA'
            Environment[1][1] = '-----'
        elif action == "RIGHT":
            Environment[1][1] = 'RUMBA'
            Environment[0][1] = '-----'

        if action == 'VACUUM':
            if Environment[0][1] == 'RUMBA':
                Environment[0][0] = 'CLEAN'
            else:
                Environment[1][0] = 'CLEAN'

        # getting the dirty percentage  form various Agent
        if (h.get_dirt(prob_of_dirt)) == True:
            Environment[0][0] = 'DIRTY'
        if ((h.get_dirt(prob_of_dirt)) == True):
            Environment[1][0] = 'DIRTY'
        # getting score
        if Environment[0][0] == "CLEAN" and Environment[1][0] == "CLEAN":
            score = score + h.TWO_CLEAN
        elif Environment[0][0] == "CLEAN" or Environment[1][0] == "CLEAN":
            score = score + h.ONE_CLEAN

        if action == "LEFT" or action == "RIGHT" or action == "VACUUM":
            score = score - h.ACTION_PENALTY
        # to get a percept
        if Environment[0][1] == "RUMBA":
            percept = [0, Environment[0][0]]
        else:
            percept = [1, Environment[1][0]]

        percept_history.append(percept.copy())
        f.write("Round " + str(rounds) + " complete." + "\n")
        f.write("Environment : " + str(Environment) + "\n")
        f.write("Percept : " + str(percept) + "\n")
        f.write("Score: " + str(score) + "\n")
        action = agent(percept_history, prob_of_dirt, action_penalty, one_clean, two_clean)
        f.write("Action : " + str(action) + "\n\n")

    # just checking for percept
    f.write("Final Score : " + str(score))


### END RUMBA_SIMULATE ####################################


### Main Program:

# sample call (remove once you have your agent programmed)
rumba_simulate(h.agent_reflex, 20, h.ACTION_PENALTY, h.ONE_CLEAN, h.TWO_CLEAN)


rumba_simulate(h.agent_KAFLE_PRATIK, 20, h.ACTION_PENALTY, h.ONE_CLEAN, h.TWO_CLEAN)
