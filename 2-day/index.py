
data = """
32 33 34 35
12 11 9 8
"""

# First Problem
lines = data.strip().split('\n')
total_array = []
for line in lines:
    total_array.append([int(x) for x in line.split()])

def find_status(diff):
    if diff > 0:
        return 'inc'
    else:
        return'dec'

def calculate_safe(source):
    safe_ones = 0
    for arr in source:
        status = find_status(arr[1] - arr[0])
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            status2 = find_status(diff)
            if status != status2 or diff < -3 or diff == 0 or diff > 3:
                break
        else:
            safe_ones += 1
    return safe_ones
print(calculate_safe(total_array))

# Second Problem
def calculate_safe(source):
    safe_ones = 0
    for arr in source:
        chance = True
        status = find_status(arr[1] - arr[0])
        i = 1
        while i < len(arr):
            diff = arr[i] - arr[i-1]
            status2 = find_status(diff)
            if status != status2 or diff < -3 or diff == 0 or diff > 3:
                if chance:
                    arr.pop(i-1)
                    chance = False
                else:
                    break
            else:
                i += 1
        else:
            safe_ones += 1
    return safe_ones
print(calculate_safe(total_array))

