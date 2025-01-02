EXAMPLE = False
if EXAMPLE:
    FILENAME = "data/18_ex.txt"
    SIZE = 7
    FALLEN_BYTES = 12
else:
    FILENAME = "data/18.txt"
    SIZE = 71
    FALLEN_BYTES = 1024

from collections import defaultdict


total_iterations = 0
def find_shortest_path(grid, position, target, visited, cost):
    global min_cost, total_iterations
    total_iterations += 1
    if cost > min_costs[position[0]][position[1]]:
        return SIZE * SIZE
    min_costs[position[0]][position[1]] = cost
    if position == target:
        if cost < min_cost:
            min_cost = cost
        return cost
    if grid[position[0]][position[1]] == "X" or position[0] < 0 or position[0] >= SIZE or position[1] < 0 or position[1] >= SIZE:
        return SIZE * SIZE
    if "%s-%s" % (position[0], position[1]) in visited:
        return SIZE * SIZE
    visited.add("%s-%s" % (position[0], position[1]))
    # Continue try left, right, up, down
    left, right, up, down = SIZE * SIZE, SIZE * SIZE, SIZE * SIZE, SIZE * SIZE
    if "%s-%s" % (position[0] - 1, position[1]) not in visited and position[0] >= 1 and min_costs[position[0] - 1][position[1]] > cost + 1:
        left = find_shortest_path(grid, [position[0] - 1, position[1]], target, visited.copy(), cost + 1)
    if "%s-%s" % (position[0] + 1, position[1]) not in visited and position[0] < SIZE - 1 and min_costs[position[0] + 1][position[1]] > cost + 1:
        right = find_shortest_path(grid, [position[0] + 1, position[1]], target, visited.copy(), cost + 1)
    if "%s-%s" % (position[0], position[1] - 1) not in visited and position[1] >= 1 and min_costs[position[0]][position[1] - 1] > cost + 1:
        up = find_shortest_path(grid, [position[0], position[1] - 1], target, visited.copy(), cost + 1)
    if "%s-%s" % (position[0], position[1] + 1) not in visited and position[1] < SIZE - 1 and min_costs[position[0]][position[1] + 1] > cost + 1:
        down = find_shortest_path(grid, [position[0], position[1] + 1], target, visited.copy(), cost + 1)
    return min(left, right, up, down)

data = []
with open(FILENAME, "r") as file:
    for line in file:
        data.append([int(i) for i in line.strip().split(",")])

grid = defaultdict(lambda: defaultdict(lambda: ""))
min_costs = defaultdict(lambda: defaultdict(lambda: 10*SIZE))
min_cost = 10*SIZE
out = ""
for i in range(SIZE):
    for j in range(SIZE):
        grid[i][j] = "."
        if ([j, i] in data[:FALLEN_BYTES]):
            grid[i][j] = "X"
        out += grid[i][j]
    out += "\n"
print(out)

print(find_shortest_path(grid, [0, 0], [SIZE-1, SIZE-1], visited = set(), cost = 0))
