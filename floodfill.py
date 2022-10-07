
height,width = 51,51
seen = set()
def flood_fill(maze,current):
    x,y = current
    if (x >= 0 and x < height and y >= 0 and y < width and (x,y) not in seen ):
        if(maze[x][y] != 0):
            seen.add((x,y))

            for (x2,y2) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                flood_fill(maze,(x2,y2))

    return(seen)
    
# reachable = flood_fill(maze,(0,0))
# print(reachable)