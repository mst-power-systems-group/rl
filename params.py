import pprint

global state_size
global action_size
global alpha
global gamma
global epsilon
global rand
global Q_table
global current_state
global action
global epsilon_min
global epsilon_decay
global alpha_min
global alpha_decay

state_size = 1
action_size = 10
alpha = 0.98
gamma = 0.7
epsilon = 0.2
epsilon_min = 0.01
alpha_min = 0.001
epsilon_decay = 0.995
alpha_decay = 0.99

rand = False

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
