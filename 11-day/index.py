memo = {}

def go(cur, times):
    print(cur)
    if (cur, times) in memo:
        return memo[(cur, times)]
    
    if times == 0:
        return 1

    result = 0
    
    if cur == "0":
        result = go("1", times - 1)
    
    elif len(cur) % 2 == 0:
        mid = len(cur) // 2
        left = cur[:mid]
        right = cur[mid:]
        result = go(left, times - 1) + go(right, times - 1)
    
    else:
        result = go(str(int(cur) * 2024), times - 1)
    
    memo[(cur, times)] = result
    return result

data = "125 17"
result = data.split(" ")

total = 0

for i in result:
    print(total)
    total += go(i, 25)

