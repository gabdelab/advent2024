data = {}
with open("data/20.txt", "r") as file:
    for iline, line in enumerate(file):
        data[iline] = {}
        for icol, col in enumerate(line.strip()):
            data[iline][icol] = col
print(data)

current_position = [(i, k) for i, j in data.items() for k, l in j.items() if l == "S"][0]
path = [current_position]

while data[current_position[0]][current_position[1]] != "E":
    next_position = [(i, k) for i, j in data.items() for k, l in j.items() 
                     if abs(i - current_position[0]) + abs(k - current_position[1]) == 1 
                     and (i, k) not in path
                     and l in [".", "E"]][0]
    path.append(next_position)
    current_position = next_position

saves = {}
for i in path:
    # look for the position +2 in the path after i, if the postion +1 is not
    # look left, up, right, down

    if (i[0], i[1] - 1) not in path[path.index(i):] and (i[0], i[1] - 2) in path[path.index(i):]:
        gain = path.index((i[0], i[1] - 2)) - path.index(i) - 2
        try:
            saves[gain].append(i)
        except KeyError:
            saves[gain] = [i]

    if (i[0], i[1] + 1) not in path[path.index(i):] and (i[0], i[1] + 2) in path[path.index(i):]:
        gain = path.index((i[0], i[1] + 2)) - path.index(i) - 2
        try:
            saves[gain].append(i)
        except KeyError:
            saves[gain] = [i]

    if (i[0] - 1, i[1]) not in path[path.index(i):] and (i[0] - 2, i[1]) in path[path.index(i):]:
        gain = path.index((i[0] - 2, i[1])) - path.index(i) -  2
        try:
            saves[gain].append(i)
        except KeyError:
            saves[gain] = [i]

    if (i[0] + 1, i[1]) not in path[path.index(i):] and (i[0] + 2, i[1]) in path[path.index(i):]:
        gain = path.index((i[0] + 2, i[1])) - path.index(i) - 2
        try:
            saves[gain].append(i)
        except KeyError:
            saves[gain] = [i]

total = 0
for k, v in saves.items():
    if k >= 100:
        total += len(v)
print(total)

