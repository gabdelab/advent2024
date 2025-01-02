import re
data = []

pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'
with open("data/13.txt", "r") as file:
    wd = file.read()
    while True:
        match = re.search(pattern, wd)
        if match:
            data.append([int(x) for x in match.groups()])
            wd = wd[match.end():]
            continue
        break

min_costs = 0
for puzzle in data:
    solutions = []
    min_cost = float('inf')
    for i in range(100):
        for j in range(100):
            if i*puzzle[0] + j*puzzle[2] == puzzle[4] and i*puzzle[1] + j*puzzle[3] == puzzle[5]:
                solutions.append((i, j))
                cost = i*3 + j
                min_cost = min(min_cost, cost)
    if min_cost != float('inf'):
        min_costs += min_cost
print(min_costs)