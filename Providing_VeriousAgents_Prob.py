name = "LASTNAME_FIRSTNAME"
header = " Agent\n"

import random

ACTION_PENALTY = 2
ONE_CLEAN = 1
TWO_CLEAN = 5


def get_dirt(prob_of_dirt):
    if 1 + random.randrange(100) < prob_of_dirt:
        return True
    else:
        return False


# It only uses the last percept seen, and not the rest of the percept history
# It also doesn't use the probability_of_dirt, or the penalty for moving or
#   vacuuming (ACTION_PENALTY), points for exactly one room clean (ONE_CLEAN)
#   or points for having both rooms clean (TWO_CLEAN).
# You may also use the "random.randrange" in your agent.

def agent_reflex(percept_history, prob_of_dirt, ACTION_PENALTY, ONE_CLEAN, TWO_CLEAN):
    curr = percept_history[-1]
    if curr[1] == "DIRTY":
        return "VACUUM"
    elif curr[0] == 0:
        return "RIGHT"
    elif curr[0] == 1:
        return "LEFT"


def agent_KAFLE_PRATIK(percept_history, prob_of_dirt, ACTION_PENALTY, ONE_CLEAN, TWO_CLEAN):

    # You may want to use some or all of the parameters
    # Your agent cannot be trivial--remove the following line:
    # I am assuming len of  percept_history will increase by 1
    # when I finish each round(round1, round2, round3 ......)
    num = len(percept_history)
    moves = 100 // prob_of_dirt

    if percept_history[-1][1] == 'DIRTY':
        return "VACUUM"
    # I am assuming prob of dirty is small and
    if prob_of_dirt < ACTION_PENALTY:
        # I am moving based on probability because I have a less chance
        # to get dirty
        if num % moves == 0:
            if percept_history[-1][0] == 0:
                return 'RIGHT'
            else:
                return 'LEFT'
        else:
            return "NOTHING"

    if TWO_CLEAN > ACTION_PENALTY:
        if num > 1:
            #  I am moving frequently because my action penalty lower than two clean
            if percept_history[-2][1] == 'CLEAN':
                if percept_history[-1][0] == 0:
                    return 'RIGHT'
                else:
                    return 'LEFT'
            else:
                return 'NOTHING'

        else:
            return "NOTHING"
    if ACTION_PENALTY > ONE_CLEAN and ACTION_PENALTY > TWO_CLEAN:
        # my prob is less than 10 % I need to move less
        # because dirt prob is very low
        if moves >= 10:
            if num % moves == 0:
                if percept_history[-1][0] == 0:
                    return 'RIGHT'
                else:
                    return 'LEFT'
            else:
                return "NOTHING"
        elif moves <= 9 and moves >= 2:
            # 10 % to 50% I doubled the moves because my probability of dirt is increasing
            if num % (moves // 2) == 0:
                if percept_history[-1][0] == 0:
                    return "RIGHT"
                else:
                    return "LEFT"
            else:
                return "NOTHING"
        else:
            # more than 50 % I need to move back and forth every time
            if percept_history[-1][1] == "CLEAN":
                if percept_history[-1][0] == 0:
                    return 'RIGHT'
                else:
                    return "LEFT"
