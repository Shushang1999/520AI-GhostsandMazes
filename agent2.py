import math
import maze_generator
import maze_check
import ghosts
import globalVariables
import a_star
from datetime import datetime

output = []
no_of_ghosts = 1

def run_agent2(grid,ghosts_coordinate):
    path = a_star.bfsGhostsInvisible(grid,(0,0))   # Checking valid paths that doesn't contain ghosts
    x2,y2 = 0,0
    path_taken_by_agent = []
    while True:
        while(not path):                               # if No path to goal
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
            path_taken_by_agent.append((x2,y2))
            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:   # Checking If Agent Dead
                return("Failed")
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate) # Move Ghosts
            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:   # Checking If Agent Dead
                return ("Failed")
            path = a_star.bfsGhostsInvisible(grid,(x2,y2))  # Check for valid Paths
        x2,y2 = path[1]                                     # New Coordinates of the player
        path_taken_by_agent.append((x2,y2))                 # The Path for the agent
        if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
            return ("Failed")
        elif grid[x2][y2] == 2:
            globalVariables.success_count = globalVariables.success_count + 1
            return("Success")
        else:
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                return ("Failed")
            path = a_star.bfsGhostsInvisible(grid,(x2,y2))      # Check for valid Paths
                
# print(run_agent2(200))  
if __name__ == "__main__": 
    # t1 = datetime.now()
    while no_of_ghosts <= 300:
        path = None
        while(not path):
            grid = maze_generator.maze_generator()  # Generates Maze
            path = maze_check.a_star_search(grid)      # Checks if maze is valid or not
        grid,ghosts_coordinate = ghosts.spawn_ghosts(grid,no_of_ghosts)  # spawn ghosts
        for _ in range(0,100):                                           # Number of mazes
            output.append(run_agent2(grid,ghosts_coordinate))            # Appending the result
        with open("./Results/output_agent2.txt","a") as o:
            o.write("Agent 2\n")
            o.write("No of Ghosts = {}\n" .format(no_of_ghosts))
            o.write("No of Mazes = 100\n")
            o.write("Successfull tries = {}\n" .format(globalVariables.success_count))
            o.write("{}\n".format(output))
        # with open("plotGraph.txt","a") as file:
        #     file.write("{}\t".format(no_of_ghosts))
        #     file.write("{}\n".format(globalVariables.success_count))


        no_of_ghosts = no_of_ghosts + 5
        output.clear()
        # # if not globalVariables.success_count:
        # #     break
        globalVariables.success_count = 0
    # t2 = datetime.now()
    # with open("output_2_new.txt","a") as o:
    #         o.write("Time Started = {}\n".format(t1))
    #         o.write("Time Ended = {}\n".format(t2))
    #         o.write("Total Time = {}\n".format(t2-t1))

