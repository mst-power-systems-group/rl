import params
import numpy as np
from random import seed, random

seed(1)

rand = False

#params.init()

def update_table(curr_state, act, nxt_state, reward):
    
    params.Q_table[curr_state][act] += params.alpha * (reward + params.gamma * max(params.Q_table[nxt_state]) - params.Q_table[curr_state][act])
    
def get_action(curr):
    global rand              #add
    if (rand == True):
        return np.random.randint(0, params.action_size)
    else:
        return params.Q_table[curr].index(max(params.Q_table[curr])) #return the index, NOT THE VALUE!



def Q_learning(next_state, profit, Qtable,day):
    params.Q_table = Qtable      #add
    #print(params.Q_table,"\n")
    #if random() <= params.epsilon:
    if day <= 500:            #add
        global rand           #add
        rand = True           #add
    
    params.current_state = next_state             #add
    params.action = get_action(params.current_state)         #add
    update_table(params.current_state, params.action, next_state, profit)       #add

    #for i in range(24):       #comment out
        
    #    update_table(params.current_state, params.action, next_state, profit)   #comment out
    #    params.current_state = next_state         #comment out
    #    params.action = get_action(params.current_state)         #comment out

    #print(params.Q_table,"\n")


    
    #update_params(day)
        
    return params.action


def getQtable():

    return params.Q_table