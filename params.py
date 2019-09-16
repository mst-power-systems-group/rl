import pprint
import numpy as np


state_size = 12
action_size = 7
alpha = 0.55
gamma = 0.6
epsilon = 0.2

#current_states = np.zeros(hour)
#actions = np.ones(hour)
#Q_table = np.zeros(shape=(hour, state_size, action_size))

current_state = 0
action = 1

Q_table = []

for i in range(state_size):
  row = []
  for j in range(action_size):
    row.append(0.0)
  Q_table.append(row)
