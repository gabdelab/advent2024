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
        if mirror.row == 6:
            print("fromage", mirror.char, direction, mirror.col)
        return
    if mirror.row == 6 and mirror.col == 91:
        print("yolo swaggy swag", propagated)
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
        if mirror.row == 6:
            print(mirror, direction, "out mirror:" , out_mirror, odir)
        if out_mirror:
            propagate(out_mirror, odir)


with open(file, 'r') as open_file:
    data = open_file.read()
mirrors = {}
for irow, row in enumerate(data.split("\n")):
    mirrors[irow] = {}
    for icol, char in enumerate(row):
        mirrors[irow][icol] = Mirror(irow, icol, char)

propagate(mirrors[0][0], "right")

data = ""
total = 0
for row in mirrors.values():
    for col in row.values():
        if col.traversed:
            data += "#"
            total += 1
        else:
            data += "." 
    data += "\n"
print(data)
print(total)