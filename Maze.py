
import numpy as np
import matplotlib.pyplot as plt


#Reward can be give as a function than as an array

class Maze():
    def __init__(self,maze,rat=(0,0),cheese=None):
        '''
        Maze Coding:
        1 - blocked
        0 - Free
        .5 - rat

        '''
        self.maze=maze
        self.nrow=maze.shape[0]
        self.ncol=maze.shape[1]
        self.actions=[0,1,2,3]
        self.rat=rat
        if cheese is None:
            self.cheese=(self.nrow-1,self.ncol-1)
        else:
            self.cheese=cheese
        #Validation if both rat and cheese are in free cells
        if maze[self.cheese] == 1:
            raise Exception("Cheese shouldn't be on a blocked cell")
        if maze[self.rat] == 1:
            raise Exception("Rat shouldn't be on a blocked cell")
        #For saving current state
        self.state=(rat[0],rat[1],"start")
        self.visited_states=set()

    
    def get_possible_actions(self,cell=None):
        '''
        Get all the actions that's possible from a particular 
        cell in the maze.
        '''

        if cell is None:
            row,col,mode=self.state
        else:
            row,col=cell
        last_row,last_col=self.nrow-1,self.ncol-1
        cell_actions=self.actions.copy()

        #Removing invalid actions from the cells on the border
        if col==0:
            cell_actions.remove(3)
        if row==0:
            cell_actions.remove(0)
        if col==last_col:
            cell_actions.remove(1)
        if row==last_row:
            cell_actions.remove(2)

        #Removing invalid actions into blocked cells
        if row>0 and self.maze[row-1,col]==1:
            cell_actions.remove(0)
        if row<last_row and self.maze[row+1,col]==1:
            cell_actions.remove(2)
        if col>0 and self.maze[row,col-1]==1:
            cell_actions.remove(3)
        if col<last_col and self.maze[row,col+1]==1:
            cell_actions.remove(1)
        return cell_actions

    def update_state(self,action):
        valid_actions=self.get_possible_actions()
        row,col,mode=self.state
        
        #Add the current state to visited states
        self.visited_states.add((row,col))
        if action in valid_actions:
            mode="valid"
            if action==0:
                row-=1
            if action==1:
                col+=1
            if action==2:
                row+=1
            if action==3:
                col-=1
        else:
            mode="invalid"
        
        self.state=row,col,mode
        
    
    def get_reward(self):
        row,col,mode=self.state

        #If an invalid move is attempted
        if mode=="invalid":
            return -10
        #If found cheese - 100 points
        if (row,col)==self.cheese:
            return 100
        #Return -1 for all other states
        return -1
    
    def get_status(self):
        #Return True if found Cheese
        row,col,mode=self.state
        if (row,col)==self.cheese:
            return True
        else:
            return False
    
    def step(self,action):
        self.update_state(action)
        reward=self.get_reward()
        done=self.get_status()
        return self.state,reward,done

    def reset(self):
        row,col=self.rat
        self.state=(row,col,"start")
        self.visited_states=set()

    
    def show(self):
        canvas=np.copy(self.maze)
        canvas[self.maze==0]=1
        canvas[self.maze==1]=0
         #Coloring Visited cells
        for row,col in self.visited_states:
            canvas[row,col]=0.2
        #Coloring Rat cell
        rat_row,rat_col,_ = self.state
        canvas[rat_row,rat_col]=0.5
        #Coloring Cheese cell
        cheese_row,cheese_col=self.cheese
        canvas[cheese_row,cheese_col]=.8
        nrow,ncol=canvas.shape
        plt.grid('on')
        ax=plt.gca()
        ax.set_xticks(np.arange(0.5,ncol,1))
        ax.set_yticks(np.arange(0.5,nrow,1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        img=plt.imshow(canvas, interpolation='none', cmap='gray')
        print("Hidh")
        return img
    
    def get_canvas(self):
        canvas=np.copy(self.maze)
        canvas[self.maze==0]=1
        canvas[self.maze==1]=0
        #Coloring Cheese cell
        cheese_row,cheese_col=self.cheese
        canvas[cheese_row,cheese_col]=.8
        #Coloring Visited cells
        for row,col in self.visited_states:
            canvas[row,col]=0.2
        #Coloring Rat cell
        rat_row,rat_col,_ = self.state
        canvas[rat_row,rat_col]=0.5
        return canvas
    
    def show_maze(self):
        canvas=np.copy(self.maze)
        canvas[self.maze==0]=1
        canvas[self.maze==1]=0
        nrow,ncol=canvas.shape
        plt.grid('on')
        ax=plt.gca()
        ax.set_xticks(np.arange(0.5,ncol,1))
        ax.set_yticks(np.arange(0.5,nrow,1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        img=plt.imshow(canvas, interpolation='none', cmap='gray')
        return img

    




        

    



    


