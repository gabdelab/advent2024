import sys
file = 'data/16.txt'

mirrors = {}

directions = {
    "/": {"right": "top", "top": "right", "left": "bottom", "bottom": "left"},
    "\\": {"left": "top", "top": "left", "right": "bottom", "bottom": "right"}
}
propagated = set()
sys.setrecursionlimit(4000)

class Mirror:

    def __init__(self, row, col, char):
        self.row = row
        self.col = col
        self.char = char
        self.traversed = False

    def __repr__(self):
        return "%s,%s,%s - %s" % (self.char,self.row, self.col, self.traversed)

def propagate(mirror, direction):
    # We arrive on the given mirror with the given direction
    irow, icol = mirror.row, mirror.col
    mirror.traversed = True
    if str(mirror.row)+ "-" +str(mirror.col) + str(direction) in propagated:
        return
    propagated.add(str(mirror.row)+"-"+str(mirror.col) + str(direction))
    out_direction = [direction]
    if mirror.char in ["/", "\\"]:
        out_direction = [directions[mirror.char][direction]]
    if mirror.char == "-" and direction in ("left", "right"):
        out_direction = [direction]
    if mirror.char == "|" and direction in ("top", "bottom"):
        out_direction = [direction]

    # Split
    if mirror.char == "-" and direction in ("top", "bottom"):
        out_direction = ["left", "right"]
    if mirror.char == "|" and direction in ("left", "right"):
        out_direction = ["top", "bottom"]

    for odir in out_direction:
        out_mirror = None
        if odir == "right":
            try:
                out_mirror = mirrors[irow][icol+1]
            except:
                out_mirror = None
        if odir == "top":
            try:
                out_mirror = mirrors[irow-1][icol]
            except:
                out_mirror = None
        if odir == "left":
            try:
                out_mirror = mirrors[irow][icol-1]
            except:
                out_mirror = None
        if odir == "bottom":
            try:
                out_mirror = mirrors[irow+1][icol]
            except:
                out_mirror = None
        if out_mirror:
            propagate(out_mirror, odir)


with open(file, 'r') as open_file:
    data = open_file.read()
mirrors = {}
nb_row = 0
for irow, row in enumerate(data.split("\n")):
    nb_row += 1
    mirrors[irow] = {}
    for icol, char in enumerate(row):
        mirrors[irow][icol] = Mirror(irow, icol, char)
    nb_col = len(row)

maximum = 0
for irow in range(nb_row):
    total = 0
    propagate(mirrors[irow][0], "right")
    for row in mirrors.values():
        for col in row.values():
            if col.traversed:
                total += 1
    if total > maximum:
        print("found a new max", maximum, total)
        maximum = total
    for row in mirrors.values():
        for col in row.values():
            col.traversed = False
    propagated = set()

for irow in range(nb_row):
    total = 0
    propagate(mirrors[irow][nb_col-1], "left")
    for row in mirrors.values():
        for col in row.values():
            if col.traversed:
                total += 1
    if total > maximum:
        print("found a new max", maximum, total)
        maximum = total
    for row in mirrors.values():
        for col in row.values():
            col.traversed = False
    propagated = set()

for column in range(nb_col):
    total = 0
    propagate(mirrors[0][column], "bottom")
    for row in mirrors.values():
        for col in row.values():
            if col.traversed:
                total += 1
    if column == 3:
        data = ""
        for row in mirrors.values():
            for col in row.values():
                if col.traversed:
                    data += "#"
                else:
                    data += "." 

            data += "\n"
        print(data)
        print(total)
    if total > maximum:
        print("found a new max", maximum, total)
        maximum = total
    for row in mirrors.values():
        for col in row.values():
            col.traversed = False
    propagated = set()

for column in range(nb_col):
    total = 0
    propagate(mirrors[nb_row-1][column], "top")
    for row in mirrors.values():
        for col in row.values():
            if col.traversed:
                total += 1
    if total > maximum:
        print("found a new max", maximum, total)
        maximum = total
    for row in mirrors.values():
        for col in row.values():
            col.traversed = False
    propagated = set()

print(maximum)
