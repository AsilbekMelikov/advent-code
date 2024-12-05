
data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

grid = data.splitlines()

# First Problem 

def calculate_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    total_count = 0

    directions = [
        (0, 1),  
        (0, -1), 
        (1, 0),  
        (-1, 0), 
        (1, 1),  
        (-1, -1),
        (1, -1), 
        (-1, 1)  
    ]
    def check_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    # Traverse the grid
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_word(x, y, dx, dy):
                    total_count += 1

    return total_count

print(calculate_xmas(grid))

# Second Problem

grid = data.splitlines()

def calculate_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    total_count = 0

    for x in range(1, rows-1):
        for y in range(1, cols-1):
            if grid[x][y] == 'A':
                left = f"{grid[x-1][y-1]}A{grid[x+1][y+1]}"
                right = f"{grid[x-1][y+1]}A{grid[x+1][y-1]}"
                if (left == "MAS" or left[::-1] == "MAS") and (right == "MAS" or right[::-1] == "MAS"):
                    total_count += 1
    return total_count
print(calculate_x_mas(grid))

