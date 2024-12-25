
data = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

grid = data.strip().splitlines()

from collections import deque

DIRS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

def calculate(grid):
    rows, cols = len(grid), len(grid[0])
    result1 = 0
    result2 = 0
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if (i, j) in visited:
                continue
            Q = deque([(i, j)])

            area = 0
            p = 0
            PERIM = dict()
            while Q:
                x, y = Q.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                area += 1
                for dx, dy in DIRS:
                    xx, yy = x + dx, y + dy

                    if 0 <= xx < rows and 0<= yy < cols and grid[xx][yy] == grid[x][y]:
                        Q.append((xx, yy))
                    else:
                        p += 1
                        if (dx,dy) not in PERIM:
                            PERIM[(dx,dy)] = set()
                        PERIM[(dx,dy)].add((x,y))
            

                        sides = 0
            
            for k,vs in PERIM.items():
                SEEN_PERIM = set()
                for (pr,pc) in vs:
                    if (pr,pc) not in SEEN_PERIM:
                        sides += 1
                        Q = deque([(pr,pc)])
                        while Q:
                            r2,c2 = Q.popleft()
                            if (r2,c2) in SEEN_PERIM:
                                continue
                            SEEN_PERIM.add((r2,c2))
                            for dr,dc in DIRS:
                                rr,cc = r2+dr,c2+dc
                                if (rr,cc) in vs:
                                    Q.append((rr,cc))

            result1 += area * p
            result2 += area * sides
    return (result1, result2)
print(calculate(grid))














