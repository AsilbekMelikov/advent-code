
data = """2182145329679799934668108710912214845844951226314823525658204550"""

from collections import defaultdict
def calculate(data):
    array = []
    total = 0
    store = defaultdict(list)
    for i, num in enumerate(data):
        if i % 2 == 1:
            for _ in range(int(num)):
                array.append('.')
        else:
            for _ in range(int(num)):
                array.append(i//2)
    n = len(array) - 1
    i = 0
    x = 0
    while x <= n:
        temp = x
        temp_count = 0
        while array[x] == ".":
            temp_count += 1
            x += 1
        if temp_count > 0:
            for y in store[temp_count]:
                if y < x:
                    store[temp_count].append(x)
        x += 1



    while i <= n:
        temp_count = 0
        if array[n] != ".":
            temp = array[n]
            while temp == array[n]:
                temp_count += 1
                n -= 1
        else:
            n -= 1
            continue
        for num in range(n):
            if array[num] == ".":
                i = num
                break
        k = i
        dot_count = 0
        while dot_count != temp_count and k < n:
            if array[k] == ".":
                dot_count += 1
            else:
                dot_count = 0
            k += 1
        if dot_count == temp_count:
            for t in range(dot_count):
                array[k-dot_count+t], array[n+t+1] = array[n+t+1], array[k-dot_count+t]
    for i, num in enumerate(array):
        if num != ".":
            total += num * i
    return total
print(calculate(data))
