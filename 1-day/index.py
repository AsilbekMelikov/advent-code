data = """
123123 2143123
234123 54634
"""

# The first problem of the day
lines = data.strip().split('\n')
left = []
right = []

for line in lines:
    left_value, right_value = map(int, line.split())
    left.append(left_value)
    right.append(right_value)
left.sort()
right.sort()

def calculate_total_distance(left, right):
    n = len(left)
    total = 0
    
    for i in range(n):
        total += abs(left[i] - right[i])
    return total
print(calculate_total_distance(left, right))

# The second problem of the day

lines = data.strip().split('\n')
left = []
right = {}

for line in lines:
    left_value, right_value = map(int, line.split())
    left.append(left_value)
    if right_value in right:
        right[right_value] += 1
        continue
    right[right_value] = 1

def calculate_total_distance(left, right):
    total = 0
    
    for num in left:
        if num in right:
            total += num * right[num]
    return total
print(calculate_total_distance(left, right))

