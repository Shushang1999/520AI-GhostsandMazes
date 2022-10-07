import math
import maze_generator
import maze_check
import ghosts
import globalVariables
import a_star


output = []
no_of_ghosts = 1

def run_agent2(no_of_ghosts):
    path = None
    while(not path):
        grid = maze_generator.maze_generator()
        path = maze_check.bfs(grid, (0,0)) 

    grid,ghosts_coordinate = ghosts.spawn_ghosts(grid,no_of_ghosts)
    
    # print(ghosts_coordinate)
    path = a_star.bfsGhostsInvisible(grid,(0,0))
    x2,y2 = 0,0
    while(not path):
        min_dist = 0
        nearest_ghost = ()
        for ghost_loc in ghosts_coordinate:
            gx,gy = ghost_loc
            if grid[gx][gy] % 2 == 1:
                continue
            dist = math.sqrt(math.pow(gx-x2,2) + math.pow(gy-y2,2))
            if min_dist == 0 or dist < min_dist:
                min_dist,nearest_ghost = dist,(gx,gy)
        max_dist = 0
        away_from_ghost = ()
        gx,gy = nearest_ghost
        for new_x,new_y in ((x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)):
            if 0 <= new_x < 51 and 0 <= new_y < 51:
                dist = math.sqrt(math.pow(gx-new_x,2) + math.pow(gy-new_y,2))
                if max_dist == 0 or max_dist < dist:
                    max_dist = dist
                    away_from_ghost = (new_x,new_y)
        x2,y2 = away_from_ghost
        if grid[x2][y2] == 8 or grid[x2][y2] >= 10:
            return("Failed")
        grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
        path = a_star.bfsGhostsInvisible(grid,(x2,y2))
    while True:
        # print(path)
        x2,y2 = path[1]
        if grid[x2][y2] == 8 or grid[x2][y2] >= 10:
            return ("Failed")
        elif grid[x2][y2] == 2:
            globalVariables.success_count = globalVariables.success_count + 1
            return("Success")
        else:
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
            path = a_star.bfsGhostsInvisible(grid,(x2,y2))
            while not path:
                min_dist = 0
                nearest_ghost = ()
                for ghost_loc in ghosts_coordinate:
                    gx,gy = ghost_loc
                    if grid[gx][gy] % 2 == 1:
                        continue
                    dist = math.sqrt(math.pow(gx-x2,2) + math.pow(gy-y2,2))
                    if min_dist == 0 or dist < min_dist:
                        min_dist,nearest_ghost = dist,(gx,gy)
                max_dist = 0
                away_from_ghost = ()
                gx,gy = nearest_ghost
                for new_x,new_y in ((x2+1,y2),(x2-1,y2),(x2,y2+1),(x2,y2-1)):
                    if 0 <= new_x < 51 and 0 <= new_y < 51:
                        dist = math.sqrt(math.pow(gx-new_x,2) + math.pow(gy-new_y,2))
                        if max_dist == 0 or max_dist < dist:
                            max_dist = dist
                            away_from_ghost = (new_x,new_y)
                x2,y2 = away_from_ghost
                if grid[x2][y2] == 8 or grid[x2][y2] >= 10:
                    return("Failed")
                grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
                path = a_star.bfsGhostsInvisible(grid,(x2,y2))
                
# print(run_agent2(200))                     
for i in range(0,500):
    for _ in range(0,100):
        output.append(run_agent2(no_of_ghosts))
    with open("output_2.txt","a") as o:
        o.write("Agent 2\n")
        o.write("No of Ghosts = {}\n" .format(no_of_ghosts))
        o.write("No of Mazes = 10\n")
        o.write("Successfull tries = {}\n" .format(globalVariables.success_count))
        o.write("{}\n".format(output))
    # with open("plotGraph.txt","a") as file:
    #     file.write("{}\t".format(no_of_ghosts))
    #     file.write("{}\n".format(globalVariables.success_count))


    no_of_ghosts = no_of_ghosts + 1
    output.clear()
    # # if not globalVariables.success_count:
    # #     break
    globalVariables.success_count = 0

