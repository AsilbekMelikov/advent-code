




data = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

grid = data.strip().splitlines()
grid = [list(row) for row in grid]

from collections import deque

def calculate(grid):
    rows, cols = len(grid), len(grid[0])

    DIRS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                sr, sc = i, j
            if grid[i][j] == "E":
                er, ec = i, j
                grid[i][j] = "."

    cheats = 0
    SEEN = set()
    SEEN.add((sr, sc, None, None, 0))
    Q = deque([(0, sr, sc, 0, None, None)])
    ans = set()
    while Q:
        steps, x, y, limit, cheat_start, cheat_end = Q.popleft()
        # print(x,y ,cheat_start, cheat_end, limit)
        if steps >14:
            continue
        
        if (x, y) == (er, ec):
            if cheat_end is None:
                cheat_end = (x, y)
            if steps <= 14 and (cheat_start, cheat_end) not in ans:
                ans.add((cheat_start, cheat_end))      
            continue


        if cheat_start is None:
            Q.append((steps, x, y, 0, (x,y), None))
        for dx, dy in DIRS:
            xx, yy = x + dx, y + dy

            if (xx, yy, cheat_start, cheat_end, limit) in SEEN:
                continue
            SEEN.add((xx, yy, cheat_start, cheat_end, limit))
            if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == ".":
                if limit != 0:
                    Q.append((steps + 1, xx, yy, 0, cheat_start, (xx, yy)))
                else:
                    Q.append((steps + 1, xx, yy, 0, (xx, yy), None))
            elif 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == "#" and limit <= 20:
                Q.append((steps + 1, xx, yy, limit + 1, cheat_start, None))

    return len(ans)
print(calculate(grid))
# from collections import deque

# def calculate(grid):
#     rows, cols = len(grid), len(grid[0])

#     # Directions: down, up, right, left
#     DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#     # Locate start (S) and end (E)
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == "S":
#                 sr, sc = i, j
#             if grid[i][j] == "E":
#                 er, ec = i, j
#                 grid[i][j] = "." 

#     # BFS initialization
#     cheats = 0
#     Q = deque([(0, sr, sc, 0, {(sr, sc)})])  # (steps, x, y, cheat_limit, visited set)

#     while Q:
#         steps, x, y, limit, visited = Q.popleft()

#         # Check if we've reached the endpoint
#         if (x, y) == (er, ec):
#             if steps <= 84:  # Example constraint: path must be within 84 steps
#                 cheats += 1
#             continue

#         # Explore neighbors
#         for dx, dy in DIRS:
#             xx, yy = x + dx, y + dy
#             print(xx, yy)
#             # Bounds check
#             if not (0 <= xx < rows and 0 <= yy < cols):
#                 continue

#             # Create a new visited set for this state
#             new_visited = visited.copy()

#             # If moving to a normal track cell
#             if grid[xx][yy] == "." and (xx, yy) not in new_visited:
#                 new_visited.add((xx, yy))
#                 Q.append((steps + 1, xx, yy, 0, new_visited))

#             # If using cheat mode to cross a wall
#             elif grid[xx][yy] == "#" and limit < 20 and (xx, yy) not in new_visited:
#                 new_visited.add((xx, yy))
#                 Q.append((steps + 1, xx, yy, limit + 1, new_visited))

#     return cheats

# print(calculate(grid))



# import sys
# from collections import defaultdict, Counter, deque

# sys.setrecursionlimit(10**6)
# DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left


# ans = 0

# G = grid
# R = len(G)
# C = len(G[0])

# for r in range(R):
#     for c in range(C):
#         if G[r][c] == 'S':
#             sr,sc = r,c
#         if G[r][c] == 'E':
#             er,ec = r,c
# DIST = {}
# Q = deque([(0,er,ec)])
# while Q:
#     d,r,c = Q.popleft()
#     if (r,c) in DIST:
#         continue
#     DIST[(r,c)] = d
#     for dr,dc in DIRS:
#         rr,cc = r+dr, c+dc
#         if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
#             Q.append((d+1,rr,cc))

# def find_cheat(d0, CHEAT_TIME):
#     ans = set()
#     Q = deque([(0,None,None,None,sr,sc)])
#     SEEN = set()
#     SAVE = 100
#     while Q:
#         d,cheat_start,cheat_end,cheat_time,r,c = Q.popleft()
#         assert cheat_end is None
#         if d>=d0-SAVE:
#             continue
#         if G[r][c] == 'E':
#             if cheat_end is None:
#                 cheat_end = (r,c)
#             if d<=d0-SAVE and (cheat_start,cheat_end) not in ans:
#                 #print(d,d0,r,c,cheat_start,cheat_end,cheat_time)
#                 ans.add((cheat_start, cheat_end))
#         if (r,c,cheat_start,cheat_end,cheat_time) in SEEN:
#             continue
#         SEEN.add((r,c,cheat_start,cheat_end,cheat_time))
#         #if len(SEEN) % 1000000 == 0:
#         #    print(len(SEEN))

#         if cheat_start is None: # start cheat
#             assert G[r][c] != '#'
#             Q.append((d,(r,c),None,CHEAT_TIME,r,c))
#         if cheat_time is not None and G[r][c]!='#': # and cheat_time==0: # end cheat
#             assert G[r][c] in ['.', 'S', 'E']
#             if DIST[(r,c)] <= d0-100-d:
#                 ans.add((cheat_start, (r,c)))
#                 #if len(ans) % 1000 == 0:
#                 #    print(len(ans), d+DIST[(r,c)])
#             #Q.append((d,cheat_start,(r,c),None,r,c))
#         if cheat_time == 0:
#             continue
#         else:
#             for dr,dc in DIRS:
#                 rr,cc = r+dr, c+dc
#                 if cheat_time is not None:
#                     assert cheat_time > 0
#                     if 0<=rr<R and 0<=cc<C:
#                         Q.append((d+1,cheat_start,None,cheat_time-1,rr,cc))
#                 else:
#                     if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
#                         Q.append((d+1,cheat_start,cheat_end,cheat_time,rr,cc))
#     #print(len(SEEN))
#     return len(ans)

# d0 = DIST[(sr,sc)]
# print(d0)
# # print(find_cheat(d0, 2))
# print(find_cheat(d0, 20))   
# # 986081









