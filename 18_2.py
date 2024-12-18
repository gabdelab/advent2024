import sys
sys.setrecursionlimit(10000)

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
def find_shortest_path(grid, position, target, visited):
    if position == target:
        return True
    if grid[position[0]][position[1]] == "X":
        return False

    visited.add("%s-%s" % (position[0], position[1]))
    # Continue try left, right, up, down
    left, right, up, down = False, False, False, False
    if "%s-%s" % (position[0] + 1, position[1]) not in visited and position[0] < SIZE - 1:
        right = find_shortest_path(grid, [position[0] + 1, position[1]], target, visited.copy())
        if right:
            return True
    if "%s-%s" % (position[0], position[1] + 1) not in visited and position[1] < SIZE - 1:
        down = find_shortest_path(grid, [position[0], position[1] + 1], target, visited.copy())
        if down:
            return True
    if "%s-%s" % (position[0] - 1, position[1]) not in visited and position[0] >= 1:
        left = find_shortest_path(grid, [position[0] - 1, position[1]], target, visited.copy())
        if left:
            return True
    if "%s-%s" % (position[0], position[1] - 1) not in visited and position[1] >= 1:
        up = find_shortest_path(grid, [position[0], position[1] - 1], target, visited.copy())
        if up:
            return True
    return right or down or up or left

data = []
with open(FILENAME, "r") as file:
    for line in file:
        data.append([int(i) for i in line.strip().split(",")])


for elem in range(0, len(data)):
    print(elem)
    grid = defaultdict(lambda: defaultdict(lambda: ""))
    out = ""
    for i in range(SIZE):
        for j in range(SIZE):
            grid[i][j] = "."
            if ([j, i] in data[:elem]):
                grid[i][j] = "X"
            out += grid[i][j]
        out += "\n"
    # print(out)
    yolo = find_shortest_path(grid, [0, 0], [SIZE-1, SIZE-1], visited = set())
    print(yolo, elem, data[elem-1])

