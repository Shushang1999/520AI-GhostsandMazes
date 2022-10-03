import numpy as np
import random

def maze_generator():
    maze = np.empty([51,51],dtype=int)
    for x in range(0,51):
        for y in range(0,51):
            if (random.random() <= 0.28):
                maze[x][y] = 0
            else:
                maze[x][y] = 1

    maze[0][0] = 1
    maze[50][50] = 2

    # plt.imshow(maze,cmap="gray")
    # plt.show()
    return(maze)

# print(maze_generator())