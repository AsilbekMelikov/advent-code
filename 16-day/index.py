




data = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

import sys
sys.setrecursionlimit(10**6)

data2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

from collections import deque
from heapq import heappush, heappop

grid = data.strip().splitlines()

grid = [list(row) for row in grid]



# The Second Way

def calculate(grid):
    rows, cols = len(grid), len(grid[0])
    # DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, top, right, left
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                sr, sc = i, j
            if grid[i][j] == "E":
                er, ec = i, j
    # BFS setup
    visited = set()
    visited.add((sr, sc, 1))  # Keep track of direction to avoid redundant paths
    Q = []
    heappush(Q, (0, sr, sc, 1, [(sr, sc)]))  # (x, y, cost, direction)
    total_ways = []
    while Q:
        cost, x, y, dir, coors = heappop(Q)
        dx, dy = DIRS[dir]
        nx, ny = x + dx, y + dy 

        if (nx, ny, dir) in visited:
            continue
        visited.add((nx, ny, dir))

        print(cost, x, y, dir)

        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == "E":
                total_ways = coors
                break
            if grid[nx][ny] != "#":
                heappush(Q, (cost+1, nx, ny, dir, coors + [(nx, ny)]))
            
            heappush(Q, (cost+1000, x, y, (dir+1)%4, coors))
            heappush(Q, (cost+1000, x, y, (dir+3)%4, coors))


#     x, y = total_ways[1]
#     queue = deque((x, y, 1, [(x, y)]))
#     total_tiles = len(total_ways)
#     while queue:
#         xx, yy, dir, coors = queue.popleft()
#         dx, dy = DIRS[dir]
#         xdx, ydy = xx + dx, yy +dy
#         if (xdx, ydy) in total_ways:
#             total_tiles += len(coors) - 1
#         if grid[xx][yy] != "#":
#             queue.append((xdx, ydy, dir, coors + [(xdx, ydy)]))
        
#         queue.append((xx, yy, (dir + 1)%4, coors))
#         queue.append((xx, yy, (dir + 3)%4, coors))
        
#     return total_tiles

# print(calculate(grid))



# The Third Way

# import heapq

# def reindeer_maze(grid):
#     # Parse the grid and find start (S) and end (E) positions
#     rows, cols = len(grid), len(grid[0])
#     start, end = None, None
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 'S':
#                 start = (r, c)
#             elif grid[r][c] == 'E':
#                 end = (r, c)
    
#     # Directions: (dy, dx, direction name)
#     directions = [(0, 1, "East"), (1, 0, "South"), (0, -1, "West"), (-1, 0, "North")]
#     direction_map = {d[2]: i for i, d in enumerate(directions)}
    
#     # Heuristic: Manhattan distance to the end
#     def heuristic(x, y):
#         return abs(x - end[0]) + abs(y - end[1])
    
#     # Priority queue: (estimated cost, actual cost, x, y, direction index)
#     pq = []
#     heapq.heappush(pq, (heuristic(*start), 0, start[0], start[1], 0))  # Start facing East (index 0)
    
#     # Visited: (x, y, direction index) -> cost
#     visited = {}
    
#     while pq:
#         est_cost, cost, x, y, dir_idx = heapq.heappop(pq)
        
#         # If reached the end, return the cost
#         if (x, y) == end:
#             return cost
        
#         # Skip if this state has been visited with a lower cost
#         state = (x, y, dir_idx)
#         if state in visited and visited[state] <= cost:
#             continue
#         visited[state] = cost
        
#         # Generate next states
#         # 1. Move forward
#         dx, dy = directions[dir_idx][0], directions[dir_idx][1]
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
#             heapq.heappush(pq, (cost + 1 + heuristic(nx, ny), cost + 1, nx, ny, dir_idx))
        
#         # 2. Rotate clockwise and counterclockwise
#         for turn, new_dir_idx in [("CW", (dir_idx + 1) % 4), ("CCW", (dir_idx - 1) % 4)]:
#             new_cost = cost + 1000
#             heapq.heappush(pq, (new_cost + heuristic(x, y), new_cost, x, y, new_dir_idx))
    
#     return -1  # If no path found


# print(reindeer_maze(grid))

    





