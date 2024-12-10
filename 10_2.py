from collections import defaultdict

def find_path(data, coord, current):
    if current == 9:
        return 1
    else:
        right, left, up, down = 0, 0, 0, 0
        # Search right
        if data[coord[0]][coord[1] + 1] == current + 1:
            right = find_path(data, (coord[0], coord[1] + 1), current + 1)
        # Search left
        if data[coord[0]][coord[1] - 1] == current + 1:
            left =  find_path(data, (coord[0], coord[1] - 1), current + 1)
        # Search up
        if data[coord[0] - 1][coord[1]] == current + 1:
            up = find_path(data, (coord[0] - 1, coord[1]), current + 1)
        # Search down
        if data[coord[0] + 1][coord[1]] == current + 1:
            down = find_path(data, (coord[0] + 1, coord[1]), current + 1)
        return right + left + up + down
    return 0

data = defaultdict(lambda: defaultdict(int))
zeroes = []
with open("data/10.txt", "r") as file:
    for iline, line in enumerate(file):
        for icol, i in enumerate(line.strip()):
            data[iline][icol] = int(i)
            if i == "0":
                zeroes.append((iline, icol))
print(data)

total = 0
for zero in zeroes:
    total += find_path(data, zero, 0)
print(total)