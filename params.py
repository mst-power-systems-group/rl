import pprint
import numpy as np


state_size = 12
action_size = 7
alpha = 0.55
gamma = 0.6
epsilon = 0.2
hour = 24

#current_states = np.zeros(hour)
#actions = np.ones(hour)
#Q_table = np.zeros(shape=(hour, state_size, action_size))

current_states = [0] * 24
actions = [1] * 24

Q_table = []

for i in range(24):
  row = []
  for j in range(state_size):
    column = []
    for k in range(action_size):
      column.append(0.0)
    row.append(column)
  Q_table.append(row)