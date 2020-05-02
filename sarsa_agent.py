import numpy as np
import random as random
class SarsaAgent():
    def __init__(self,maze): 
        self.maze=maze
        nrow=maze.nrow
        ncol=maze.ncol
        state_number=nrow*ncol
        action_number=len(maze.actions)
        #implementing q as a dict - Not Yet
        self.q={}
    
    def get_q(self,state,action=None):
        row,col,_=state
        if action is None:
            if (row,col) in self.q.keys():
                return self.q[(row,col)]
            else:
                self.q[(row,col)]=np.full((4,),0.5)
                return self.q[(row,col)]
        else:
            if (row,col) in self.q.keys():
                return self.q[(row,col)][action]
            else:
                self.q[(row,col)]=np.full((4,),0.5)
                return self.q[(row,col)][action]

    def set_q(self,state,action,value):
        row,col,_=state
        if (row,col) not in self.q.keys():
            self.q[(row,col)]=np.full((4,),0.5)
        self.q[(row,col)][action]=value

    def learn(self,episodes=100,alpha=.5,gamma=.99,epsilon=0.1):
        for i in range(episodes):
            self.maze.reset()
            done=False
            while not done:
                state=self.maze.state
                p=random.random()
                if p<epsilon:
                    action=random.choice(self.maze.actions)
                else:
                    action=np.argmax(self.get_q(state))
                
                next_state,reward,done=self.maze.step(action)
                
                p=random.random()
                if p<epsilon:
                    next_action=random.choice(self.maze.actions)
                else:
                    next_action=np.argmax(self.get_q(next_state))

                #Update Rule
                new_val=self.get_q(state,action)+alpha*(reward+gamma*self.get_q(next_state,next_action)-self.get_q(state,action))
                self.set_q(state,action,new_val)
    
    def get_policy(self,cell):
        row,col=cell
        state=(row,col,None)
        action=np.argmax(self.get_q(state))
        return action
    
    def get_policy_matrix():
        policy=np.copy(self.maze.maze)
        policy[maze.maze==1]==5



