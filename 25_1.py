locks, keys = [], []

with open("data/25.txt", "r") as file:
    wd = file.read()

grids = wd.split("\n\n")

for grid in grids: 
    if grid[0] == "#":
        shape = [0, 0, 0, 0, 0]
        rows = grid.split("\n")
        for row in rows[1:]:
            for i, char in enumerate(row):
                if char == "#":
                    shape[i] += 1
        locks.append(shape)
    else:
        shape = [5, 5, 5, 5, 5]
        rows = grid.split("\n")
        for row in rows[:-1]:
            for i, char in enumerate(row):
                if char == "#":
                    shape[i] -= 1
        keys.append(shape)

total = 0
for i in locks:
    for j in keys: 
        if all(i[k] <= j[k] for k in range(5)):
            print(i, j)
            total += 1
print(total)
