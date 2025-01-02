from collections import defaultdict

class Point():

    def __init__(self, row, col, value):    
        self.row = row
        self.col = col
        self.value = value
        self.is_current = False

    def __repr__(self):
        return f"({self.row}, {self.col})"

with open("data/15.txt", "r") as file:
    wd = file.read()
    map, directions = wd.split("\n\n")
    directions = "".join([i.strip() for i in directions.split("\n")])

out = defaultdict(lambda: defaultdict(lambda: None))
for irow, row in enumerate(map.split("\n")):
    for icol, col in enumerate(row):
        out[irow][icol] = Point(irow, icol, col)
        if col == "@":
            start = out[irow][icol]
            start.is_current = True
            start.value = "."
            first_position = (irow, icol)
print(out)

position = first_position
for direction in directions:

    draw = ""
    for row in out.values():
        for col in row.values():
            if col.is_current:
                draw += "@"
            else:
                draw += col.value
        draw += "\n"

    print(position, direction, out[position[0]][position[1]].value, sum([j.value == "O" for i in out.values() for j in i.values()]))
    if direction == "v":
        next_hole = out[position[0]+1][position[1]]
        if next_hole.value == "#":
            continue
        if next_hole.value == ".":
            out[position[0]][position[1]].is_current = False
            out[position[0]+1][position[1]].is_current = True
            position = (position[0]+1, position[1])
            continue
        # Find the next point in the column that has a value of "."
        next_holes = [out[k][position[1]] for k in out.keys()]
        next_stop = min([k.row for k in next_holes if k.row > position[0] and k.value == "#"])
        next_holes = [k for k in next_holes if k.row > position[0] and k.value == "." and k.row < next_stop]
        if next_holes:
            next_hole = min(next_holes, key=lambda x: x.row)
            for i in range(position[0] + 1, next_hole.row+1):
                out[i][position[1]].value = "O"
            new_position = (position[0] + 1, position[1])
            out[new_position[0]][new_position[1]].is_current = True
            out[position[0]][position[1]].is_current = False
            out[new_position[0]][new_position[1]].value = "."
            position = new_position
        else:
            continue
    if direction == "^":
        next_hole = out[position[0]-1][position[1]]
        if next_hole.value == "#":
            continue
        if next_hole.value == ".":
            out[position[0]][position[1]].is_current = False
            out[position[0]-1][position[1]].is_current = True
            position = (position[0]-1, position[1])
            continue
        next_holes = [out[k][position[1]] for k in out.keys()]  
        next_stop = max([k.row for k in next_holes if k.row < position[0] and k.value == "#"])
        next_holes = [k for k in next_holes if k.row < position[0] and k.value == "." and k.row > next_stop]
        if next_holes:
            next_hole = max(next_holes, key=lambda x: x.row)
            for i in range(position[0] - 1, next_hole.row-1, -1):
                out[i][position[1]].value = "O"
            new_position = (position[0] - 1, position[1])
            out[new_position[0]][new_position[1]].is_current = True
            out[position[0]][position[1]].is_current = False
            out[new_position[0]][new_position[1]].value = "."
            position = new_position
        else:
            continue
    if direction == "<":
        next_hole = out[position[0]][position[1]-1]
        if next_hole.value == "#":
            continue
        if next_hole.value == ".":
            out[position[0]][position[1]].is_current = False
            out[position[0]][position[1]-1].is_current = True
            position = (position[0], position[1]-1)
            continue
        next_holes = [i for i in out[position[0]].values() if i.value == "." and i.col < position[1]]
        next_stop = max([k.col for k in out[position[0]].values() if k.value == "#" and k.col < position[1]])
        next_holes = [k for k in next_holes if k.col < position[1] and k.value == "." and k.col > next_stop]
        if next_holes:
            next_hole = max(next_holes, key=lambda x: x.col)
            for i in range(position[1] - 1, next_hole.col-1, -1):
                out[position[0]][i].value = "O"
            new_position = (position[0], position[1] - 1)
            out[new_position[0]][new_position[1]].is_current = True
            out[position[0]][position[1]].is_current = False
            out[new_position[0]][new_position[1]].value = "."
            position = new_position
        else:
            continue
    if direction == ">":
        next_hole = out[position[0]][position[1]+1]
        print(next_hole.value)
        if next_hole.value == "#":
            continue
        if next_hole.value == ".":
            out[position[0]][position[1]].is_current = False
            out[position[0]][position[1]+1].is_current = True
            position = (position[0], position[1]+1)
            continue
        next_holes = [i for i in out[position[0]].values() if i.value == "." and i.col > position[1]]
        next_stop = min([k.col for k in out[position[0]].values() if k.value == "#" and k.col > position[1]])
        next_holes = [k for k in next_holes if k.col > position[1] and k.value == "." and k.col < next_stop]
        if next_holes:
            next_hole = min(next_holes, key=lambda x: x.col)
            for i in range(position[1] + 1, next_hole.col+1):
                out[position[0]][i].value = "O"
            new_position = (position[0], position[1] + 1)
            out[new_position[0]][new_position[1]].is_current = True
            out[position[0]][position[1]].is_current = False
            out[new_position[0]][new_position[1]].value = "."
            position = new_position
        else:
            continue

total = 0
for row in out.values():
    for col in row.values():
        if col.value == "O":
            total += col.row*100 + col.col
print(total)