import collections
import maze_generator
import matplotlib.pyplot as plt
import ghosts

wall, path, goal = 0,1,2
ghosts_value = [7,8,10]
width, height = 51, 51

def bfsGhostsInvisible(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] != wall and grid[x2][y2] not in ghosts_value and grid[x2][y2] <10 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


# maze = maze_generator.maze_generator()
# maze,ghost_location = ghosts.spawn_ghosts(maze,50)
# count = 0
# for _ in range(1000):
#     maze,ghost_location = ghosts.move_ghosts(maze,ghost_location)
#     path = bfsGhostsInvisible(maze,(0,0))
#     print(path)
#     print(ghost_location)
#     if path:
#         count = count +1
#         for c in path:
#             if c in ghost_location:
#                 print("Error in code")
#                 print(c)
#         print("No match")
# print(count)
# plt.imshow(maze)
# plt.show()
