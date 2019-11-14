# trial_winstate_gen.py
# ryan pili 20191103
# using random library to generate the winstates for each of the six trials

import collections
import textwrap
import re
import random 


def randints(int_range: int, length: int) -> list: 
    randlist = []
    randlist = random.sample(range(int_range), length)
    randlist = [item_in_list + 1 for item_in_list in randlist]
    return randlist


trials = range(3)
trial_states = []
for trial in trials:
    randlist = randints(12, 12)
    randlist = [item_in_list for item_in_list in randlist]
    trial_states.append(randlist)

print(randlist, "randlist")
print(trial_states, "trial_states")