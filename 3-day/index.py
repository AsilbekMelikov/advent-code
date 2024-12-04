data = """
!*^mul(363,974)&(how()'mul(307,210)(:]+$:!why()%@mul(542,323)&(whe
"""

import re

# First Problem

pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, data)
numbers = [(int(x), int(y)) for x, y in matches]

total = 0

for x, y in numbers:
    total += x * y

print(total)

#  Second Problem

pattern = r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)'

data = re.sub(r'undo\(\)', 'do()', data)

total = 0
is_calculate = True  # Assume 'do()' initially
matches = re.finditer(pattern, data)

for match in matches:
    if match.group(0).startswith('mul'):
        # Extract numbers from mul pattern
        x, y = map(int, match.groups()[:2])
        if is_calculate:
            total += x * y
    elif match.group(0) == "do()":
        is_calculate = True  # Set to calculate
    elif match.group(0) == "don't()":
        is_calculate = False

