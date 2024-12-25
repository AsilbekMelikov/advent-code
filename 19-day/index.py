

data = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

data = data.strip().split('\n')

stripes = [i for i in data[0].split(', ')]
groups = []

for item in data[2:]:
    groups.append(item)


# The First Way

def calculate1(stripes, groups):
    total = 0

    def find_sequences(sequence:str):   
        if not sequence:
            return True

        for stripe in stripes:
            if sequence.startswith(stripe):
                if find_sequences(sequence[len(stripe):]):
                    return True
                else:
                    continue
        return False


    for group in groups:
        if find_sequences(group):
            total += 1
    return total

# print(calculate1(stripes, groups))

def calculate(stripes, groups):
    total = 0
    caching = {}
    def find_sequences(sequence:str):   
        if sequence in caching:
            return caching[sequence]
        total = 0
        if not sequence:
            return 1

        for stripe in stripes:
            if sequence.startswith(stripe):
                total += find_sequences(sequence[len(stripe):])
        caching[sequence] = total
        return total


    for group in groups:
        total += find_sequences(group)
    return total

# print(calculate(stripes, groups))
import sys
sys.setrecursionlimit(10**6)
caching = {}
def fib(n):
    array =[1, 1]

    if n == 0:
        return 0
    elif n == 1:
        return array[0]
    elif n == 2:
        return array[1]
    elif n > 2:
        for i in range(2, n+1):
            array.append(array[0] + array[1])
            array.pop(0)
        return array[0]

def fib1(n):
    if n in caching:
        return caching[n]
    
    if n <=1:
        return n
    result  = fib1(n-1) + fib1(n-2)
    caching[n] = result 
    return result
    
# Dynamic Programming -> Breaking the complex problem into subproblems, and store the subproblems solution into the memory 
print(fib(101))
print(fib1(101))


# Time Complexity -> O(N)
# Space Complexity -> O(N)



    

        



















