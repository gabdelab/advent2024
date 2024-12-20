data = {}
with open("data/20.txt", "r") as file:
    for iline, line in enumerate(file):
        data[iline] = {}
        for icol, col in enumerate(line.strip()):
            data[iline][icol] = col

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
for index, element in enumerate(path):
    # We want a gain of at least 50 so we look 50 spots ahead
    to_look_for = path[index + 50:]

    for item in to_look_for:
        gain = path.index(item) - index - abs(item[0] - element[0]) - abs(item[1] - element[1])
        if gain == 76:
            print(element, item)
        if abs(item[0] - element[0]) + abs(item[1] - element[1]) <= 20:
            try:
                saves[gain].append(element)
            except KeyError:
                saves[gain] = [element]

total = 0
for k, v in saves.items():
    print(k, len(v))
    if k >= 100:
        total += len(v)
print(total)

