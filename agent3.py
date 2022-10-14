import a_star
from agent2 import run_agent2
import maze_generator
import maze_check
import ghosts
import globalVariables
import math
from datetime import datetime
import multiprocessing

output = []

def agent3(no_of_ghosts):
    path = None
    while(not path):
        grid = maze_generator.maze_generator()  # Generates Maze
        path = maze_check.a_star_search(grid)      # Checks if maze is valid or not
    grid,ghosts_coordinate = ghosts.spawn_ghosts(grid,no_of_ghosts)  # spawn ghosts
    current_co_ordinate = (0,0)
    path_taken = []
    while True:
        # print(ghosts_coordinate)
        if current_co_ordinate in path_taken:
            if(path_taken.count(current_co_ordinate) >= 20):
                return("Hanged")
        path_taken.append(current_co_ordinate)
        # print(path_taken)
        x,y = current_co_ordinate
        success_rate = {
            "left":0,
            "right":0,
            "up":0,
            "down":0,
            "stay":0
        }
        for key in success_rate.keys():
            if key == "left":
                x2,y2 = x,y-1
            elif key == "right":
                x2,y2 = x,y+1
            elif key == "up":
                x2,y2 = x-1,y
            elif key == "down":
                x2,y2 = x+1,y
            else:
                x2,y2 = x,y
            for _ in range(3):
                if x2 < 0 or x2 >= 51 or y2 < 0 or y2 >= 51:
                    break
                if (run_agent2(grid.copy(),ghosts_coordinate.copy()) == "Success"):
                    success_rate[key] = success_rate[key] + 1
        max_survival = max(success_rate.values())
        if max_survival == 0:
            ## write code for running away
            min_dist = 0
            nearest_ghost = ()
            for ghost_loc in ghosts_coordinate:        #Finding Nearest Ghost
                gx,gy = ghost_loc
                if grid[gx][gy] % 2 == 1:              # Checking whether ghost visible or not
                    continue                           # if ghost in blocked cell - skip
                dist = math.sqrt(math.pow(gx-x2,2) + math.pow(gy-y2,2)) # calculating distance from every visible ghost
                if min_dist == 0 or dist < min_dist:
                    min_dist,nearest_ghost = dist,(gx,gy)
            max_dist = 0
            away_from_ghost = ()
            gx,gy = nearest_ghost                       # Nearest Ghost Coordinate
            for new_x,new_y in ((x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)): # Calculating Max Distance from 4 possible moves from the nearest ghost
                if 0 <= new_x < 51 and 0 <= new_y < 51:
                    dist = math.sqrt(math.pow(gx-new_x,2) + math.pow(gy-new_y,2))
                    if max_dist == 0 or max_dist < dist:
                        max_dist = dist
                        away_from_ghost = (new_x,new_y)
            x2,y2 = away_from_ghost                      # New Coordinate of the agent
            current_co_ordinate = (x2,y2)
            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:   # Checking If Agent Dead
                return("Failed")
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate) # Move Ghosts
            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:   # Checking If Agent Dead
                return ("Failed")
            continue
        directions_possible = []
        no_of_moves = []
        for dir,survival_rate in success_rate.items():
            if survival_rate == max_survival:
                directions_possible.append(dir)
        # print(directions_possible)
        if len(directions_possible)== 1:
            dir = directions_possible[0]
        else:
            for dir in directions_possible:
                if dir == "left":
                    x2,y2 = x,y-1
                elif dir == "right":
                    x2,y2 = x,y+1
                elif dir == "up":
                    x2,y2 = x-1,y
                elif dir == "down":
                    x2,y2 = x+1,y
                else:
                    x2,y2 = x,y
                moves = a_star.bfsGhostsInvisible(grid,(x2,y2))
                if moves:
                    no_of_moves.append(len(moves))
                else:
                    no_of_moves.append(0)
            # print(no_of_moves)
            min_moves = min(no_of_moves)
            dir = directions_possible[no_of_moves.index(min_moves)]
            # print(dir)
        if dir == "left":
            x2,y2 = x,y-1
        elif dir == "right":
            x2,y2 = x,y+1
        elif dir == "up":
            x2,y2 = x-1,y
        elif dir == "down":
            x2,y2 = x+1,y
        else:
            x2,y2 = x,y
        current_co_ordinate = (x2,y2)
        if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
            return ("Failed")
        elif grid[x2][y2] == 2:
            globalVariables.success_count = globalVariables.success_count + 1
            return("Success")
        else:
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                return ("Failed")
                    
def callAgent3(ghost_start,ghost_end):
    for g in range(ghost_start,ghost_end,20):
        for _ in range(0,10):
            output.append(agent3(g))
        with open("output_agent3_{}.txt".format(ghost_end),"a") as o:
            o.write("Agent 3\n")
            o.write("No of Ghosts = {}\n" .format(g))
            o.write("No of Mazes = 1\n")
            o.write("Successfull tries = {}\n" .format(output.count("Success")))
            o.write("{}\n".format(output))


        output.clear()
    # if not globalVariables.success_count:
    #     break
        

if __name__ == "__main__":
    time1 = datetime.now()
    print(time1)
    p1 = multiprocessing.Process(target=callAgent3,args=(11,20))
    p2 = multiprocessing.Process(target=callAgent3,args=(31,40))
    p3 = multiprocessing.Process(target=callAgent3,args=(51,60))
    p4 = multiprocessing.Process(target=callAgent3,args=(71,80))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print("Done")
    time2 = datetime.now()
    print(time2)
    print("Total Time ={}".format(time2-time1))
