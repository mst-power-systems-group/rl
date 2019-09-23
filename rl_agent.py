import params
import xlwt
from xlwt import Workbook
from random import seed, random, randint

#seed(1)

#rand = False

#params.init()

def update_table(curr_state, act, nxt_state, reward):
    
    params.Q_table[curr_state][act] += params.alpha * (reward + params.gamma * max(params.Q_table[nxt_state]) - params.Q_table[curr_state][act])
    
def get_action(curr):
    print("random is ",params.rand)
    if (params.rand == True):
        print("random action")
        return randint(0, params.action_size)
    else:
        print("not random action")
        return params.Q_table[curr].index(max(params.Q_table[curr])) #return the index, NOT THE VALUE!
    
def update_epsilon():
    
    if params.epsilon > params.epsilon_min:
        params.epsilon *= params.epsilon_decay
    else:
        params.epsilon = 0.0
        

def update_alpha():
    
    if params.alpha > params.alpha_min:
        params.alpha *= params.alpha_decay



#def Q_learning(next_state, profit, Qtable,day):
def Q_learning(next_state, profit):
    #params.Q_table = Qtable      #add
    #print(params.Q_table,"\n"    #if random() <= params.epsilon:
    #global rand           #add
    #if day <= 200:            #add      
       # rand = True           #add
    #else:
        #rand = False
        
    
    if (random() <= params.epsilon):
        params.rand = True
    else:
        params.rand = False
        
      
    params.current_state = next_state             #add 
    update_table(params.current_state, params.action, next_state, profit)       #add
    params.action = get_action(params.current_state) #add
    
    update_epsilon()
    
    update_alpha()

    #for i in range(24):       #comment out
        
    #    update_table(params.current_state, params.action, next_state, profit)   #comment out
    #    params.current_state = next_state         #comment out
    #    params.action = get_action(params.current_state)         #comment out

    #print(params.Q_table,"\n")


    
    #update_params(day)
        
    return params.action


def getQtable():
    #print(params.Q_table,"\n")

    return params.Q_table

def output_table(hour):
    
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    
    for i in range(params.state_size):
        for j in range(params.action_size):
            sheet1.write(i+hour+2, j, params.Q_table[i][j])
            
    wb.save('Q_table.xlsx')
