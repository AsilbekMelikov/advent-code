
data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
from collections import defaultdict

grid = data.strip().split('\n')

def is_ingrid(x,y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

# The First Problem
def calculate_antinodes(grid):
    antennas = defaultdict(list)
    rows, cols = len(grid), len(grid[0])
    
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] != '.':
                antennas[grid[x][y]].append((x, y))

    antinodes = set()

    for _, direc in antennas.items():
        n = len(direc)
        for i in range(n):
            for j in range(i + 1, n):
                d1, d2 = direc[i], direc[j]
                dx, dy = d2[0] - d1[0], d2[1] - d1[1]

                antinode1 = (d1[0] - dx, d1[1] - dy)
                antinode2 = (d2[0] + dx, d2[1] + dy)

                # Add valid antinodes within grid bounds
                if is_ingrid(*antinode1, rows, cols):
                    antinodes.add(antinode1)
                if is_ingrid(*antinode2, rows, cols):
                    antinodes.add(antinode2)

    return len(antinodes)
print(calculate_antinodes(grid))


# The Second Problem
def calculate_antinodes(grid):
    antennas = defaultdict(list)
    
    rows, cols = len(grid), len(grid[0])
    
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] != '.':
                antennas[grid[x][y]].append((x, y))
    
    antinodes = set()
    
    for _, direc in antennas.items():
        n = len(direc)
        for i in range(n):
            for j in range(i+1, n):
                d1, d2 = direc[i], direc[j]
                diffx, diffy = d2[0] - d1[0], d2[1] - d1[1]
                
                s1 = (d1[0] - diffx, d1[1] - diffy)
                s2 = (d2[0] + diffx, d2[1] + diffy)
                
                while is_ingrid(*s1, rows, cols):
                    antinodes.add(s1)
                    s1 = (d1[0] - diffx, d1[1] - diffy)
                while is_ingrid(*s2, rows, cols):
                    antinodes.add(s2) 
                    s2 = (d2[0] + diffx, d2[1] + diffy)
            antinodes.add(direc[i])
    return len(antinodes)
print(calculate_antinodes(grid))

                















