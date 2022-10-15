import maze_generator
import maze_check
import ghosts
import globalVariables

output = []
no_of_ghosts = 1
def run_agent1(no_of_ghosts):
    path = None
    while(not path):
        grid = maze_generator.maze_generator()                  # Generate grid that is not too blocked
        path = maze_check.bfs(grid, (0,0))                      # Checking if path available or not

    grid,ghosts_coordinate = ghosts.spawn_ghosts(grid,no_of_ghosts)   # Spawn ghosts
    for points in path:                                                # as BFS returns the shortest path we are using that path to move forward
        x2,y2 = points
        if grid[x2][y2] == 8 or grid[x2][y2] >= 10:                    # Checking wheather agent dead
            return ("Failed")
        elif grid[x2][y2] == 2:                                         # Checking whether agent reached goal cell
            globalVariables.success_count = globalVariables.success_count + 1
            return("Success")
        else:
            grid, ghosts_coordinate = ghosts.move_ghosts(grid,ghosts_coordinate)  # Move Ghosts
            if grid[x2][y2] == 8 or grid[x2][y2] >= 10:                            # Checking whether agent dead 
                return ("Failed")

if __name__ == "__main__":
    while no_of_ghosts <= 300:
        for _ in range(0,100):                                              # No of Mazes
            output.append(run_agent1(no_of_ghosts))                         # Writing output to file 
        with open("./Results/output_agent1.txt","a") as o:
            o.write("Agent 1\n")
            o.write("No of Ghosts = {}\n" .format(no_of_ghosts))
            o.write("No of Mazes = 100\n")
            o.write("Successfull tries = {}\n" .format(globalVariables.success_count))
            o.write("{}\n".format(output))


        no_of_ghosts = no_of_ghosts + 5
        output.clear()
        globalVariables.success_count = 0

