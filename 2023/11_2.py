file = 'data/11.txt'

class Galaxy:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return "%s-%s" % (self.row, self.col)

with open(file, 'r') as open_file:
    data = open_file.read()
galaxies = []

for irow, row in enumerate(data.split("\n")):

    lrow = len(row)
    for ichar, char in enumerate(row):
        if char == ".":
            continue
        galaxies.append(Galaxy(irow, ichar))


colset = {r for r in range(lrow)}
rowset = {r for r in range(irow)}

# Expand the universe
for i in galaxies:
    if i.col in colset:
        colset.remove(i.col)
    if i.row in rowset:
        rowset.remove(i.row)

for galaxy in galaxies:
    nb_col_to_add = len([k for k in colset if k < galaxy.col])
    nb_rows_to_add = len([k for k in rowset if k < galaxy.row])
    print(galaxy, nb_col_to_add, nb_rows_to_add)

    galaxy.col = galaxy.col + nb_col_to_add*999999
    galaxy.row = galaxy.row + nb_rows_to_add*999999

print(colset, rowset, [str(g) for g in galaxies])


total = 0
for i1, g1 in enumerate(galaxies):
    for i2, g2 in enumerate(galaxies):
        if i1 <= i2:
            continue
        total += (abs(g1.col-g2.col)+abs(g1.row-g2.row))

print(total)
