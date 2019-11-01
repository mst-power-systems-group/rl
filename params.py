#import pprint
import collections as coll
import numpy as np

global state_size
global action_size
global alpha
global gamma
global epsilon
#global rand
#global Q_table
#global current_state
#global action
global epsilon_min
global epsilon_decay
#global alpha_min
#global alpha_decay
global memory
global batch_size
global agent_current_state
global action

state_size = 12
action_size = 10
alpha = 0.5
gamma = 0.8
epsilon = 1.0
epsilon_min = 0.01
#alpha_min = 0.001
epsilon_decay = 0.995
#alpha_decay = 0.99
memory = coll.deque(maxlen=3000)
batch_size = 32

action = 1

agent_current_state = [0]*state_size

agent_current_state[0] = 1

agent_current_state = np.array(agent_current_state)

#rand = False

#current_states = np.zeros(hour)
#actions = np.ones(hour)
#Q_table = np.zeros(shape=(hour, state_size, action_size))



