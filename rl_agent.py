import params
import numpy as np
from random import seed, random

seed(1)

rand = False

#params.init()

def update_table(hour, curr_state, act, nxt_state, reward):
    
    params.Q_table[hour][curr_state][act] += params.alpha * (reward + params.gamma * max(params.Q_table[hour][nxt_state]) - params.Q_table[hour][curr_state][act])
    
def get_action(hour, curr):
    
    if (rand == True):
        return np.random.randint(0, params.action_size)
    else:
        return Q_table.index(max(params.Q_table[hour][curr])) #return the index, NOT THE VALUE!



def Q_learning(next_state, profit):
    
    if random() <= params.epsilon:
        rand = True
    
    for i in range(24):
        update_table(i, params.current_state, params.action, next_state, profit)
        params.current_state = next_state
        params.action = get_action(i, params.current_state)
    
    #update_params(day)
        
    return params.action
