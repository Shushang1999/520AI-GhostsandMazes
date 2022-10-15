import numpy as np
import random

def maze_generator():
    maze = np.empty([51,51],dtype=int)        # Generating a random empty maze
    for x in range(0,51):                      
        for y in range(0,51):
            if (random.random() <= 0.28):      # If probabilty less than 28%
                maze[x][y] = 0                 # Make cell blocked
            else:
                maze[x][y] = 1                 # Else make cell unblocked

    maze[0][0] = 1                             # Start Cell Unblocked
    maze[50][50] = 2                           # Goal Cell Unblocked
    return(maze)

