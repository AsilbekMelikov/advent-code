example = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

# The First Problem
data = example.split('\n')
store = []
for i in data:
    if i:
        numbers = i.split(":")
        store.append((int(numbers[0]), [int(j) for j in numbers[1].strip().split(' ')]))


def explore_combinations(numbers, target, current_value, index=1):
    if index == len(numbers):
        return current_value == target

    if explore_combinations(numbers, target, current_value + numbers[index], index + 1):
        return True

    if explore_combinations(numbers, target, current_value * numbers[index], index + 1):
        return True

    return False

def calculate(data):
    total = 0
    for key, value in data:
        if explore_combinations(value, key, value[0]):
            total += key
    return total
print(calculate(store))

# The Second Problem
def explore_combinations(numbers, target, current_value, index=1):
    if index == len(numbers):
        return current_value == target

    if explore_combinations(numbers, target, current_value + numbers[index], index + 1):
        return True

    if explore_combinations(numbers, target, current_value * numbers[index], index + 1):
        return True
    
    if explore_combinations(numbers, target, int(f"{current_value}{numbers[index]}"), index + 1):
        return True

    return False

def calculate(data):
    total = 0
    for key, value in data:
        if explore_combinations(value, key, value[0]):
            total += key
    return total
print(calculate(store))

