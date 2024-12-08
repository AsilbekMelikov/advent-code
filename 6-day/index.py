data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

grid = data.strip().splitlines()

# The First Problem

def calculate_dir(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    x = y = 0
    distinct = set()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                x, y = i, j
                break
    
    while 0 <= x < rows and 0 <= y < cols:
        for dx, dy in directions:
            x, y = x + dx, y + dy
            while grid[x][y] != "#":
                distinct.add((x, y))
                x, y = x + dx, y + dy
                if x >= rows or x < 0 or y < 0 or y >= cols:
                    return len(distinct)
            x, y = x - dx, y - dy
        
    return len(distinct)
print(calculate_dir(grid))


# The Second Problem
grid = [list(row) for row in grid]

def calculate_dir(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    x = y = 0
    distinct = set()
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                x, y = i, j
                break
    
    while 0 <= x < rows and 0 <= y < cols:
        for dx, dy in directions:
            x, y = x + dx, y + dy
            while grid[x][y] != "#":
                if (x, y, dx, dy) in distinct:
                    return True
                distinct.add((x, y, dx, dy))
                x, y = x + dx, y + dy
                if x >= rows or x < 0 or y < 0 or y >= cols:
                    return False
            x, y = x - dx, y - dy
        
    return False

def calculate_possible(grid):
    rows, cols = len(grid), len(grid[0])
    possible_directions = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "." and grid[i][j] != "^":
                grid[i][j] = "#"
                if calculate_dir(grid):
                    print(possible_directions)
                    possible_directions += 1
                
                grid[i][j] = '.'
    return possible_directions
print(calculate_possible(grid))