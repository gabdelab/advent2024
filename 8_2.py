from collections import defaultdict
import itertools
class Point():
    def __init__(self, x, y, value="."):
        self.x = x
        self.y = y
        self.value = value
        self.antinode = False
    

data = {}
nodes = defaultdict(list)
with open("data/8.txt", "r") as file:
    for row_nb, line in enumerate(file):
        data[row_nb] = {}
        for col_nb, col in enumerate(line.strip()):
            data[row_nb][col_nb] = Point(row_nb, col_nb, col)
            if col != ".":
                nodes[col].append((row_nb, col_nb))
    size = len(data)

points = set()
for nodekey in nodes:
    # Get any 2 elements from the list of nodes
    if len(nodes[nodekey]) <= 1:
        continue
    for a, b in itertools.combinations(nodes[nodekey], 2):
        points.add(a)
        points.add(b)
        delta = (b[0]-a[0], b[1]-a[1])
        # Compute the symmetry in both sides and check if they are outside of range
        sym_a = (a[0]-delta[0], a[1]-delta[1])
        while not(sym_a[0] < 0 or sym_a[0] >= size or sym_a[1] < 0 or sym_a[1] >= size):
            points.add(sym_a)
            sym_a = (sym_a[0]-delta[0], sym_a[1]-delta[1])
        sym_b = (b[0]+delta[0], b[1]+delta[1])
        while not(sym_b[0] < 0 or sym_b[0] >= size or sym_b[1] < 0 or sym_b[1] >= size):
            points.add(sym_b)
            sym_b = (sym_b[0]+delta[0], sym_b[1]+delta[1])

print(points)
print(len(points))

a = ""
for i in range(size):
    for j in range(size):
        if (i, j) in points:
            a += "#"
        elif data[i][j].value != ".":
            a += data[i][j].value

        else:
            a += "."
    a += "\n"
print(a)