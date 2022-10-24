import collections
from queue import PriorityQueue

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

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(maze,start):
    goal = (50,50)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()
        x,y = current
        if maze[x][y] == 2:
            break

        for x2,y2 in ((x+1,y),(x-1,y),(x,y-1),(x,y+1)):
            if x2 < 0 or x2 >= height or y2 < 0 or y2 >= width or maze[x2][y2] == 0 or maze[x2][y2] in ghosts_value or maze[x2][y2] > 10:
                continue
            new_cost = cost_so_far[current] + (abs(x-x2)+ abs(y-y2))
            if ((x2,y2)) not in cost_so_far or new_cost < cost_so_far[(x2,y2)]:
                cost_so_far[(x2,y2)] = new_cost
                priority = new_cost + heuristic(goal, (x2,y2))
                frontier.put((x2,y2), priority)
                came_from[(x2,y2)] = current
    
    if goal not in came_from:
        return None
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

