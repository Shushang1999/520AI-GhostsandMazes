import math
import time
import maze_generator
import maze_check
import ghosts
import globalVariables
import a_star
import random
from datetime import datetime

output = []

def agent4(no_of_ghosts):
    path = None
    while(not path):
        grid = maze_generator.maze_generator()     # Generates Maze
        path = maze_check.bfs(grid,(0,0))      # Checks if maze is valid or not
    grid,ghosts_coordinate = ghosts.spawn_ghosts(grid,no_of_ghosts)
    x2,y2 = 0,0
    path_taken_by_agent = []
    while True:
        # print(path_taken_by_agent)
        if path == None:
            print(grid)
        path = maze_check.bfs(grid,(x2,y2))  # Check for valid Paths
        for point in path:
            potential_x,potential_y = point
            ghost_in_neighboring_cells = False
            for neighbor_x,neighbor_y in (potential_x+1,potential_y),(potential_x-1,potential_y),(potential_x,potential_y+1),(potential_x,potential_y-1),(potential_x,potential_y):
                if neighbor_x < 0 or neighbor_x >= 51 or neighbor_y < 0 or neighbor_y >= 51:    # If neighbor cell out of bounds
                    continue
                if grid[neighbor_x][neighbor_y] == 8 or grid[neighbor_x][neighbor_y] == 7 or grid[neighbor_x][neighbor_y] >= 10:     # Checking whether the potential cell or its neighbors have any ghosts
                    ghost_in_neighboring_cells = True
            if ghost_in_neighboring_cells == False:          # If no ghosts in potential cell and its neighboring cell take that step
                x2,y2 = point
                path_taken_by_agent.append((x2,y2))
                if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                    return ("Failed")
                elif grid[x2][y2] == 2:                             # Checking if Agent reached goal cell
                    globalVariables.success_count = globalVariables.success_count + 1
                    return("Success")
                else:
                    grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate) # Move ghosts
                    if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                        return ("Failed")
            else:                                                               # If No cell found without ghosts in neighbor, than mark your neighboring cells as potential cell and check whether their neighboring cells have ghosts or not, If not take that step
                for new_x,new_y in (x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1):
                    if new_x < 0 or new_x > 50 or new_y < 0 or new_y > 50:
                        continue
                    if grid[new_x][new_y] == 0:
                        continue
                    else:
                        ghosts_neighbor = False
                        for neighbor_x,neighbor_y in (new_x+1,new_y),(new_x-1,new_y),(new_x,new_y+1),(new_x,new_y-1),(new_x,new_y):
                            if neighbor_x < 0 or neighbor_x >= 51 or neighbor_y < 0 or neighbor_y >= 51:
                                continue
                            if grid[neighbor_x][neighbor_y] == 8 or grid[neighbor_x][neighbor_y] == 7 or grid[neighbor_x][neighbor_y] >= 10:
                                ghosts_neighbor = True
                                break
                        if ghosts_neighbor == False:
                            x2,y2 = new_x,new_y
                            path_taken_by_agent.append((x2,y2))
                            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                                return ("Failed")
                            elif grid[x2][y2] == 2:                             # Checking if Agent reached Goal cell
                                globalVariables.success_count = globalVariables.success_count + 1
                                return("Success")
                            else:
                                grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)  # Move Ghosts
                                if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                                    return ("Failed")
                        else:
                            while True:
                                new_x,new_y = random.choice([(x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)])  # If none of the above conditions match choose any cell at random
                                if new_x < 0 or new_x >= 51 or new_y < 0 or new_y >= 51:
                                    continue
                                if grid[new_x][new_y] == 0:
                                    continue
                                else:
                                    break
                            x2,y2 = new_x,new_y
                            path_taken_by_agent.append((x2,y2))
                            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                                return ("Failed")
                            elif grid[x2][y2] == 2:
                                globalVariables.success_count = globalVariables.success_count + 1  # Checking If Agent reached goal cell
                                return("Success")
                            else:
                                grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate) # Moving ghosts
                                if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                                    return ("Failed")
                        break
                        
# for _ in range(0,100):                
#     print(agent4(100))  
if __name__ == "__main__": 
    for no_of_ghosts in range(1,300,5):
        for _ in range(0,100):
            output.append(agent4(no_of_ghosts))
        with open("./Results/output_agent4.txt","a") as o:
            o.write("Agent 4\n")
            o.write("No of Ghosts = {}\n" .format(no_of_ghosts))
            o.write("No of Mazes = 100\n")
            o.write("Successfull tries = {}\n" .format(globalVariables.success_count))
            o.write("{}\n".format(output))
        output.clear()
        globalVariables.success_count = 0

