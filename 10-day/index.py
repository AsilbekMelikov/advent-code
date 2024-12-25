





data = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

grid = data.strip().splitlines()


def find_zero(grid):
    rows, cols = len(grid), len(grid[0])
    zero_p = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "0":
                zero_p.append((i, j))

    return zero_p

from collections import deque

def calculate_trail(grid, zero_p):
    total = 0
    rows, cols = len(grid), len(grid[0])

    DIRS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    for p in zero_p:
        visited = set()
        x, y = p
        Q = deque([(x, y, 0)])

        while Q:
            x, y, score = Q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if score == 9:
                total += 1

            for dx, dy in DIRS:
                xx, yy = x + dx, y + dy
                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == str(score + 1):
                    Q.append((xx, yy, score + 1))
    return total


print(calculate_trail(grid, find_zero(grid)))

def calculate_trail2(grid, zero_p):
    total = 0
    rows, cols = len(grid), len(grid[0])

    DIRS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    for p in zero_p:
        x, y = p
        Q = deque([(x, y, 0)])

        while Q:
            x, y, score = Q.popleft()
            if score == 9:
                total += 1

            for dx, dy in DIRS:
                xx, yy = x + dx, y + dy
                if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == str(score + 1):
                    Q.append((xx, yy, score + 1))
    return total


print(calculate_trail2(grid, find_zero(grid)))















