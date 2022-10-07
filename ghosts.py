import random
import floodfill

def spawn_ghosts(maze,no_of_ghosts):
    reachable_coordinates = floodfill.flood_fill(maze,(0,0))
    reachable_coordinates_list = list(reachable_coordinates)
    ghost_coordinates = []
    for _ in range(0,no_of_ghosts):
        gx,gy = random.choice(reachable_coordinates_list)
        flag = True
        while flag:
            if gx == 0 and gy == 0 or maze[gx][gy] == 0 or [gx,gy] in ghost_coordinates:
                gx,gy = random.choice(reachable_coordinates_list)
            else:
                flag = False
        ghost_coordinates.append((gx,gy))
        if gx == 50 and gy == 50:
            maze[gx][gy] = 8
        else:
            maze[gx][gy] = 10
    return(maze,ghost_coordinates)


def move_ghosts(maze,ghosts_coordinates):
    for i in range(0,len(ghosts_coordinates)):
        x,y = ghosts_coordinates[i]
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

        x2,y2 = random.choice(possible_moves)
        
        if maze[x2][y2] == 1:
            if maze[x][y] == 10:
                maze[x][y] = 1
            elif maze[x][y] == 8:
                maze[x][y] = 2
            elif maze[x][y] == 7:
                maze[x][y] = 0
            else:
                maze[x][y] = maze[x][y] - 10
            maze[x2][y2] = 10
        elif maze[x2][y2] == 2:
            if maze[x][y] == 10:
                maze[x][y] = 1
            elif maze[x][y] == 8:
                maze[x][y] = 2
            elif maze[x][y] == 7:
                maze[x][y] = 0
            else:
                maze[x][y] = maze[x][y] - 10
            maze[x2][y2] = 8
        elif maze[x2][y2] == 8 or maze[x2][y2] == 7 or maze[x2][y2] >= 10:
            if maze[x][y] == 10:
                maze[x][y] = 1
            elif maze[x][y] == 8:
                maze[x][y] = 2
            elif maze[x][y] == 7:
                maze[x][y] = 0
            else:
                maze[x][y] = maze[x][y] - 10
            maze[x2][y2] = maze[x2][y2] + 10
        else:
            if random.random() >= 0.5:
                if maze[x][y] == 10:
                    maze[x][y] = 1
                elif maze[x][y] == 8:
                    maze[x][y] = 2
                elif maze[x][y] == 7:
                    maze[x][y] = 0
                else:
                    maze[x][y] = maze[x][y] - 10
                maze[x2][y2] = 7 
            else:
                x2,y2 = x,y
            
        ghosts_coordinates[i] = (x2,y2)
    return(maze,ghosts_coordinates)
