import maze_generator
import maze_check
import ghosts
import globalVariables
import a_star

output = []
no_of_ghosts = 10
def run_agent2(no_of_ghosts):
    path = None
    while(not path):
        grid = maze_generator.maze_generator()
        path = maze_check.bfs(grid, (0,0)) 

    grid,ghosts_coordinate = ghosts.spawn_ghosts(grid,no_of_ghosts)
    
    path = a_star.bfsGhostsInvisible(grid,(0,0))
    while True:
        x2,y2 = path[1]
        if grid[x2][y2] == 8 or grid[x2][y2] >= 10:
            return ("Failed")
        elif grid[x2][y2] == 2:
            globalVariables.success_count = globalVariables.success_count + 1
            return("Success")
        else:
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)
            path = a_star.bfsGhostsInvisible(grid,(x2,y2))
            if not path:
                return "Path Not Found"


print(run_agent2(1))
    # print(grid)
    # for points in path:
    #     x2,y2 = points
    #     if grid[x2][y2] == 8 or grid[x2][y2] >= 10:
    #         return ("Failed")
    #     elif grid[x2][y2] == 2:
    #         globalVariables.success_count = globalVariables.success_count + 1
    #         return("Success")
    #     else:
    #         grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)