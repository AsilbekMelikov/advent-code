









data = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


grid = data.strip().split('\n\n')

LOCK = []
KEY = []
for item in grid:
    item = [list(row) for row in item.split('\n')]
    cols = len(item[0])
    is_key = all(item[6][i] == "#" for i in range(cols))
    is_lock = all(item[0][i] == "#" for i in range(cols))
    if is_key:
        rows, cols = len(item), len(item[0])
        sub_array = []
        for i in range(cols):
            p = 0
            for j in range(rows-2, -1, -1):
                if item[j][i] == "#":
                    p += 1
            sub_array.append(p)
        KEY.append(sub_array)

    if is_lock:
        rows, cols = len(item), len(item[0])
        sub_array = []  
        for i in range(cols):
            p = 0
            for j in range(rows):
                if item[j][i] == "#":
                    p += 1
            sub_array.append(p-1)
        LOCK.append(sub_array)



def make_combinations(keys, locks):
    result = 0
    for key in keys:
        for lock in locks:
            fit = all(key[i] + lock[i] <= 5 for i in range(len(key)))
            if fit:
                result += 1
    return result

print(make_combinations(KEY, LOCK))







