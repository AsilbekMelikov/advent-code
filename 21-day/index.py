


from collections import deque 
from heapq import heappush, heappop


data = """
789
456
123
#0A
"""
data1 = """
#^A
<v>
"""

grid = data.strip().splitlines()
n_k = [list(row) for row in grid]
d_k = [list(row) for row in data1.strip().splitlines()]

dirs_h = {
    (-1, 0): "^",
    (1, 0): "v",
    (0, 1): ">",
    (0, -1): "<",
}
DIRS = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]

DIRS2= DIRS

def calculate(code, n_k, DIRS):
    n_rows, n_cols = len(n_k), len(n_k[0])
    result = []

    for i in range(n_rows):
        for j in range(n_cols):
            if n_k[i][j] == "A":
                nr, nc = i, j
    for s in code:
        Q = deque([(nr, nc, [])])
        visited = {}
        key = (nr, nc, None)
        visited[key] = 0
        while Q:
            xx, yy, dirs = Q.popleft()

            if n_k[xx][yy] == s:
                result.append(dirs+['A'])
                nr, nc = xx, yy

            for dx, dy in DIRS:
                nx, ny = xx + dx, yy + dy
                if (nx, ny, dirs_h[(dx, dy)]) in visited:
                    continue
                visited[(nx, ny, dirs_h[(dx, dy)])] = 0
                if 0 <= nx < n_rows and 0 <= ny < n_cols:
                    Q.append((nx,ny, dirs + [dirs_h[(dx, dy)]])) 
    return ''.join(''.join(sublist) for sublist in result)
# print(calculate('029A', n_k, DIRS))

def second_robot(code, d_k, DIRS):
    d_rows, d_cols = len(d_k), len(d_k[0])

    for i in range(d_rows):
        for j in range(d_cols):
            if d_k[i][j] == "A":
                dr, dc = i, j
    
    result = []
    for s in code:
        Q = deque([(dr, dc, [])])
        visited  = set()
        visited.add((dr, dc))
        while Q:
            xx, yy, dirs = Q.popleft()
            
            if d_k[xx][yy] == s:
                result.append(dirs + ['A'])
                dr, dc = xx, yy
                break
            
            for dx, dy in DIRS:
                nx, ny = xx + dx, yy + dy
                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))

                if 0 <= nx < d_rows and 0 <= ny <d_cols:
                    Q.append((nx,ny, dirs + [dirs_h[(dx, dy)]])) 
    t = ''.join(''.join(sublist) for sublist in result)
    return t

from itertools import permutations
total = 0
# codes = ['029A', '980A', '179A', '456A', '379A']
codes = ['029A']
for code in codes:
    result = set()
    combination = calculate(code, n_k, DIRS)
    result.add(combination)
    result_len = len(combination)
    for perm in permutations(DIRS):
        combination = calculate(code, n_k, list(perm))
        if len(combination) == result_len:
            result.add(combination)
    # print(result)
    result2 = set()
    combination2 = second_robot(combination, d_k, DIRS)
    result2.add(combination2)
    result2_len = combination2
    for i in range(3):
        for j in range(i+1, 4):
            DIRS[i], DIRS[j] = DIRS[j], DIRS[i]
            for element in result:
                combination2 = second_robot(element, d_k, DIRS)
                if result2_len == len(combination2):
                    result2.add(combination2)
    # print(result)
    # print(len(second_robot(combination2, d_k, DIRS)))
    n = float('inf')
    for i in range(3):
        for j in range(i+1, 4):
            DIRS[i], DIRS[j] = DIRS[j], DIRS[i]
            for element in result2:
                n = min(len(second_robot(element, d_k, DIRS)), n)
    digit = int(code[:3])
    # print(n)
    # print(digit)
    total += n * digit
print(total)

# for code in codes:
#     digit = int(code[:3])

#     number = len(second_robot(second_robot(calculate(code, n_k), d_k), d_k))
#     print(number)
#     total += digit*number

# print(total)

