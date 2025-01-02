from collections import defaultdict

class Point():

    def __init__(self, row, col, value, even=True):    
        self.row = row
        self.col = col
        self.value = value
        self.is_current = False
        if value == "O":
            if even:
                self.value = "["
            else:
                self.value = "]"

    def __repr__(self):
        return f"({self.row}, {self.col})"

with open("data/15.txt", "r") as file:
    wd = file.read()
    map, directions = wd.split("\n\n")
    directions = "".join([i.strip() for i in directions.split("\n")])

out = defaultdict(lambda: defaultdict(lambda: None))
for irow, row in enumerate(map.split("\n")):
    for icol, col in enumerate(row):
        out[irow][icol*2] = Point(irow, icol*2, col, even=True)
        out[irow][icol*2+1] = Point(irow, icol*2+1, col, even=False)
        if col == "@":
            start = out[irow][icol*2]
            start.is_current = True
            start.value = "."
            first_position = (irow, icol*2)
            out[irow][icol*2+1].value = "."
print(out)
iteration = 0
position = first_position
for direction in directions:
    iteration += 1
    draw = ""
    for row in out.values():
        for col in row.values():
            if col.is_current:
                draw += "@"
            else:
                draw += col.value
        draw += "\n"

    print(iteration, "\n", draw, "\n", position, direction, out[position[0]][position[1]].value, sum([j.value == "O" for i in out.values() for j in i.values()]))
    if direction == "v":
        next_hole = out[position[0]+1][position[1]]
        if next_hole.value == "#":
            continue
        if next_hole.value == ".":
            out[position[0]][position[1]].is_current = False
            out[position[0]+1][position[1]].is_current = True
            position = (position[0]+1, position[1])
            continue 

        # Adapt the algorithm:
        # - if you find a [ you need to look for the remaining one at col+1 and then see what is below each of them
        # - if you find a ] you need to look for the remaining one at col-1 and then see what is below each of them
        # This should go recursively and if anyone of the children bumps on a # then noone moves
        stoppers = [out[position[0]+2][position[1]]]
        to_move = [out[position[0]+1][position[1]]]
        if next_hole.value == "[":
            to_move.append(out[position[0]+1][position[1]+1])
            stoppers.append(out[position[0]+2][position[1]+1])
        else:
            to_move.append(out[position[0]+1][position[1]-1])
            stoppers.append(out[position[0]+2][position[1]-1])
        while True:
            print("to move", to_move, "stoppers", stoppers)
            if any([i.value == "#" for i in stoppers]):
                break
            if all([i.value == "." for i in stoppers]):
                to_move = sorted(to_move, key=lambda x: -x.row)
                # perform the moves, in an ascending order
                for i in to_move:
                    # replace the value of i with the value above
                    tmp = out[i.row][i.col].value
                    out[i.row][i.col].value = out[i.row+1][i.col].value
                    out[i.row+1][i.col].value = tmp
                out[position[0]+1][position[1]].is_current = True
                out[position[0]][position[1]].is_current = False
                position = (position[0]+1, position[1])
                break
            # iterate
            for i in stoppers:
                if i.value == "[":
                    to_move.append(out[i.row][i.col])
                    to_move.append(out[i.row][i.col+1])
                    stoppers = [k for k in stoppers if k != i]
                    stoppers.append(out[i.row+1][i.col])
                    stoppers.append(out[i.row+1][i.col+1])
                elif i.value == "]":
                    to_move.append(out[i.row][i.col])
                    to_move.append(out[i.row][i.col-1])
                    stoppers = [k for k in stoppers if k != i]
                    stoppers.append(out[i.row+1][i.col])
                    stoppers.append(out[i.row+1][i.col-1])
            stoppers = list(set(stoppers))
            to_move = list(set(to_move))
    if direction == "^":
        next_hole = out[position[0]-1][position[1]]
        if next_hole.value == "#":
            continue
        if next_hole.value == ".":
            out[position[0]][position[1]].is_current = False
            out[position[0]-1][position[1]].is_current = True
            position = (position[0]-1, position[1])
            continue

        # Adapt the algorithm:
        # - if you find a [ you need to look for the remaining one at col+1 and then see what is below each of them
        # - if you find a ] you need to look for the remaining one at col-1 and then see what is below each of them
        # This should go recursively and if anyone of the children bumps on a # then noone moves
        stoppers = [out[position[0]-2][position[1]]]
        to_move = [out[position[0]-1][position[1]]]
        if next_hole.value == "[":
            to_move.append(out[position[0]-1][position[1]+1])
            stoppers.append(out[position[0]-2][position[1]+1])
        else:
            to_move.append(out[position[0]-1][position[1]-1])
            stoppers.append(out[position[0]-2][position[1]-1])
        while True:
            print("to move", to_move, "stoppers", stoppers)
            if any([i.value == "#" for i in stoppers]):
                break
            if all([i.value == "." for i in stoppers]):
                to_move = sorted(to_move, key=lambda x: x.row)
                # perform the moves, in an ascending order
                print("here", position, position[0], position[1], to_move)
                for i in to_move:
                    # replace the value of i with the value above
                    tmp = out[i.row][i.col].value
                    out[i.row][i.col].value = out[i.row-1][i.col].value
                    out[i.row-1][i.col].value = tmp
                out[position[0]-1][position[1]].is_current = True
                out[position[0]][position[1]].is_current = False
                position = (position[0]-1, position[1])
                break
            # iterate
            for i in stoppers:
                if i.value == "[":
                    to_move.append(out[i.row][i.col])
                    to_move.append(out[i.row][i.col+1])
                    stoppers = [k for k in stoppers if k != i]
                    stoppers.append(out[i.row-1][i.col])
                    stoppers.append(out[i.row-1][i.col+1])
                elif i.value == "]":
                    to_move.append(out[i.row][i.col])
                    to_move.append(out[i.row][i.col-1])
                    stoppers = [k for k in stoppers if k != i]
                    stoppers.append(out[i.row-1][i.col])
                    stoppers.append(out[i.row-1][i.col-1])
            stoppers = list(set(stoppers))
            to_move = list(set(to_move))

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
            print(next_holes)
            next_hole = max(next_holes, key=lambda x: x.col)
            for i in range(next_hole.col, position[1] - 1):
                print("switching", i, i+1, out[position[0]][i].value, out[position[0]][i+1].value)
                out[position[0]][i].value = out[position[0]][i+1].value
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
            for i in range(next_hole.col, position[1] + 1, -1):
                out[position[0]][i].value = out[position[0]][i-1].value
            new_position = (position[0], position[1] + 1)
            out[new_position[0]][new_position[1]].is_current = True
            out[position[0]][position[1]].is_current = False
            out[new_position[0]][new_position[1]].value = "."
            position = new_position
        else:
            continue


draw = ""
for row in out.values():
    for col in row.values():
        if col.is_current:
            draw += "@"
        else:
            draw += col.value
    draw += "\n"
print(draw)


total = 0
for row in out.values():
    for col in row.values():
        if col.value == "[":
            total += col.row*100 + col.col
print(total)