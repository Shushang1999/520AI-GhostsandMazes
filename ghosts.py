import random
import floodfill

def spawn_ghosts(maze,no_of_ghosts):
    reachable_coordinates = floodfill.flood_fill(maze,(0,0))  # Spawning ghosts at reachable location
    reachable_coordinates_list = list(reachable_coordinates)
    ghost_coordinates = []                                     # Storing ghost coordinates
    for _ in range(0,no_of_ghosts):
        gx,gy = random.choice(reachable_coordinates_list)      # Choosing Random cell
        flag = True
        while flag:
            if gx == 0 and gy == 0 or maze[gx][gy] == 0 or [gx,gy] in ghost_coordinates:  # Not Spawning in start cell, blocked cell or if there was a ghosts in the chosen cell  
                gx,gy = random.choice(reachable_coordinates_list)
            else:
                flag = False
        ghost_coordinates.append((gx,gy))
        if gx == 50 and gy == 50:
            maze[gx][gy] = 8                               # Ghost in goal cell Representation
        else:
            maze[gx][gy] = 10                               # Ghost in Empty Cell
    return(maze,ghost_coordinates)


def move_ghosts(maze,ghosts_coordinates):
    for i in range(0,len(ghosts_coordinates)):
        x,y = ghosts_coordinates[i]                        # Current Ghost Coordinates
        # Storing all the possible moves according to the Coordinates of the cell
        if x == 0 and y == 0:
            possible_moves = [(x+1,y),(x,y+1)]       
        elif x == 0 and y == 50:
            possible_moves = [(x+1,y),(x,y-1)]
        elif x == 50 and y == 0:
            possible_moves = [(x-1,y),(x,y+1)]
        elif x == 50 and y == 50:
            possible_moves = [(x-1,y),(x,y-1)]
        elif x == 0:
            possible_moves = [(x+1,y),(x,y+1),(x,y-1)]
        elif x == 50:
            possible_moves = [(x-1,y),(x,y+1),(x,y-1)]
        elif y == 0:
            possible_moves = [(x+1,y),(x-1,y),(x,y+1)]
        elif y == 50:
            possible_moves = [(x+1,y),(x-1,y),(x,y-1)]
        else:
            possible_moves = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]

        x2,y2 = random.choice(possible_moves)      # Choosing Random from possible moves
        
        if maze[x2][y2] == 1:                       # If next ghost cell is empty
            if maze[x][y] == 10:                            # If previous cell is ghost in empty
                maze[x][y] = 1                                    # Change previous cell to empty
            elif maze[x][y] == 8:                           # If previous cell is ghost in goal
                maze[x][y] = 2                                      # Change previous cell to goal
            elif maze[x][y] == 7:                           # If previous cell is ghost in blocked
                maze[x][y] = 0                                      # Change previous cell to blocked
            else:
                maze[x][y] = maze[x][y] - 10                 # else it contains multiple ghosts so subtract one ghosts
            maze[x2][y2] = 10                      # Empty  cell ghost representation
        elif maze[x2][y2] == 2:                     # If next ghost cell is goal
            if maze[x][y] == 10:                             # If previous cell is ghost in empty
                maze[x][y] = 1                                      # Change previous cell to empty
            elif maze[x][y] == 8:                              # If previous cell is ghost in goal
                maze[x][y] = 2                                       # Change previous cell to goal
            elif maze[x][y] == 7:                               # If previous cell is ghost in blocked
                maze[x][y] = 0                                        # Change previous cell to blocked
            else:
                maze[x][y] = maze[x][y] - 10                    # else it contains multiple ghosts so subtract one ghosts
            maze[x2][y2] = 8                         # Goal cell ghost representation
        elif maze[x2][y2] == 8 or maze[x2][y2] == 7 or maze[x2][y2] >= 10:   # If next ghost cell already contains
            if maze[x][y] == 10:                                                         # If previous cell is ghost in empty
                maze[x][y] = 1                                                                     # Change previous cell to empty
            elif maze[x][y] == 8:                                                          # If previous cell is ghost in goal
                maze[x][y] = 2                                                                         # Change previous cell to goal
            elif maze[x][y] == 7:                                                           # If previous cell is ghost in blocked
                maze[x][y] = 0                                                                          # Change previous cell to blocked
            else:
                maze[x][y] = maze[x][y] - 10                                                # else it contains multiple ghosts so subtract one ghosts
            maze[x2][y2] = maze[x2][y2] + 10         # Multiple ghost representation
        else:
            if random.random() >= 0.5:                  # If next ghost cell is blocked 50% probability of moving
                if maze[x][y] == 10:                             # If previous cell is ghost in empty
                    maze[x][y] = 1                                          # Change previous cell to empty
                elif maze[x][y] == 8:                              # If previous cell is ghost in goal
                    maze[x][y] = 2                                             # Change previous cell to goal
                elif maze[x][y] == 7:                               # If previous cell is ghost in blocked
                    maze[x][y] = 0                                              # Change previous cell to blocked
                else:
                    maze[x][y] = maze[x][y] - 10                     # else it contains multiple ghosts so subtract one ghosts
                maze[x2][y2] = 7                      # Blocked Cell ghost representation
            else:                                     # 50% probability of staying
                x2,y2 = x,y
            
        ghosts_coordinates[i] = (x2,y2)              # Change previous Ghost Coordinates to new
    return(maze,ghosts_coordinates)
