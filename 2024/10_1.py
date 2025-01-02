from collections import defaultdict

def find_path(data, coord, current, found_nines=set()):
    if current == 9:
        found_nines.add(coord)
        return found_nines
    else:
        right, left, up, down = set(), set(), set(), set()
        # Search right
        if data[coord[0]][coord[1] + 1] == current + 1:
            right = find_path(data, (coord[0], coord[1] + 1), current + 1, found_nines)
        # Search left
        if data[coord[0]][coord[1] - 1] == current + 1:
            left =  find_path(data, (coord[0], coord[1] - 1), current + 1, found_nines)
        # Search up
        if data[coord[0] - 1][coord[1]] == current + 1:
            up = find_path(data, (coord[0] - 1, coord[1]), current + 1, found_nines)
        # Search down
        if data[coord[0] + 1][coord[1]] == current + 1:
            down = find_path(data, (coord[0] + 1, coord[1]), current + 1, found_nines)
        return set(list(right) + list(left) + list(up) + list(down))
    return set()

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
    # print(find_path(data, zero, 0), zero)
    total += len(find_path(data, zero, 0, set()))
print(total)