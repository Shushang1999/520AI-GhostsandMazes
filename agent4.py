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
        path = maze_check.bfs(grid,(x2,y2))  # Check for valid Paths
        for point in path:
            potential_x,potential_y = point
            ghost_in_neighboring_cells = False
            for neighbor_x,neighbor_y in (potential_x+1,potential_y),(potential_x-1,potential_y),(potential_x,potential_y+1),(potential_x,potential_y-1):
                if neighbor_x < 0 or neighbor_x >= 51 or neighbor_y < 0 or neighbor_y >= 51:
                    continue
                if grid[neighbor_x][neighbor_y] == 8 or grid[neighbor_x][neighbor_y] == 7 or grid[neighbor_x][neighbor_y] >= 10:
                    ghost_in_neighboring_cells = True
            if ghost_in_neighboring_cells == False:
                x2,y2 = point
                path_taken_by_agent.append((x2,y2))
                if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                    return ("Failed")
                elif grid[x2][y2] == 2:
                    globalVariables.success_count = globalVariables.success_count + 1
                    return("Success")
                else:
                    grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
                    if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                        return ("Failed")
            else:
                for new_x,new_y in (x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1):
                    if new_x < 0 or new_x > 50 or new_y < 0 or new_y > 50:
                        continue
                    if grid[new_x][new_y] == 0:
                        continue
                    else:
                        ghosts_neighbor = False
                        for neighbor_x,neighbor_y in (new_x+1,new_y),(new_x-1,new_y),(new_x,new_y+1),(new_x,new_y-1):
                            if neighbor_x < 0 or neighbor_x >= 51 or neighbor_y < 0 or neighbor_y >= 51:
                                continue
                            if grid[neighbor_x][neighbor_y] == 8 or grid[neighbor_x][neighbor_y] == 7 or grid[neighbor_x][neighbor_y] >= 10:
                                ghosts_neighbor = True
                                break
                        if ghosts_neighbor == False:
                            x2,y2 = new_x,new_y
                        else:
                            while True:
                                new_x,new_y = random.choice([(x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)])
                                if new_x < 0 or new_x >= 51 or new_y < 0 or new_y >= 51:
                                    continue
                                if grid[new_x][new_y] == 0:
                                    continue
                                else:
                                    break
                            x2,y2 = new_x,new_y
                            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                                return ("Failed")
                            elif grid[x2][y2] == 2:
                                globalVariables.success_count = globalVariables.success_count + 1
                                return("Success")
                            else:
                                grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
                                if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
                                    return ("Failed")
                        break
                        


        # print(paths)
        # path_found = False
        # for ways in paths:
        #     # print("path",ways)
        #     potential_x,potential_y = ways[1]
        #     ghost_free = True
        #     path_found = False
        #     for neighbor_x,neighbor_y in (potential_x+1,potential_y),(potential_x-1,potential_y),(potential_x,potential_y+1),(potential_x,potential_y-1):
        #         if neighbor_x >= 0 and neighbor_x < 51 and neighbor_y >= 0 and neighbor_y < 51:
        #             if grid[neighbor_x][neighbor_y] == 8 or grid[neighbor_x][neighbor_y] == 7 or grid[neighbor_x][neighbor_y] >= 10:
        #                 ghost_free == False
        #     if ghost_free:
        #         x2,y2 = potential_x,potential_y
        #         if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
        #             return ("Failed")
        #         elif grid[x2][y2] == 2:
        #             globalVariables.success_count = globalVariables.success_count + 1
        #             with open("output_agent4.txt","a") as o:
        #                 o.write("{}\n".format(path_taken_by_agent))
        #             return("Success")
        #         else:
        #             grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
        #             if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
        #                 return ("Failed")
        #         path_found = True
        #         break
        # if path_found == False:
        #     while True:
        #         random_cell = random.choice([(x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)])
        #         if random_cell[0] > 0 and random_cell[1] > 0 and random_cell[0] <= 50 and random_cell[1] <= 50:
        #             break
        #     x2,y2 = random_cell
        #     if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
        #         return ("Failed")
        #     elif grid[x2][y2] == 2:
        #         globalVariables.success_count = globalVariables.success_count + 1
        #         with open("output_agent4.txt","a") as o:
        #             o.write("{}\n".format(path_taken_by_agent))
        #         return("Success")
        #     else:
        #         grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
        #         if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
        #             return ("Failed")
        # paths.clear()
            # Check if the next cell and the neighboring cells contains ghosts or not if not take the next step or else
            # check the next cell in the other paths and search for the same if no paths exists run from the nearest ghost


        # while(len(paths) == 0 or ghost_present_in_next_cell):                               # if No path to goal
        #     min_dist = 0
        #     nearest_ghost = ()
        #     for ghost_loc in ghosts_coordinate:        #Finding Nearest Ghost
        #         gx,gy = ghost_loc
        #         if grid[gx][gy] % 2 == 1:              # Checking whether ghost visible or not
        #             continue                           # if ghost in blocked cell - skip
        #         dist = math.sqrt(math.pow(gx-x2,2) + math.pow(gy-y2,2)) # calculating distance from every visible ghost
        #         if min_dist == 0 or dist < min_dist:
        #             min_dist,nearest_ghost = dist,(gx,gy)
        #     max_dist = 0
        #     away_from_ghost = ()
        #     gx,gy = nearest_ghost                       # Nearest Ghost Coordinate
        #     for new_x,new_y in ((x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)): # Calculating Max Distance from 4 possible moves from the nearest ghost
        #         ghost_free_cell = True
        #         away_from_ghost = (100,100)
        #         if 0 <= new_x < 51 and 0 <= new_y < 51:
        #             # Code to get the coordinates that does'nt have ghosts and if there are no cells choose any at random
        #             for neighbor_x,neighbor_y in ((new_x+1,new_y),(new_x-1,new_y),(new_x,new_y+1),(new_x,new_y-1)):
        #                 if 0 <= neighbor_x < 51 and 0 <= neighbor_y < 51:
        #                     if grid[neighbor_x][neighbor_y] == 8 or grid[neighbor_x][neighbor_y] >= 10:
        #                         ghost_free_cell == False
        #             if ghost_free_cell:
        #                 away_from_ghost = new_x,new_y
        #                 break
            # if away_from_ghost == (100,100):
            #     while True:
            #         random_cell = random.choice((x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1))
            #         if random_cell[0] < 51 or random_cell[1] <= 50:
            #             away_from_ghost = random_cell
            #             break
            # x2,y2 = away_from_ghost                      # New Coordinate of the agent
            # path_taken_by_agent.append((x2,y2))
            # if grid[x2][y2] == 8 or grid[x2][y2] >= 10:   # Checking If Agent Dead
            #     return("Failed")
            # grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate) # Move Ghosts
            # if grid[x2][y2] == 8 or grid[x2][y2] >= 10:   # Checking If Agent Dead
            #     return ("Failed")



        # x2,y2 = path[1]                                     # New Coordinates of the player
        # path_taken_by_agent.append((x2,y2))                 # The Path for the agent
        # if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
        #     return ("Failed")
        # elif grid[x2][y2] == 2:
        #     globalVariables.success_count = globalVariables.success_count + 1
        #     return("Success")
        # else:
        #     grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
        #     if grid[x2][y2] == 8 or grid[x2][y2] >= 10:         # Checking If Agent Dead 
        #         return ("Failed")
        #     path = a_star.bfsGhostsInvisible(grid,(x2,y2))      # Check for valid Paths
                
# print(run_agent2(200))  
if __name__ == "__main__": 
    for no_of_ghosts in range(1,100,5):
        for _ in range(0,100):
            output.append(agent4(no_of_ghosts))
        with open("output_agent4.txt","a") as o:
            o.write("Agent 4\n")
            o.write("No of Ghosts = {}\n" .format(no_of_ghosts))
            o.write("No of Mazes = 100\n")
            o.write("Successfull tries = {}\n" .format(globalVariables.success_count))
            o.write("{}\n".format(output))
        output.clear()
        globalVariables.success_count = 0

