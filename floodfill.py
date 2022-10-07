# import maze_generator
import numpy as np
import random

# maze= np.empty([3,3],dtype=int)
# for i in range(0,3):
#     for j in range(0,3):
#         maze[i][j] = random.choice([0,1])
# # maze = maze_generator.maze_generator()
# maze[0][0] = 1
# print(maze)
# # maze = np.array([[1,1,1],
# #                   [1,0,1],
# #                   [1,1,1]  ])

height,width = 3,3
seen = set()
def flood_fill(maze,current):
    x,y = current
    if (x >= 0 and x < height and y >= 0 and y < width and (x,y) not in seen ):
        if(maze[x][y] != 0):
            seen.add((x,y))

            for (x2,y2) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                flood_fill(maze,(x2,y2))

    return(seen)
    
# reachable = flood_fill(maze,(0,0))
# print(reachable)