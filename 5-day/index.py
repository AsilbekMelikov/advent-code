
data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

# The First Problem

data = data.split('\n')
rules = []
updates = []

for i in data:
    if ',' in i:
        updates.append(i)
    elif '|' in i:
        rules.append(i)

def updates_rules():
    total = 0
    for update in updates:
        numbers = update.split(',')
        finished = False 
        n = len(numbers)
        for i in range(n):
            for j in range(i+1, n):
                sign = numbers[i] + "|" + numbers[j]
                re_sign = numbers[j] + "|" + numbers[i]
                if sign in rules:
                    continue
                if re_sign in rules:
                    finished = True
                    break
            if finished:
                break
        else:
            total += int(numbers[n//2])
    return total
print(updates_rules())


def second_problem():
    total = 0
    for update in updates:
        numbers = update.split(',')
        n = len(numbers)
        incorrect = False
        for i in range(n):
            for j in range(i+1, n):
                sign = numbers[i] + "|" + numbers[j]
                re_sign = numbers[j] + "|" + numbers[i]
                if sign in rules:
                    continue
                if re_sign in rules:
                    incorrect = True
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        if incorrect:
            total += int(numbers[n//2])
    return total
print(second_problem())

