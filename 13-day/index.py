
data = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


import re

blocks = data.strip().split("\n\n")


result = []
for block in blocks:
    numbers = re.findall(r'-?\d+', block)
    
    result.append(list(map(int, numbers)))

def calculate(data, number):
    
    total1 = 0
    total2 = 0
    for array in data:
        a1, b1, c1 = array[0], array[2], array[4] + number
        a2, b2, c2 = array[1], array[3], array[5] + number
        
        eq1 = [a1 * a2, b1 * a2, c1 * a2]
        eq2 = [a2 * a1, b2 * a1, c2 * a1]
            
        b_elim = eq1[1] - eq2[1]
        c_elim = eq1[2] - eq2[2]
        
        y = c_elim / b_elim
        
        x = (c1 - b1 * y) / a1
        if x > 100 and y > 100 and x == int(x) and y == int(y):
            total2 += x * 3 + y 
        if x == int(x) and y == int(y):
            total1 += x * 3 + y 
        
    return {total1, total2}
        
print(calculate(result, 0))
print(calculate(result, 10000000000000))
