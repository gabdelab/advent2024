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
    puzzle[4] += 10000000000000
    puzzle[5] += 10000000000000
    solutions = []

    b_pushes = (puzzle[4] * puzzle[1] - puzzle[5] * puzzle[0]) / (puzzle[2] * puzzle[1] - puzzle[0] * puzzle[3])
    a_pushes = (puzzle[4] - b_pushes * puzzle[2]) / puzzle[0]

    if int(a_pushes) != a_pushes or int(b_pushes) != b_pushes:
        continue
    min_costs += int(a_pushes*3 + b_pushes)

print(min_costs)

