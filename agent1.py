import maze_generator
import maze_check
import ghosts
import globalVariables
import datetime

output = []
no_of_ghosts = 1
def run_agent1(no_of_ghosts):
    path = None
    while(not path):
        grid = maze_generator.maze_generator()
        path = maze_check.bfs(grid, (0,0)) 

    grid,ghosts_coordinate = ghosts.spawn_ghosts(grid,no_of_ghosts)
    # print(grid)
    for points in path:
        x2,y2 = points
        if grid[x2][y2] == 8 or grid[x2][y2] >= 10:
            return ("Failed")
        elif grid[x2][y2] == 2:
            globalVariables.success_count = globalVariables.success_count + 1
            return("Success")
        else:
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)

# with open("output.txt","a") as o:
#     o.write("Agent 1"

# while True:

while no_of_ghosts <= 500:
    for _ in range(0,100):
        output.append(run_agent1(no_of_ghosts))
    with open("output_agent1_floodfill.txt","a") as o:
        o.write("Agent 1\n")
        o.write("No of Ghosts = {}\n" .format(no_of_ghosts))
        o.write("No of Mazes = 100\n")
        o.write("Successfull tries = {}\n" .format(globalVariables.success_count))
        o.write("{}\n".format(output))
    with open("plotGraph.txt","a") as file:
        file.write("{}\t".format(no_of_ghosts))
        file.write("{}\n".format(globalVariables.success_count))


    no_of_ghosts = no_of_ghosts + 1
    output.clear()
    # if not globalVariables.success_count:
    #     break
    globalVariables.success_count = 0

